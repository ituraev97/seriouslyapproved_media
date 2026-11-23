import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
// LAST CONTACT 007 — US Airways 1549 (A320, N106US), Jan 15, 2009. Local frame: x east, z south, meters; origin = touchdown
// point from the NTSB docket performance study (N40°46'16.78" W74°00'20.50"). Track = EWR ASR-9 secondary returns (docket table 1a).
const TM = await (await fetch('timing.json')).json();
const GEO = await (await fetch('geo.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const sm = x => x * x * (3 - 2 * x);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const FT = 0.3048;
function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
function segStart(L) { let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--; return i === 0 ? 0 : TM[i].start; }
function segEnd(L) { let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++; return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2; }

// ---------- renderer
const QS = new URLSearchParams(location.search);
const PR = +(QS.get('pr') || window.PR || 0.7);
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true, logarithmicDepthBuffer: true });
renderer.setPixelRatio(PR); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 2, 120000);
const scene = new THREE.Scene();
const hdr = await new RGBELoader().loadAsync('sky.hdr'); hdr.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = hdr; scene.environmentIntensity = 0.9; scene.background = hdr; scene.backgroundIntensity = 0.85; scene.backgroundBlurriness = 0.05;
scene.fog = new THREE.Fog(0xc3ccd6, 14000, 52000);
scene.add(new THREE.HemisphereLight(0xdfe8ff, 0x606050, 0.6));
const sun = new THREE.DirectionalLight(0xfff1dc, 2.2); scene.add(sun, sun.target);
sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048); const sc0 = sun.shadow.camera; sc0.left = sc0.bottom = -60; sc0.right = sc0.top = 60; sc0.near = 1; sc0.far = 3000; sun.shadow.bias = -0.0005;
const SUNDIR = V(-0.55, 0.45, 0.70).normalize(); // low afternoon sun from the southwest (January, ~15:30)

// ---------- ground (USGS imagery, current)
const tl = new THREE.TextureLoader();
async function groundPlane(file, g, y, offs) {
  const tx = await tl.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const m = new THREE.Mesh(new THREE.PlaneGeometry(g[2], g[2]), new THREE.MeshLambertMaterial({ map: tx, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs }));
  m.rotation.x = -Math.PI / 2; m.position.set(g[0], y, g[1]); m.receiveShadow = true; scene.add(m); return m;
}
await groundPlane('far.jpg', GEO.far, -6, 6);
await groundPlane('wide.jpg', GEO.wide, -3, 4);
await groundPlane('river.jpg', GEO.river, -1.2, 2);
await groundPlane('near.jpg', GEO.near, 0, 0);
const P2 = a => V(a[0], 0, a[1]);
const LGA04 = P2(GEO.lga04), LGA22 = P2(GEO.lga22), TEB1 = P2(GEO.teb1);
const TD = V(0, 0, 0);

