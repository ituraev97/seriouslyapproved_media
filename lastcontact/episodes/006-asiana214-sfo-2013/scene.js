import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
const TM = await (await fetch('timing.json')).json();
const GEO = await (await fetch('geo.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const sm = x => x * x * (3 - 2 * x);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const FT = 0.3048, KT = 0.514444, TAN3 = Math.tan(3 * Math.PI / 180);
function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
function segStart(L) { let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--; return i === 0 ? 0 : TM[i].start; }
function segEnd(L) { let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++; return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2; }

// ---------- renderer
const QS = new URLSearchParams(location.search);
const PR = +(QS.get('pr') || window.PR || 0.7);
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(PR); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 1, 60000);
const scene = new THREE.Scene();
const hdr = await new RGBELoader().loadAsync('sky.hdr'); hdr.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = hdr; scene.environmentIntensity = 0.9; scene.background = hdr; scene.backgroundIntensity = 0.9; scene.backgroundBlurriness = 0.05;
scene.fog = new THREE.Fog(0xb9c7d6, 9000, 30000);
scene.add(new THREE.HemisphereLight(0xdfe8ff, 0x606050, 0.6));
const sun = new THREE.DirectionalLight(0xfff3e0, 2.4); sun.position.set(-3000, 5000, 3000); scene.add(sun, sun.target);

// ---------- ground (USGS imagery)
const tl = new THREE.TextureLoader();
async function groundPlane(file, g, y, offs) {
  const tx = await tl.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const m = new THREE.Mesh(new THREE.PlaneGeometry(g[2], g[2]), new THREE.MeshLambertMaterial({ map: tx, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs }));
  m.rotation.x = -Math.PI / 2; m.position.set(g[0], y, g[1]); scene.add(m); return m;
}
await groundPlane('sfo_wide.jpg', GEO.wide, -1.5, 2);
await groundPlane('sfo.jpg', GEO.near, 0, -2);

// ---------- geometry (x east, z south, meters). Landing direction: from the 28L end toward the 10R end.
const e28 = V(GEO.e28[0], 0, GEO.e28[1]), e10 = V(GEO.e10[0], 0, GEO.e10[1]);
const dir = e10.clone().sub(e28).normalize();
const right = V(-dir.z, 0, dir.x);
const SEA = e28.clone().add(dir.clone().multiplyScalar(-(window.SEAOFF || 120)));   // seawall on the shoreline (approx., from imagery)
const at = (s, lat = 0) => SEA.clone().add(dir.clone().multiplyScalar(s)).add(right.clone().multiplyScalar(lat)); // s meters past seawall
const THR = at(600 * FT);                     // 600-ft RSA between seawall and displaced threshold (NTSB 1.10)
const REST = at(2400 * FT, -95);              // came to rest off the left side, ~2,400 ft from the seawall (NTSB 1.1)
const hdg = d => Math.atan2(d.x, d.z);

function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
const glowT = canvasTex(64, 64, g => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.25, 'rgba(255,255,255,.5)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
const mk = (c, o = 0) => new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: o, depthWrite: false, depthTest: false, fog: false });
function flat(w, l, cen, mat, ro = 2) { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, l), mat); m.rotation.set(-Math.PI / 2, 0, hdg(dir) + Math.PI); m.position.copy(cen).setY(.8); m.renderOrder = ro; scene.add(m); return m; }
const seaMat = mk(0xFF2E2E), thrMat = mk(0x3CFF8F), restMat = mk(0xFFB020);
flat(140, 6, SEA, seaMat, 3); flat(70, 4, THR, thrMat, 3); flat(50, 50, REST, restMat, 3);

