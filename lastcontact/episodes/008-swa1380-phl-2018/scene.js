import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
// LAST CONTACT 008 — Southwest 1380 (B737-700 N772SW), Apr 17 2018. Frame: x east, z south, meters; origin PHL (39.8669N 75.2458W).
// Track/attitude = NTSB docket DCA18MA142 FDR (1 Hz). t = seconds after 11:03:33 EDT (left engine failure).
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

const QS = new URLSearchParams(location.search);
const PR = +(QS.get('pr') || window.PR || 0.7);
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true, logarithmicDepthBuffer: true });
renderer.setPixelRatio(PR); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 1, 600000);
const scene = new THREE.Scene();
const hdr = await new RGBELoader().loadAsync('sky.hdr'); hdr.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = hdr; scene.environmentIntensity = 0.9; scene.background = hdr; scene.backgroundIntensity = 0.9; scene.backgroundBlurriness = 0.05;
const FOG = new THREE.Fog(0xc3ccd6, 20000, 90000);
scene.fog = FOG;
scene.add(new THREE.HemisphereLight(0xdfe8ff, 0x606050, 0.6));
const sun = new THREE.DirectionalLight(0xfff4e6, 2.3); scene.add(sun, sun.target);
sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048); const sc0 = sun.shadow.camera; sc0.left = sc0.bottom = -60; sc0.right = sc0.top = 60; sc0.near = 1; sc0.far = 3000; sun.shadow.bias = -0.0005;
const SUNDIR = V(0.25, 0.85, 0.45).normalize();

const tl = new THREE.TextureLoader();
async function groundPlane(file, g, y, offs) {
  const tx = await tl.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const m = new THREE.Mesh(new THREE.PlaneGeometry(g[2], g[2]), new THREE.MeshLambertMaterial({ map: tx, color: 0x8c8c8c, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs }));
  m.rotation.x = -Math.PI / 2; m.position.set(g[0], y, g[1]); m.receiveShadow = true; scene.add(m); return m;
}
await groundPlane('huge.jpg', GEO.huge, -60, 10);
await groundPlane('far.jpg', GEO.far, -20, 8);
await groundPlane('wide.jpg', GEO.wide, -8, 5);
await groundPlane('mid.jpg', GEO.mid, -3, 3);
await groundPlane('near.jpg', GEO.near, 0, 0);
const P2 = a => V(a[0], 0, a[1]);
const TD = V(0, 0, 0); const THR = P2(GEO.r27l_thr), MDT = P2(GEO.mdt), PHL = P2(GEO.phl);

// ---------- track from FDR
const TRK = GEO.trk; // [t,x,z,alt,ias,hdg,roll,pitch,flap,n1a,n1b,wow]
function col(t, c) { if (t <= TRK[0][0]) return TRK[0][c]; if (t >= TRK[TRK.length - 1][0]) return TRK[TRK.length - 1][c];
  const i = Math.floor(t - TRK[0][0]), a = TRK[i], b = TRK[i + 1], k = (t - a[0]) / (b[0] - a[0]); return lerp(a[c], b[c], k); }
function colS(t, c, w) { let s = 0, n = 0; for (let u = -w; u <= w + 1e-6; u += w / 4 || 1) { s += col(t + u, c); n++; } return s / n; }
const END = TRK[TRK.length - 1][0];
const ALTOFF = 125; // ft: pressure altitude → height above field (≈)
function altFt(t) { return Math.max(0, colS(t, 3, 2) - ALTOFF); }
function posAt(t) { return V(colS(t, 1, 2), altFt(t) * FT + 2.2, colS(t, 2, 2)); }
let lastH = Math.atan2(-1, 0);
function headingAt(t) { const a = posAt(t - 3), b = posAt(t + 3), d = b.clone().sub(a); if (Math.hypot(d.x, d.z) < 4) return lastH; return Math.atan2(d.x, d.z); }
function attitude(t) { const h = headingAt(t); lastH = h; return { h, bank: colS(t, 6, 0.8), pitch: colS(t, 7, 0.8) }; }
const TS = 0; // failure
const ROLLSIGN = +(QS.get('rs') || window.RS || 1);