// ---------- track (t = seconds after 15:25:00 EST)
const RAD = GEO.radar.map(r => ({ t: r[0], x: r[2], z: r[3] }));
const rwDir = LGA22.clone().sub(LGA04).normalize();
const LIFT = LGA04.clone().add(rwDir.clone().multiplyScalar(1500));
const PTS = [{ t: 4, x: LGA04.x + rwDir.x * 150, z: LGA04.z + rwDir.z * 150 }, { t: 40, x: LIFT.x, z: LIFT.z }, ...RAD, { t: 343, x: 0, z: 0 }];
function rawXZ(t) { if (t <= PTS[0].t) return [PTS[0].x, PTS[0].z]; for (let i = 1; i < PTS.length; i++) if (t <= PTS[i].t) { const a = PTS[i - 1], b = PTS[i], k = (t - a.t) / (b.t - a.t); return [lerp(a.x, b.x, k), lerp(a.z, b.z, k)]; } const l = PTS[PTS.length - 1]; return [l.x, l.z]; }
const DT = 0.1, T1s = 360, SM = []; // smoothed (moving average, 7 s window; tighter near the ends)
for (let t = 0; t <= T1s + 1e-6; t += DT) {
  const w = t < 50 || t > 330 ? 1.0 : 3.5; let sx = 0, sz = 0, n = 0;
  for (let u = -w; u <= w + 1e-6; u += 0.5) { const [x, z] = rawXZ(clamp(t + u, 4, 343)); sx += x; sz += z; n++; }
  SM.push([sx / n, sz / n]);
}
function xzAt(t) { const i = clamp(t / DT, 0, SM.length - 1), i0 = Math.floor(i), i1 = Math.min(i0 + 1, SM.length - 1), k = i - i0; return [lerp(SM[i0][0], SM[i1][0], k), lerp(SM[i0][1], SM[i1][1], k)]; }
// altitude, ft (≈): climb keyframes from report text; after the peak, Mode C (−200 ft bias tapering to 0 by 15:29:00); last minute from AAR 1.16.1
const ALT = [[4, 0], [40, 0], [51, 700], [59.7, 900], [91.7, 1800], [125, 2500], [131.4, 2800], [150, 3060]];
for (const r of GEO.radar) { const t = r[0]; if (t > 151 && t < 286) { const off = t < 190 ? 200 : t < 240 ? lerp(200, 0, (t - 190) / 50) : 0; ALT.push([t, r[1] - off]); } }
ALT.push([289, 270], [300, 210], [316, 360], [330, 180], [343, 6]);
ALT.sort((a, b) => a[0] - b[0]);
function kf(K, t) { if (t <= K[0][0]) return K[0][1]; for (let i = 1; i < K.length; i++) if (t <= K[i][0]) { const a = K[i - 1], b = K[i]; return lerp(a[1], b[1], (t - a[0]) / (b[0] - a[0])); } return K[K.length - 1][1]; }
function altFt(t) { if (t >= 336) return kf(ALT, t); let s = 0, n = 0; const w = t > 280 ? 1 : 3; for (let u = -w; u <= w; u += 1) { s += kf(ALT, clamp(t + u, 0, 343)); n++; } return s / n; }
const IAS = [[131.4, 219], [150, 185], [190, 210], [210, 200], [240, 190], [289, 194], [306, 170], [316, 150], [343, 125]];
const AOA = [[0, 5], [131, 5], [150, 9], [190, 6], [289, 8], [325, 10], [343, 13]];
const TS = 131.4; // 15:27:11.4 thumps
function posAt(t) { const tt = Math.min(t, 343); const [x, z] = xzAt(tt); return V(x, Math.max(altFt(tt), 0) * FT + 2.2, z); }

// ---------- airplane (A320 model, clean white livery, scaled to A320 length 37.57 m)
const g = await new GLTFLoader().loadAsync('a320.glb'); const o = g.scene;
const white = new THREE.MeshStandardMaterial({ color: 0xeceef0, roughness: .35, metalness: .1 });
const glass = new THREE.MeshStandardMaterial({ color: 0x0f1822, roughness: .08, metalness: .7 });
const grey = new THREE.MeshStandardMaterial({ color: 0x9aa1a8, roughness: .4, metalness: .5 });
const dark = new THREE.MeshStandardMaterial({ color: 0x23272d, roughness: .5, metalness: .3 });
window.MATS = {};
const RX = new RegExp(window.GLASSRX || QS.get('glass') || 'glass|window|windshield', 'i');
const RG = new RegExp(window.GREYRX || QS.get('grey') || 'engine|metal|chrome|silver|alu', 'i');
const RD = new RegExp(window.DARKRX || QS.get('dark') || 'tire|tyre|rubber|black', 'i');
o.traverse(m => { if (!m.isMesh) return; const n = (m.material.name || '') + '|' + m.name; window.MATS[n] = (window.MATS[n] || 0) + 1;
  m.material = RX.test(n) ? glass : RD.test(n) ? dark : RG.test(n) ? grey : white; m.castShadow = true; m.receiveShadow = true; });