// ---------- simulation: t = seconds relative to seawall impact (11:27:50.3 PDT). NTSB AAR-14/01 sec 1.1 + table 1.
// [t, airspeed kt, height ft (msl before -55.3, radio altitude after), pitch deg (approx., from sec 1.1 text)]
const K = [[-120, 174, 2140, 1], [-115.3, 174, 2085, 1], [-104.3, 175, 1900, 1], [-81.5, 169, 1500, 1.5], [-72.3, 165, 1300, 0.5], [-55.3, 150.5, 1000, 0], [-51.7, 146.7, 917, 0], [-45.2, 146.0, 723, 0.5],
  [-39.5, 141.3, 581, 1], [-35.4, 136.7, 500, 1.5], [-30.5, 134.0, 404, 2], [-27.0, 130.5, 344, 2], [-26.2, 129.7, 331, 2], [-21.2, 126, 270, 4], [-19.3, 121.9, 219, 4],
  [-15.5, 119.2, 165, 6.5], [-11.0, 113.9, 124, 7.5], [-8.7, 111.8, 102, 8.5], [-7.1, 109.1, 86, 9], [-3.9, 103.6, 46, 11], [-3.4, 103, 39, 12], [-1.7, 104.7, 21, 11.5], [0, 105.5, 5, 11]];
function kv(t, j) { if (t <= K[0][0]) return K[0][j]; for (let i = 1; i < K.length; i++) if (t <= K[i][0]) { const a = K[i - 1], b = K[i]; return lerp(a[j], b[j], (t - a[0]) / (b[0] - a[0])); } return K[K.length - 1][j]; }
const DT = 0.05, DS = []; { let d = 0; for (let t = 0; t >= -121; t -= DT) { DS.push(d); d += (kv(t, 1) - 1.9) * KT * DT; } } // ground speed ≈ IAS − 1.9 kt headwind
const distBefore = t => { const i = clamp(-t / DT, 0, DS.length - 1), i0 = Math.floor(i); return lerp(DS[i0], DS[Math.min(i0 + 1, DS.length - 1)], i - i0); };
const posAt = t => { const p = at(-distBefore(Math.min(t, 0))); p.y = kv(t, 2) * FT + 4.5; return p; };
// desired 3° glidepath, anchored so the airplane is 243 ft above it at 1,000 ft RA (NTSB sec 1.1)
const p1000 = posAt(-55.3), dG = (1000 - 243) * FT / TAN3;
const G = p1000.clone().setY(0).add(dir.clone().multiplyScalar(dG));
const back = p => p.clone().setY(0).sub(G).dot(dir.clone().negate());   // horizontal distance before G
const gpPt = d => G.clone().add(dir.clone().multiplyScalar(-d)).setY(d * TAN3);
const gpA = gpPt(0).setY(1), gpB = gpPt(12000), gpLen = gpA.distanceTo(gpB);
const gpLine = new THREE.Mesh(new THREE.CylinderGeometry(2.2, 2.2, gpLen, 8, 1, true), new THREE.MeshBasicMaterial({ color: 0x3CFF8F, transparent: true, opacity: 0, depthWrite: false, fog: false }));
gpLine.position.copy(gpA).lerp(gpB, .5); gpLine.quaternion.setFromUnitVectors(V(0, 1, 0), gpB.clone().sub(gpA).normalize()); gpLine.renderOrder = 5; scene.add(gpLine);
// PAPI (position illustrative): left of the runway near the glidepath origin
const PAPI = [0, 1, 2, 3].map(k => { const sp = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowT, color: 0xffffff, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, fog: false })); sp.position.copy(G).add(right.clone().multiplyScalar(-45 - k * 9)).setY(1.5); sp.scale.setScalar(16); scene.add(sp); return sp; });
const PAPIK = [[-999, 'WWWW'], [-35.4, 'WWWR'], [-30.5, 'WWRR'], [-26.2, 'WRRR'], [-19.3, 'RRRR']];
const papiAt = t => { let s = 'WWWW'; for (const [a, x] of PAPIK) if (t >= a) s = x; return s; };
const ATK = [[-999, 'SPD'], [-84.6, 'THR'], [-77.3, 'HOLD'], [-5.6, 'THR']];
const atAt = t => { let s = ''; for (const [a, x] of ATK) if (t >= a) s = x; return s; };