// ---------- airplane (generic B737, clean white, scaled to 737-700 length 33.6 m)
const g = await new GLTFLoader().loadAsync('b737.glb'); const o = g.scene;
const white = new THREE.MeshStandardMaterial({ color: 0xeceef0, roughness: .35, metalness: .1 });
const glass = new THREE.MeshStandardMaterial({ color: 0x0f1822, roughness: .08, metalness: .7 });
const grey = new THREE.MeshStandardMaterial({ color: 0x9aa1a8, roughness: .4, metalness: .5 });
const dark = new THREE.MeshStandardMaterial({ color: 0x23272d, roughness: .5, metalness: .3 });
window.MATS = {};
const RX = new RegExp(window.GLASSRX || QS.get('glass') || 'glass|window|windshield|cockpit', 'i');
const RG = new RegExp(window.GREYRX || QS.get('grey') || 'engine|metal|chrome|silver|alu', 'i');
const RD = new RegExp(window.DARKRX || QS.get('dark') || 'tire|tyre|rubber|black', 'i');
o.traverse(m => { if (!m.isMesh) return; const n = (m.material.name || '') + '|' + m.name; window.MATS[n] = (window.MATS[n] || 0) + 1;
  m.material = RX.test(n) ? glass : RD.test(n) ? dark : RG.test(n) ? grey : white; m.castShadow = true; m.receiveShadow = true; });
const inner = new THREE.Group(); inner.add(o);
let b = new THREE.Box3().setFromObject(inner); const sz = b.getSize(V(0, 0, 0));
if ((window.LONGAXIS || QS.get('ax') || (sz.x > sz.z ? 'x' : 'z')) === 'x') o.rotation.y = Math.PI / 2;
o.rotation.y += +(window.YAW ?? QS.get('yaw') ?? 0) * Math.PI / 180;
inner.updateMatrixWorld(true); b = new THREE.Box3().setFromObject(inner); const sc = 33.6 / (b.max.z - b.min.z); inner.scale.setScalar(sc); inner.updateMatrixWorld(true);
b = new THREE.Box3().setFromObject(inner); inner.position.set(-(b.min.x + b.max.x) / 2, -b.min.y - 2.2, -(b.min.z + b.max.z) / 2);
const HIDE = (window.HIDE || QS.get('hide') || 'Torus01-,Torus02-,Torus19-,Torus20-,Torus21-,Torus22-,Cylinder04-,Cylinder14-,Cylinder15-,Cylinder16-,Cylinder17-,Cylinder18-,Cylinder19-,Cylinder20-,Cylinder21-,Cylinder22-,Cylinder23-,Box10-,Box15-,Box16-,Box17-,Box18-,Sphere03-,Object01_0-,Object02_0-,Cylinder133-,Cylinder138-,Cylinder144-,Cylinder149-,Cylinder145-,Cylinder134-,Cylinder146-,Cylinder135-,Cylinder143-,Cylinder132-,Cylinder147-,Cylinder136-,Cylinder148-,Cylinder137-,Box539-,Box535-,Box538-,Box534-,Box533-,Box537-,Object06-,Object08-,Object09-,Object10-').split(',').filter(Boolean);
o.traverse(m => { if (m.isMesh && HIDE.some(h => m.name.includes(h))) m.visible = false; });
const rollG = new THREE.Group(), pitchG = new THREE.Group(); pitchG.add(inner); rollG.add(pitchG);
const jet = new THREE.Group(); jet.add(rollG); scene.add(jet);
window.BOX = [sz.x, sz.y, sz.z];
window.MESHES = []; { const bb0 = new THREE.Box3().setFromObject(inner); o.traverse(m => { if (!m.isMesh) return; const bb = new THREE.Box3().setFromObject(m); window.MESHES.push([m.name, +(bb.min.y - bb0.min.y).toFixed(2), +(bb.max.y - bb0.min.y).toFixed(2), +(bb.min.x).toFixed(1), +(bb.max.x).toFixed(1), +(bb.min.z).toFixed(1), +(bb.max.z).toFixed(1)]); }); }
const GEARTOP = +(QS.get('gear') || window.GEARTOP || 0);
function poseJet(t) {
  jet.visible = true; const tt = clamp(t, TRK[0][0] + 4, END), p = posAt(tt), at = attitude(tt);
  jet.position.copy(p); jet.rotation.set(0, at.h, 0); pitchG.rotation.set(-at.pitch * Math.PI / 180, 0, 0); rollG.rotation.set(0, 0, ROLLSIGN * at.bank * Math.PI / 180);
  if (colS(tt, 11, 0.5) > 0.5) jet.position.y = 2.2 + 0.0; return jet.position.clone();
}
// ---------- markers, path ribbon, debris
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
const glowT = canvasTex(64, 64, g => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.3, 'rgba(255,255,255,.6)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
const pathPts = []; for (let t = -75; t <= END; t += 4) pathPts.push(posAt(t));
const pathCurve = new THREE.CatmullRomCurve3(pathPts);
const pathMat = new THREE.MeshBasicMaterial({ color: 0x3CFF8F, transparent: true, opacity: 0, depthWrite: false, fog: false });
const topMat = pathMat.clone();
const topMesh = new THREE.Mesh(new THREE.TubeGeometry(pathCurve, 1200, 380, 6, false), topMat); topMesh.renderOrder = 4; scene.add(topMesh);
const pathMesh = new THREE.Mesh(new THREE.TubeGeometry(pathCurve, 1200, 18, 6, false), pathMat); pathMesh.renderOrder = 4; scene.add(pathMesh);
function dot(c, s) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, color: c, transparent: true, depthWrite: false, depthTest: false, fog: false })); sp.scale.setScalar(s); sp.renderOrder = 6; scene.add(sp); return sp; }
const FBO = posAt(TS), dFbo = dot(0xFF2E2E, 2600), dTD = dot(0xFFB020, 700), dMdt = dot(0x3CFF8F, 2400), dPhl = dot(0xFFB020, 2400);
dFbo.position.copy(FBO); dTD.position.set(0, 30, 0); dMdt.position.copy(MDT).setY(100); dPhl.position.copy(PHL).setY(100);
const deb = []; { let s = 11; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647;
  for (let i = 0; i < 26; i++) { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, color: i % 3 ? 0xdfe3e8 : 0x8a919a, transparent: true, depthWrite: false })); scene.add(sp);
    deb.push({ sp, v: V((rnd() - .2) * 6, (rnd() - .6) * 3, -8 - rnd() * 14), s: .5 + rnd() * 1.4, d: rnd() * .8 }); } }