const inner = new THREE.Group(); inner.add(o);
let b = new THREE.Box3().setFromObject(inner); const sz = b.getSize(V(0, 0, 0));
if ((window.LONGAXIS || QS.get('ax') || (sz.x > sz.z ? 'x' : 'z')) === 'x') o.rotation.y = Math.PI / 2;
o.rotation.y += +(window.YAW ?? QS.get('yaw') ?? 180) * Math.PI / 180;
inner.updateMatrixWorld(true); b = new THREE.Box3().setFromObject(inner); const sc = 37.57 / (b.max.z - b.min.z); inner.scale.setScalar(sc); inner.updateMatrixWorld(true);
b = new THREE.Box3().setFromObject(inner); inner.position.set(-(b.min.x + b.max.x) / 2, -b.min.y - 2.2, -(b.min.z + b.max.z) / 2);
const HIDE = (window.HIDE || QS.get('hide') || 'Cylinder009,Cylinder012,Cylinder017,Cylinder019,Cylinder021,Cylinder022,Cylinder008,Cylinder006,Cylinder015,Cylinder013').split(',').filter(Boolean);
o.traverse(m => { if (m.isMesh && HIDE.some(h => m.name.includes(h))) m.visible = false; });
const rollG = new THREE.Group(), pitchG = new THREE.Group(); pitchG.add(inner); rollG.add(pitchG);
const jet = new THREE.Group(); jet.add(rollG); scene.add(jet);
window.BOX = [sz.x, sz.y, sz.z];
window.MESHES = []; { const bb0 = new THREE.Box3().setFromObject(inner); o.traverse(m => { if (!m.isMesh) return; const bb = new THREE.Box3().setFromObject(m); window.MESHES.push([m.name, +(bb.min.y - bb0.min.y).toFixed(2), +(bb.max.y - bb0.min.y).toFixed(2), +((bb.min.z + bb.max.z) / 2).toFixed(1), +((bb.min.x + bb.max.x) / 2).toFixed(1)]); }); }
const hdg = d => Math.atan2(d.x, d.z);
function attitude(t) {
  const tt = clamp(t, 5, 336), a = posAt(tt - 0.5), c = posAt(tt + 0.5), d = c.clone().sub(a);
  const gs = Math.hypot(d.x, d.z); const gam = Math.atan2(d.y, Math.max(gs, 1)) * 180 / Math.PI;
  const a2 = posAt(tt - 2.5), c2 = posAt(tt - 1.5), b2 = posAt(tt + 1.5), e2 = posAt(tt + 2.5);
  const h1 = hdg(c2.clone().sub(a2)), h2 = hdg(e2.clone().sub(b2)); let dh = h2 - h1; while (dh > Math.PI) dh -= 2 * Math.PI; while (dh < -Math.PI) dh += 2 * Math.PI;
  const om = dh / 4, bank = clamp(Math.atan(gs * om / 9.81) * 180 / Math.PI, -32, 32) * (1 - seg(t, 326, 333));
  const onGround = t < 40; return { h: hdg(gs > 0.05 ? d : rwDir), pitch: onGround ? 0 : gam + kf(AOA, t), bank: onGround ? 0 : -bank, gs };
}
function poseJet(t) {
  jet.visible = true;
  if (t <= 343) { const p = posAt(t), at = attitude(t); jet.position.copy(p); jet.rotation.set(0, at.h, 0);
    let pit = at.pitch; if (t > 336) pit = lerp(pit, 9.5, seg(t, 336, 341)); pitchG.rotation.set(-pit * Math.PI / 180, 0, 0); rollG.rotation.set(0, 0, at.bank * Math.PI / 180); return p; }
  const at = attitude(342.5), k = sm(seg(t, 343, 348)); jet.position.set(0, lerp(2.2, -1.6, k), 0); jet.rotation.set(0, at.h, 0);
  pitchG.rotation.set(-lerp(9.5, 2.5, k) * Math.PI / 180, 0, 0); rollG.rotation.set(0, 0, 0); return jet.position.clone();
}
// ---------- markers + path ribbon
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
const glowT = canvasTex(64, 64, g => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.3, 'rgba(255,255,255,.6)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
const gooseT = canvasTex(128, 64, g => { g.fillStyle = '#1b1a18'; g.beginPath(); g.ellipse(64, 34, 22, 7, 0, 0, 7); g.fill(); g.beginPath(); g.moveTo(50, 32); g.quadraticCurveTo(30, 6, 4, 14); g.quadraticCurveTo(34, 22, 60, 36); g.fill(); g.beginPath(); g.moveTo(74, 32); g.quadraticCurveTo(98, 6, 124, 14); g.quadraticCurveTo(94, 22, 68, 36); g.fill(); g.fillRect(84, 31, 18, 4); });
const pathPts = []; for (let t = 5; t <= 343; t += 1) pathPts.push(posAt(t));
const pathCurve = new THREE.CatmullRomCurve3(pathPts);
const pathMat = new THREE.MeshBasicMaterial({ color: 0x3CFF8F, transparent: true, opacity: 0, depthWrite: false, fog: false });
const pathMesh = new THREE.Mesh(new THREE.TubeGeometry(pathCurve, 900, 14, 6, false), pathMat);
const topMat = pathMat.clone(); const topMesh = new THREE.Mesh(new THREE.TubeGeometry(pathCurve, 900, 70, 6, false), topMat); topMesh.renderOrder = 4; scene.add(topMesh); pathMesh.renderOrder = 4; scene.add(pathMesh);
function dot(c, s) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, color: c, transparent: true, depthWrite: false, depthTest: false, fog: false })); sp.scale.setScalar(s); sp.renderOrder = 6; scene.add(sp); return sp; }
const STRIKE = posAt(TS), dStrike = dot(0xFF2E2E, 500), dTD = dot(0xFFB020, 380); dStrike.position.copy(STRIKE); dTD.position.set(0, 30, 0);
// geese (illustrative flock; positions not recorded)
const flock = []; { let s = 7; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647;
  for (let i = 0; i < 16; i++) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: gooseT, transparent: true, depthWrite: false })); sp.scale.set(1.8, 0.9, 1); scene.add(sp); flock.push({ sp, off: V((rnd() - .5) * 60, (rnd() - .5) * 12, (rnd() - .5) * 60), ph: rnd() * 6 }); } }