// ---------- airplane (Boeing 777 model, clean livery, scaled to 777-200ER length 63.7 m)
const g = await new GLTFLoader().loadAsync('b777.glb'); const o = g.scene;
const white = new THREE.MeshStandardMaterial({ color: 0xeceef0, roughness: .35, metalness: .1 });
const dark = new THREE.MeshStandardMaterial({ color: 0x1b1f25, roughness: .45, metalness: .3 });
const glass = new THREE.MeshStandardMaterial({ color: 0x0f1822, roughness: .08, metalness: .7 });
const grey = new THREE.MeshStandardMaterial({ color: 0x9aa1a8, roughness: .4, metalness: .5 });
o.traverse(m => { if (!m.isMesh) return; m.userData.mat = m.material.name; const n = (m.material.name || '').toLowerCase();
  m.material = n.includes('glass') ? glass : false ? dark : n.includes('silver') ? grey : white; });
const inner = new THREE.Group(); inner.add(o);
let b = new THREE.Box3().setFromObject(inner); const sz = b.getSize(V(0, 0, 0));
if ((window.LONGAXIS || (sz.x > sz.z ? 'x' : 'z')) === 'x') o.rotation.y = Math.PI / 2;
o.rotation.y += +(window.YAW ?? QS.get('yaw') ?? 180) * Math.PI / 180;
inner.updateMatrixWorld(true); b = new THREE.Box3().setFromObject(inner); const sc = 63.7 / (b.max.z - b.min.z); inner.scale.setScalar(sc); inner.updateMatrixWorld(true);
b = new THREE.Box3().setFromObject(inner); inner.position.set(-(b.min.x + b.max.x) / 2, -b.min.y - 4.5, -(b.min.z + b.max.z) / 2);
const pitchG = new THREE.Group(); pitchG.add(inner);
const jet = new THREE.Group(); jet.add(pitchG); scene.add(jet);
window.BOX = [sz.x, sz.y, sz.z];
const HIDE = (window.HIDE || 'Translucent_Glass_Gray_x').split(',');
o.traverse(m => { if (m.isMesh && HIDE.includes(m.name)) m.visible = false; });
window.MESHES = []; o.traverse(m => { if (!m.isMesh) return; const bb = new THREE.Box3().setFromObject(m); const s3 = bb.getSize(V(0,0,0)); window.MESHES.push([m.name, m.userData.mat, s3.x.toFixed(1), s3.y.toFixed(1), s3.z.toFixed(1), bb.min.x.toFixed(1), bb.min.z.toFixed(1)]); });
function poseJet(t) {
  const p = posAt(t); jet.position.copy(p);
  const a = posAt(Math.min(t, -0.6)), c = posAt(Math.min(t, -0.6) + 0.5); const d = c.clone().sub(a); d.y = 0;
  jet.rotation.set(0, hdg(d.lengthSq() > 1e-4 ? d : dir), 0); pitchG.rotation.set(-kv(t, 3) * Math.PI / 180, 0, 0);
  jet.visible = true; return p;
}