function debAt(t) { const F = jetF(t); deb.forEach(d => { const k = t - TS - d.d; const on = k > 0 && k < 5;
  d.sp.visible = on; if (!on) return; const base = jet.position.clone().add(F.r.clone().multiplyScalar(-5)).add(V(0, -1, 0)).add(F.f.clone().multiplyScalar(4));
  const w = d.v.clone(); const pos = base.add(F.r.clone().multiplyScalar(-w.x * k * -1)).add(V(0, w.y * k - 0.5 * 6 * k * k * 0.3, 0)).add(F.f.clone().multiplyScalar(w.z * k * 0.45));
  d.sp.position.copy(pos); d.sp.scale.setScalar(d.s * (1 + k)); d.sp.material.opacity = 0.9 * (1 - k / 5); }); }

// ---------- HUD + events
const EV = [[-999, ''], [0, '11:03:33 · LEFT ENGINE FAILS · FL320'], [4.5, ''], [6, '11:03:39 · CABIN ALTITUDE WARNING'], [9, ''], [10.5, '11:03:44 · ROLL 41° LEFT'], [15, ''], [24.5, '11:03:58 · BOTH ENGINES TO IDLE'], [30, ''], [36, '11:04:09 · LEFT ENGINE FUEL CUTOFF PARAMETER: RUN → CUTOFF'], [42, ''], [76, '11:04:49 · OXYGEN MASKS'], [80, '11:04:54 · “ENGINE FIRE DESCENDING”'], [88, ''], [139, '11:05:52 · CLEARED DIRECT TO PHILADELPHIA'], [147, ''], [357, '11:09:30 · CAPTAIN: “I’M GONNA TAKE IT” · 13,600 FT'], [365, ''], [701, '11:15:14 · FLIGHT ATTENDANT: “THE WINDOW IS COMPLETELY OUT”'], [709, ''], [762, '11:16:15 · 5° OF FLAPS'], [770, ''], [926, '11:18:59 · CLEARED TO LAND · RUNWAY 27L'], [934, ''], [1017, '11:20:30 · TOUCHDOWN · ≈171 KT'], [1030, '']];
const f2 = n => String(Math.floor(n)).padStart(2, '0');
const clock = t => { const x = 11 * 3600 + 3 * 60 + 33 + Math.round(t); return `11:${f2(x % 3600 / 60)}:${f2(x % 60)}`; };
const since = t => { const a = Math.abs(t - TS); return (t < TS ? '−' : '+') + `${Math.floor(a / 60)}:${f2(a % 60)}`; };
function hud(t, show) {
  $('hud').style.opacity = show ? 1 : 0; $('ev').style.opacity = 0; if (!show) return;
  const al = altFt(t); $('halt').textContent = colS(t, 11, 0.5) > .5 ? 'ON RUNWAY' : '≈' + (Math.round(al / 10) * 10).toLocaleString('en-US'); $('halt').style.fontSize = colS(t, 11, .5) > .5 ? '34px' : '';
  $('hias').textContent = Math.round(colS(t, 4, 1)) + ' KT';
  const n1a = col(t, 9), n1b = col(t, 10); const e = $('heng'); e.textContent = Math.round(n1a) + '% · ' + Math.round(n1b) + '%'; e.style.color = n1a < 80 && t > 0 ? '#FF2E2E' : '#3CFF8F';
  $('ht').textContent = clock(t) + ' · ' + since(t);
  let ev = ''; for (const [a, x] of EV) if (t >= a) ev = x; if (ev) { $('ev').textContent = ev; $('ev').style.opacity = 1; }
}
function place(id, w3, show = 1) { const el = $(id), v = w3.clone().project(cam); const px = (v.x + 1) / 2 * 1920, py = (1 - v.y) / 2 * 1080; el.style.left = px + 'px'; el.style.top = py + 'px'; const inHud = $('hud').style.opacity !== '0' && px > 1380 && py < 460; el.style.opacity = (v.z < 1 && v.z > -1 && px > 60 && px < 1860 && py > 100 && py < 1000 && !inHud) ? show : 0; }
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }
function jetF(t) { const a = attitude(clamp(t, TRK[0][0] + 4, END)); const f = V(Math.sin(a.h), 0, Math.cos(a.h)), r = V(-f.z, 0, f.x); return { f, r }; }
const rel = (p, F, bk, side, up) => p.clone().add(F.f.clone().multiplyScalar(-bk)).add(F.r.clone().multiplyScalar(side)).add(V(0, up, 0));
const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_lga', 'L_fbo', 'L_mdt', 'L_phl', 'L_td', 'L_jet', 'L_riv'];

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
  pathMat.opacity = 0; topMat.opacity = 0; dFbo.visible = false; dTD.visible = false; dMdt.visible = false; dPhl.visible = false;
  scene.fog = FOG; let st = 0, showHud = !['top', 'top2', 'orbit'].includes(vis[1]); const sh = vis[1]; $('hud').style.opacity = showHud ? 1 : 0;
  if (sh === 'open') {
    st = lerp(-34, 14, U); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, lerp(70, 55, U), lerp(-40, -32, U), lerp(12, 9, U)), rel(p, F, -45, 14, 0), 38);
    place('L_jet', p.clone().add(V(0, -10, 0)), seg(U, .05, .1) * (1 - seg(U, .4, .45)));
  } else if (sh === 'fbo') {
    st = lerp(-4, 16, sm(U)); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, lerp(-10, 14, U), lerp(34, 26, U), lerp(7, 9, U)), rel(p, F, 0, 8, 0), 34);
  } else if (sh === 'fbo2') {
    st = lerp(0, 14, U); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, 52, 24, 14), rel(p, F, -10, 0, 0), 40);
  } else if (sh === 'climb') {
    st = lerp(-78, -4, U); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, lerp(80, 130, U), lerp(-60, -95, U), lerp(18, 38, U)), rel(p, F, -60, 0, 0), 40);
  } else if (sh === 'top' || sh === 'top2') {
    jet.visible = false; showHud = false; scene.fog = null; topMat.opacity = .95 * fadeIn; pathMat.opacity = .9 * fadeIn; dFbo.visible = dTD.visible = dPhl.visible = true;
    if (sh === 'top') { look(V(lerp(-40000, -36000, U), lerp(165000, 150000, U), lerp(40000, 36000, U)), V(-40000, 0, -34000), 40);
      place('L_fbo', FBO.clone().setY(200), seg(U, .15, .2)); place('L_phl', PHL.clone().setY(200), seg(U, .35, .4)); }
    else { dMdt.visible = true; look(V(lerp(-78000, -70000, U), lerp(150000, 120000, U), lerp(40000, 34000, U)), V(-74000, 0, -30000), 40);
      place('L_mdt', MDT.clone().setY(300), seg(U, .1, .15)); place('L_fbo', FBO.clone().setY(200), seg(U, .2, .25)); place('L_phl', PHL.clone().setY(200), seg(U, .3, .35)); }
  } else if (sh === 'desc') {
    st = lerp(14, 130, U); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, lerp(130, 160, U), lerp(-80, -110, U), lerp(30, 50, U)), rel(p, F, -80, 0, -10), 40);
  } else if (sh === 'desc2') {
    st = lerp(340, 690, U); const p = poseJet(st), F = jetF(st);
    look(rel(p, F, lerp(130, 110, U), lerp(-80, 85, U), lerp(35, 25, U)), rel(p, F, -60, 0, -5), 40);
  } else if (sh === 'final') {
    st = lerp(935, 1015, U); const p = poseJet(st), F = jetF(st);
    const c = rel(p, F, lerp(90, 52, U), lerp(-45, -30, U), lerp(14, 6, U)); c.y = Math.max(c.y, 4); look(c, rel(p, F, -55, 0, -2), 40);
    place('L_phl', THR.clone().setY(8), seg(U, .05, .1) * (1 - seg(U, .45, .5)));
  } else if (sh === 'land') {
    st = lerp(1012, 1070, U); const p = poseJet(st), F = jetF(1012);
    const k = seg(U, 0, 1); const c = rel(TD.clone().add(F.f.clone().multiplyScalar(-380)), F, lerp(-20, 30, k), lerp(-26, -22, k), 7);
    look(c, TD.clone().add(F.f.clone().multiplyScalar(lerp(-200, 120, U))).setY(4), 40); place('L_td', V(0, 18, 0).add(F.f.clone().multiplyScalar(-380)), seg(st, 1017, 1019));
  } else if (sh === 'replay') {
    st = lerp(-30, 1018, U); const p = poseJet(st), F = jetF(st); pathMat.opacity = .12;
    const w = seg(st, 900, 1018); look(rel(p, F, lerp(420, 90, w), lerp(-300, -45, w), lerp(220, 10, w)), rel(p, F, -150, 0, -10), 40);
    if (st > TS - 2 && st < TS + 5) place('L_fbo', FBO.clone().add(V(0, 15, 0)));
  } else if (sh === 'orbit') {
    st = END; poseJet(st); showHud = false; const a = lerp(-0.4, 1.4, U), R = lerp(120, 85, U);
    look(jet.position.clone().add(V(Math.sin(a) * R, lerp(30, 20, U), Math.cos(a) * R)), jet.position.clone(), 38);
  }
  debAt(st);
  const jp = jet.position; sun.position.copy(jp).add(SUNDIR.clone().multiplyScalar(1500)); sun.target.position.copy(jp); sun.target.updateMatrixWorld();
  hud(st, showHud);
  renderer.render(scene, cam);
}
window.THREE = THREE; window.renderAt = renderAt; window.SCN = scene; window.JET = jet; window.REN = renderer; window.CAM = cam; window.look = look; window.posAt = posAt; window.poseJet = poseJet; window.attitude = attitude; window.altFt = altFt;
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