function flockAt(t) { const on = t > 118 && t < TS + 0.4; const a = attitude(TS); const fwd = V(Math.sin(a.h), 0, Math.cos(a.h));
  const c = STRIKE.clone().add(V(0, 3, 0)).add(fwd.clone().multiplyScalar(-(t - TS) * 3));
  flock.forEach((f, i) => { f.sp.visible = on && !(i < 4 && t > TS - 0.05); f.sp.position.copy(c).add(f.off).add(V(0, Math.sin(t * 6 + f.ph) * 0.3, 0)); f.sp.scale.set(1.8, 0.9 * (0.6 + 0.4 * Math.abs(Math.sin(t * 5 + f.ph))), 1); }); }
// spray at touchdown
const spray = []; for (let i = 0; i < 40; i++) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, color: 0xf4f7fa, transparent: true, depthWrite: false, opacity: 0 })); scene.add(sp); spray.push({ sp, a: i * 2.4, r: 3 + (i % 7) * 2.2, h: 2 + (i % 5) * 2.5 }); }
function sprayAt(t) { const k = seg(t, 342.8, 347); const on = t > 342.8 && t < 349; const at = attitude(342.5); const back = V(-Math.sin(at.h), 0, -Math.cos(at.h));
  spray.forEach((s, i) => { s.sp.visible = on; if (!on) return; const p = back.clone().multiplyScalar(6 + (i % 10) * 2.5).add(V(Math.cos(s.a) * s.r * (0.5 + k), s.h * Math.sin(Math.PI * clamp(k * 1.4)), Math.sin(s.a) * s.r * (0.5 + k)));
    s.sp.position.copy(p); s.sp.scale.setScalar(6 + 10 * k); s.sp.material.opacity = 0.8 * (1 - k); }); }