// ---------- HUD + events
const EV = [[-999, ''], [-115.3, '11:25:55 · 5 NM · ≈400 FT ABOVE 3° PATH · 174 KT'], [-104.3, '11:26:06 · FLAPS 20'],
  [-84.6, '11:26:25.7 · FLCH SPD · A/T → THR · AUTOFLIGHT STARTS A CLIMB'], [-81.5, '11:26:28.8 · AUTOPILOT DISCONNECTED · FLAPS 30'],
  [-77.3, '11:26:33 · THRUST LEVERS AT IDLE · A/T → HOLD'], [-70, ''], [-55.3, '1,000 FT RA · PAPI ○○○○ · ≈151 KT · ≈1,500 FT/MIN'],
  [-51.7, 'OBSERVER: “SINK RATE SIR”'], [-48, ''], [-45.2, 'OBSERVER: “SINK RATE SIR”'], [-41, ''], [-35.4, '500 FT · 137 KT · THRUST LEVERS IDLE · ≈1,200 FT/MIN'],
  [-30.5, 'PM: “ON GLIDE PATH SIR” · ○○●●'], [-27.0, 'AIRSPEED BELOW VREF (132 KT)'], [-19.3, 'PAPI ●●●● · 219 FT · 122 KT'], [-16.7, 'PM: “IT’S LOW”'],
  [-11.0, 'QUADRUPLE CHIME · 114 KT'], [-7.5, 'PM: “SPEED”'], [-7.1, 'THRUST LEVERS ADVANCED'], [-3.9, 'STICK SHAKER · LOWEST ≈103 KT'], [-2.5, 'PM: “GO AROUND”'], [-0.9, 'SEAWALL IMPACT · 11:27:50']];