// ---------- HUD + events (times EST; t = s after 15:25:00)
const EV = [[-999, ''], [124.5, '15:27:05 · FLAPS RETRACTED · ≈2,500 FT'], [129, ''], [130.4, '15:27:10.4 · CAPT: “BIRDS”'], [131.4, '15:27:11.4 · THUMPS · BOTH ENGINES ROLL BACK'],
  [139, '15:27:19 · “IGNITION, START”'], [141, '15:27:21 · “I’M STARTING THE APU”'], [143, '15:27:23 · “MY AIRCRAFT”'], [147, ''], [150, '15:27:30 · PEAK ≈3,060 FT · 185 KT'], [153, '15:27:33 · “…LOST THRUST IN BOTH ENGINES”'], [160, ''],
  [190.6, '15:28:10 · “WE MAY END UP IN THE HUDSON”'], [198, ''], [229.9, '15:28:50 · “I’M NOT SURE WE CAN MAKE ANY RUNWAY”'], [236, ''], [243, '15:29:03 · TETERBORO? “YES”'], [249, ''], [251, '15:29:11 · PA: “BRACE FOR IMPACT”'], [258, ''],
  [268, '15:29:28 · “WE’RE GONNA BE IN THE HUDSON”'], [276, ''], [285.4, '15:29:45 · “PUT THE FLAPS OUT”'], [289, '15:29:49 · FLAPS 2 SELECTED'], [293, '15:29:53 · RADAR CONTACT LOST'], [299, ''],
  [303, '15:30:03 · F/O: “250 FEET IN THE AIR”'], [309, ''], [317, '15:30:17 · F/O: “GOT FLAPS TWO…”'], [322, ''], [324, '15:30:24 · GPWS: “TERRAIN, TERRAIN… PULL UP”'], [334, ''], [338, '15:30:38 · CAPT: “WE’RE GONNA BRACE”'],
  [343, '15:30:43 · TOUCHDOWN · 125 KT · 9.5° NOSE UP'], [352, '']];
const f2 = n => String(Math.floor(n)).padStart(2, '0');
const clock = t => { const x = 15 * 3600 + 25 * 60 + Math.min(t, 360); return `15:${f2(x % 3600 / 60)}:${f2(x % 60)}`; };
const since = t => { const d = t - TS; const a = Math.abs(d); return (d < 0 ? '−' : '+') + `${Math.floor(a / 60)}:${f2(a % 60)}`; };
function hud(t, show) {
  $('hud').style.opacity = show ? 1 : 0; $('ev').style.opacity = 0; if (!show) return;
  const al = t >= 343 ? 0 : altFt(t); $('halt').textContent = t >= 343 ? 'ON THE RIVER' : t < 40 ? 'ON RUNWAY 4' : '≈' + (Math.round(al / 10) * 10).toLocaleString('en-US');
  $('halt').style.fontSize = t >= 343 || t < 40 ? '34px' : '';
  $('hias').textContent = t < 130 || t > 343.5 ? '—' : '≈' + Math.round(kf(IAS, t)) + ' KT';
  const e = $('heng'); if (t < TS) { e.textContent = 'NORMAL'; e.style.color = '#3CFF8F'; } else if (t < TS + 4) { e.textContent = 'N1 82%→35% · 82%→15%'; e.style.color = '#FF2E2E'; } else { e.textContent = 'ALMOST TOTAL LOSS OF THRUST'; e.style.color = '#FF2E2E'; }
  $('ht').textContent = clock(t) + ' · ' + since(t);
  let ev = ''; for (const [a, x] of EV) if (t >= a) ev = x; if (ev) { $('ev').textContent = ev; $('ev').style.opacity = 1; }
}
function place(id, w3, show = 1) { const el = $(id), v = w3.clone().project(cam); const px = (v.x + 1) / 2 * 1920, py = (1 - v.y) / 2 * 1080; el.style.left = px + 'px'; el.style.top = py + 'px'; const inHud = $('hud').style.opacity !== '0' && px > 1250 && py < 640; el.style.opacity = (v.z < 1 && Math.abs(v.x) < 0.95 && Math.abs(v.y) < 0.92 && show && !inHud) ? show : 0; }
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }
function jetFrame(t) { const a = attitude(Math.min(t, 342.5)); const f = V(Math.sin(a.h), 0, Math.cos(a.h)), r = V(-f.z, 0, f.x); return { f, r }; }
const rel = (p, F, bk, side, up) => p.clone().add(F.f.clone().multiplyScalar(-bk)).add(F.r.clone().multiplyScalar(side)).add(V(0, up, 0));
const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_lga', 'L_teb', 'L_bird', 'L_hud', 'L_td', 'L_jet', 'L_man', 'L_nj'];
const HUDSON = V(-1500, 3, -9000), MAN = V(3500, 3, -4000), NJ = V(-4500, 3, -1500);