const T0 = 11 * 3600 + 27 * 60 + 50.3;
const clock = t => { const x = T0 + t, h = Math.floor(x / 3600), m = Math.floor(x % 3600 / 60), s = x % 60; return `${h}:${String(m).padStart(2, '0')}:${s.toFixed(1).padStart(4, '0')}`; };
function hud(t, show) {
  $('hud').style.opacity = show ? 1 : 0; $('ev').style.opacity = 0; if (!show) return;
  $('hias').textContent = Math.round(kv(t, 1)) + ' KT';
  $('hra').textContent = t < -55.3 ? '≈' + (Math.round(kv(t, 2) / 10) * 10).toLocaleString('en-US') + ' FT MSL' : Math.round(kv(t, 2)).toLocaleString('en-US') + ' FT';
  const ps = papiAt(t); [...$('hpapi').children].forEach((el, i) => el.className = ps[i] === 'W' ? 'w' : 'r');
  const am = atAt(t); $('hat').textContent = am; $('hat').style.color = am === 'HOLD' ? '#FF2E2E' : '';
  $('ht').textContent = clock(t) + ' · ' + (t < 0 ? '−' : '') + Math.abs(t).toFixed(1) + ' S';
  let e = ''; for (const [a, x] of EV) if (t >= a) e = x; if (e) { $('ev').textContent = e; $('ev').style.opacity = 1; }
}
function papiShow(t, on) { const ps = papiAt(t); PAPI.forEach((sp, i) => { sp.visible = on; sp.material.color.set(ps[i] === 'W' ? 0xffffff : 0xff2020); }); }
function place(id, w3, show = 1) { const el = $(id), v = w3.clone().project(cam); el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080) + 'px'; el.style.opacity = (v.z < 1 && Math.abs(v.x) < 1.0 && Math.abs(v.y) < 1.0 && show) ? show : 0; }
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }
const rel = (p, bk, side, up) => p.clone().add(dir.clone().multiplyScalar(-bk)).add(right.clone().multiplyScalar(side)).add(V(0, up, 0));
const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_rwy', 'L_sea', 'L_thr', 'L_rest', 'L_jet', 'L_path', 'L_papi', 'L_bay'];

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
  seaMat.opacity = .85; thrMat.opacity = .8; restMat.opacity = 0; gpLine.material.opacity = 0;
  let st = -120, showHud = false, papiOn = false; const sh = vis[1];
  if (sh === 'open') {
    st = lerp(-62, -20, U); const p = poseJet(st);
    look(rel(p, lerp(170, 120, U), lerp(-90, -60, U), lerp(35, 22, U)), rel(p, -140, 0, -12), 38);
    place('L_jet', p.clone().add(V(0, 18, 0)), seg(U, 0, .04) * (1 - seg(U, .3, .35)));
    place('L_rwy', at(900).setY(3), seg(U, .45, .5)); papiOn = true;
  } else if (sh === 'open_low') {
    st = lerp(-17, -0.6, sm(U)); const p = poseJet(st); showHud = true; papiOn = true;
    look(rel(p, 95, 55, 6), rel(p, -60, 0, 0), 36); place('L_sea', SEA.clone().setY(3), seg(st, -8, -7));
  } else if (sh === 'top') {
    jet.visible = false;
    look(at(-600).add(right.clone().multiplyScalar(lerp(-1700, -1450, U))).setY(lerp(3000, 2650, U)), at(700), 40);
    place('L_rwy', at(1800).setY(3)); place('L_sea', SEA.clone().setY(3), seg(U, .1, .15)); place('L_thr', THR.clone().setY(3), seg(U, .2, .25)); place('L_bay', at(-1200, 600).setY(3));
  } else if (sh === 'far') {
    st = lerp(-116, -76, U); const p = poseJet(st); showHud = true; gpLine.material.opacity = .75 * fadeIn;
    look(rel(p, lerp(200, 150, U), 210, 35), rel(p, -120, 0, -20), 40);
    place('L_path', gpPt(back(p) - 600), seg(U, .05, .1)); place('L_jet', p.clone().add(V(0, 22, 0)), 1 - seg(U, .25, .3));
  } else if (sh === 'profile') {
    st = lerp(-56, -28, U); const p = poseJet(st); showHud = true; gpLine.material.opacity = .75; papiOn = true;
    look(rel(p, 40, 250, 0), rel(p, -60, 0, -12), 38);
    place('L_path', gpPt(back(p) - 300), 1);
  } else if (sh === 'papi') {
    st = lerp(-32, -18, U); const p = poseJet(st); showHud = true; papiOn = true;
    look(rel(p, 80, -16, 15), G.clone().setY(0), 34); place('L_papi', PAPI[1].position.clone().setY(10), seg(U, 0, .05) * (1 - seg(U, .4, .45)));
  } else if (sh === 'final') {
    st = lerp(-12, -0.6, sm(U)); const p = poseJet(st); showHud = true; papiOn = true;
    look(at(-140, 170).setY(16), p.clone().lerp(SEA, .2), 42);
    place('L_sea', SEA.clone().setY(3), seg(U, .1, .15));
  } else if (sh === 'rest') {
    jet.visible = false; restMat.opacity = .85; const c = at(420);
    look(at(lerp(-650, -500, U), lerp(-900, -750, U)).setY(lerp(650, 560, U)), c, 40);
    place('L_sea', SEA.clone().setY(3)); place('L_thr', THR.clone().setY(3), seg(U, .05, .1)); place('L_rest', REST.clone().setY(4), seg(U, .3, .35));
  } else if (sh === 'replay') {
    st = lerp(-56, -0.6, U); const p = poseJet(st); showHud = true; papiOn = true; gpLine.material.opacity = 0;
    const w = seg(st, -22, -1); look(rel(p, lerp(150, 95, w), lerp(-80, 55, w), lerp(28, 7, w)), rel(p, -120, 0, -5), 38);
    if (st > -8) place('L_sea', SEA.clone().setY(3));
  } else if (sh === 'orbit') {
    jet.visible = false; restMat.opacity = .6; const a = lerp(0, 1.2, U); const c = at(350);
    const off = dir.clone().multiplyScalar(-Math.cos(a) * 1500).add(right.clone().multiplyScalar(-Math.sin(a) * 1500));
    look(c.clone().add(off).setY(lerp(520, 640, U)), c, 40);
    place('L_sea', SEA.clone().setY(3)); place('L_rest', REST.clone().setY(4));
  }
  hud(st, showHud); papiShow(st, papiOn);
  renderer.render(scene, cam);
}
window.THREE = THREE; window.renderAt = renderAt; window.SCN = scene; window.JET = jet; window.REN = renderer; window.CAM = cam; window.look = look; window.posAt = posAt; window.poseJet = poseJet;
window.DUR = TM[TM.length - 1].end + 2;
window.DBG = () => { const v = jet.position.clone().project(cam); return [v.x, v.y, v.z, jet.visible]; };
window.READY = true;