function renderAt(t) {
  const L = lineAt(t), vis = L.vis, s0 = segStart(L), s1 = segEnd(L), U = seg(t, s0, s1), u = t - s0;
  CARDS.forEach(c => c.style.opacity = 0); LBLS.forEach(id => $(id).style.opacity = 0);
  ['recon', 'cred', 'hud', 'ev'].forEach(id => $(id).style.opacity = 0);
  const fadeIn = clamp(u / 0.35), fadeOut = clamp((s1 - t) / 0.35);
  if (vis[0] === 'card') {
    const c = $('c_' + vis[1]); c.style.opacity = Math.min(fadeIn, fadeOut);
    c.querySelectorAll('[data-from]').forEach(el => { const d = T[el.dataset.from]; el.style.opacity = d ? clamp((t - d.start) / 0.4) : 1; });
    if (vis[1] === 'status') $('sweep').setAttribute('transform', `rotate(${(t * 60) % 360})`);
    return;
  }
  $('recon').style.opacity = 1; $('cred').style.opacity = .9;
  pathMat.opacity = 0; topMat.opacity = 0; dStrike.visible = false; dTD.visible = false;
  let st = 100, showHud = !['top', 'orbit'].includes(vis[1]); const sh = vis[1]; $('hud').style.opacity = showHud ? 1 : 0;
  if (sh === 'open') {
    st = lerp(108, 127, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, lerp(95, 70, U), lerp(-55, -40, U), lerp(14, 10, U)), rel(p, F, -60, 22, 0), 38);
    place('L_jet', p.clone().add(V(0, -12, 0)), seg(U, .05, .1) * (1 - seg(U, .45, .5)));
  } else if (sh === 'strike') {
    st = lerp(127.5, 146, sm(U)); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, lerp(60, 85, U), lerp(32, 48, U), lerp(6, 12, U)), rel(p, F, -40, 0, 0), 36);
  } else if (sh === 'strike2') {
    st = lerp(146, 162, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, 140, -90, 45), rel(p, F, -120, 120, -30), 40);
  } else if (sh === 'top') {
    jet.visible = false; showHud = false; topMat.opacity = .95 * fadeIn; dStrike.visible = dTD.visible = true;
    look(V(lerp(3600, 3200, U), lerp(24500, 23000, U), lerp(3500, 2500, U)), V(3200, 0, -6000), 40);
    place('L_lga', LGA04.clone().setY(3)); place('L_teb', TEB1.clone().setY(3), seg(U, .1, .15)); place('L_bird', STRIKE, seg(U, .2, .25)); place('L_hud', HUDSON, seg(U, .3, .35)); place('L_td', TD.clone().setY(3), seg(U, .4, .45));
    place('L_man', MAN, seg(U, .5, .55)); place('L_nj', NJ, seg(U, .5, .55));
  } else if (sh === 'climb') {
    st = lerp(48, 125, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, lerp(120, 200, U), lerp(70, 120, U), lerp(18, 45, U)), rel(p, F, -80, -20, 0), 40);
    place('L_lga', LGA04.clone().setY(3), 1 - seg(U, .35, .4));
  } else if (sh === 'turn') {
    st = lerp(146, 200, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, 130, 120, 40), rel(p, F, -150, -30, -25), 40); place('L_hud', HUDSON, seg(U, .4, .45));
  } else if (sh === 'turn2') {
    st = lerp(205, 268, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, 150, -55, 35), rel(p, F, -700, 320, -150), 42);
    place('L_teb', TEB1.clone().setY(3), seg(U, .1, .15)); place('L_hud', HUDSON, seg(U, .05, .1));
  } else if (sh === 'river') {
    st = lerp(283, 305, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, lerp(130, 90, U), -120, 25), rel(p, F, -40, 80, -4), 40); place('L_hud', p.clone().add(F.f.clone().multiplyScalar(900)).setY(3), seg(U, .05, .1) * (1 - seg(U, .5, .55)));
  } else if (sh === 'river2') {
    st = lerp(305, 322, U); const p = poseJet(st), F = jetFrame(st);
    look(rel(p, F, -110, 70, -5), p.clone().add(V(0, 2, 0)), 36);
  } else if (sh === 'final') {
    st = lerp(326, 342.2, U); const p = poseJet(st), F = jetFrame(st);
    const c = rel(p, F, lerp(70, 48, U), lerp(38, 30, U), lerp(6, 4, U)); c.y = Math.max(c.y, 4); look(c, rel(p, F, -45, 0, -2), 38);
  } else if (sh === 'touch') {
    st = lerp(339.5, 352, U); poseJet(st); const F = jetFrame(339.5);
    look(rel(TD, F, 50, 55, 9), rel(TD, F, -10, 0, 2), 40); place('L_td', TD.clone().setY(14), seg(st, 344, 345));
  } else if (sh === 'replay') {
    st = lerp(118, 344, U); const p = poseJet(st), F = jetFrame(st); pathMat.opacity = .1;
    const w = seg(st, 280, 343); look(rel(p, F, lerp(300, 80, w), lerp(220, 45, w), lerp(140, 8, w)), rel(p, F, -150, 0, -10), 40);
    if (st > TS - 3 && st < TS + 4) place('L_bird', STRIKE.clone().add(V(0, 15, 0)));
  } else if (sh === 'orbit') {
    st = 360; poseJet(st); showHud = false; const a = lerp(-0.4, 1.3, U), R = lerp(130, 95, U);
    look(V(Math.sin(a) * R, lerp(32, 20, U), Math.cos(a) * R), V(0, 0, 0), 38);
    place('L_hud', V(-500, 3, -1400), seg(U, 0, .05)); place('L_man', V(1300, 30, 200), seg(U, .1, .15)); place('L_nj', V(-900, 30, 300), seg(U, .1, .15));
  }
  flockAt(st); sprayAt(st);
  const jp = jet.position; sun.position.copy(jp).add(SUNDIR.clone().multiplyScalar(1500)); sun.target.position.copy(jp); sun.target.updateMatrixWorld();
  hud(st, showHud);
  renderer.render(scene, cam);
}
window.THREE = THREE; window.renderAt = renderAt; window.SCN = scene; window.JET = jet; window.REN = renderer; window.CAM = cam; window.look = look; window.posAt = posAt; window.poseJet = poseJet; window.attitude = attitude; window.altFt = altFt;
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
