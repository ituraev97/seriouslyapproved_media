import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
const TM = await (await fetch('timing.json')).json();
const GEO = await (await fetch('geo.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const sm = x => x * x * (3 - 2 * x);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const FT = 0.3048, KT = 0.514444;
function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
function segStart(L) { let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--; return i === 0 ? 0 : TM[i].start; }
function segEnd(L) { let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++; return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2; }

// ---------- renderer
const PR = +(new URLSearchParams(location.search).get('pr') || window.PR || 0.7);
const QS = new URLSearchParams(location.search); const AA = (QS.get('aa') ?? window.AA ?? '1') === '1', SH = +(QS.get('sh') ?? window.SH ?? 2048);
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: AA, preserveDrawingBuffer: true });
renderer.setPixelRatio(PR); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
renderer.shadowMap.enabled = false; renderer.shadowMap.type = SH >= 2048 ? THREE.PCFSoftShadowMap : THREE.PCFShadowMap;
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 0.5, 30000);
const scene = new THREE.Scene();
const hdr = await new RGBELoader().loadAsync('night.hdr'); hdr.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = hdr; scene.environmentIntensity = 0.55;
scene.background = hdr; scene.backgroundIntensity = 0.22; scene.backgroundBlurriness = +(QS.get('bb') ?? window.BB ?? 0.1);
scene.fog = new THREE.Fog(0x141b26, 2500, 9000);
scene.add(new THREE.HemisphereLight(0x8fa6c8, 0x202018, 0.9));
const moon = new THREE.DirectionalLight(0xbcd0ff, 0.9); moon.position.set(-2000, 3000, 1500); scene.add(moon);
const flood = new THREE.DirectionalLight(0xffe6c4, 2.6); flood.castShadow = true; flood.shadow.mapSize.set(Math.max(SH, 256), Math.max(SH, 256));
Object.assign(flood.shadow.camera, { left: -30, right: 30, top: 30, bottom: -30, near: 1, far: 400 }); flood.shadow.bias = -0.0005;
scene.add(flood, flood.target);

// ---------- ground (USGS imagery), darkened for night
const tl = new THREE.TextureLoader();
async function groundPlane(file, size, y, offs, col) {
  const tx = await tl.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const GM = QS.get('gm') ?? window.GM ?? 'std'; const mo = { map: tx, color: col, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs };
  const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), GM === 'lam' ? new THREE.MeshLambertMaterial(mo) : new THREE.MeshStandardMaterial({ ...mo, roughness: 1 }));
  m.rotation.x = -Math.PI / 2; m.position.y = y; m.receiveShadow = true; scene.add(m); return m;
}
await groundPlane('cae_wide.jpg', GEO.ground_wide, -0.8, 2, 0x8a8f9a);
await groundPlane('cae.jpg', GEO.ground, 0, -2, 0xa8adb8);

// ---------- runway geometry (x east, z south). Runway 11 start at e11, toward e29
const RWY = 8601;
const e11 = V(GEO.e11[0], 0, GEO.e11[1]), e29 = V(GEO.e29[0], 0, GEO.e29[1]);
const dir = e29.clone().sub(e11).normalize();
const right = V(-dir.z, 0, dir.x);           // right of direction of travel
const at = (sft, lat = 0) => e11.clone().add(dir.clone().multiplyScalar(sft * FT)).add(right.clone().multiplyScalar(lat));
const hdg = d => Math.atan2(d.x, d.z);
const REST = at(RWY + 1870, 4);

// runway lights (edge white, threshold green, end red) as glows
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; }
const glowT = canvasTex(64, 64, g => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.25, 'rgba(255,255,255,.4)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
function glows(color, pts, s) { const geo = new THREE.BufferGeometry().setFromPoints(pts); const m = new THREE.PointsMaterial({ color, size: s, map: glowT, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true, fog: false }); const p = new THREE.Points(geo, m); scene.add(p); return p; }
const edge = [], grn = [], red = [], cl = [];
for (let s = 0; s <= RWY; s += 200) for (const k of [-1, 1]) edge.push(at(s, k * 24).setY(.6));
for (let k = -22; k <= 22; k += 3) { grn.push(at(-3, k).setY(.6)); red.push(at(RWY + 3, k).setY(.6)); }
for (let s = 50; s <= RWY; s += 50) cl.push(at(s, 0).setY(.3));
glows(0xfff1d6, edge, 9); glows(0x52ff8a, grn, 10); glows(0xff3b3b, red, 10); glows(0xdfe8ff, cl, 3.2);
// overlays: highlight strip + distance ticks + safety area box
const mk = (c, o = 0) => new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: o, depthWrite: false, depthTest: false });
const stripMat = mk(0x3CFF8F), tickMat = mk(0xEEF2F4), rsaMat = mk(0xFFB020), redMat = mk(0xFF2E2E);
function flat(w, l, cen, mat, ro = 2) { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, l), mat); m.rotation.set(-Math.PI / 2, 0, hdg(dir) + Math.PI); m.position.copy(cen).setY(.8); m.renderOrder = ro; scene.add(m); return m; }
flat(46, RWY * FT, at(RWY / 2), stripMat);
for (let s = 1000; s < RWY; s += 1000) flat(46, 2, at(s), tickMat);
flat(500 * FT, 1000 * FT, at(RWY + 500), rsaMat, 1);
flat(70, 4, at(6100), redMat, 3); const amberBar = flat(70, 4, at(2500), mk(0xFFB020));

// ---------- airplane (Learjet 55 model, clean livery, scaled to Learjet 60 length 17.88 m)
const g = await new GLTFLoader().loadAsync('lj55.glb'); const o = g.scene;
const white = new THREE.MeshStandardMaterial({ color: 0xeceef0, roughness: .36, metalness: .12 });
const black = new THREE.MeshStandardMaterial({ color: 0x1a1d22, roughness: .5, metalness: .2 });
const glass = new THREE.MeshStandardMaterial({ color: 0x0f1822, roughness: .08, metalness: .7 });
o.traverse(m => { if (!m.isMesh) return; m.castShadow = false; m.receiveShadow = false; const n = (m.material.name || '').toLowerCase(); m.material = n.includes('black') ? black : n.includes('window') ? glass : white; });
const inner = new THREE.Group(); inner.add(o);
let b = new THREE.Box3().setFromObject(inner); const sc = 17.88 / (b.max.z - b.min.z); inner.scale.setScalar(sc); inner.updateMatrixWorld(true);
b = new THREE.Box3().setFromObject(inner); inner.position.set(-(b.min.x + b.max.x) / 2, -b.min.y, -(b.min.z + b.max.z) / 2);
const jet = new THREE.Group(); jet.add(inner); scene.add(jet);
const blobT = canvasTex(128, 128, g => { const gr = g.createRadialGradient(64, 64, 0, 64, 64, 64); gr.addColorStop(0, 'rgba(0,0,0,.75)'); gr.addColorStop(.6, 'rgba(0,0,0,.35)'); gr.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = gr; g.fillRect(0, 0, 128, 128); });
const blob = new THREE.Mesh(new THREE.PlaneGeometry(15, 19), new THREE.MeshBasicMaterial({ map: blobT, transparent: true, depthWrite: false, polygonOffset: true, polygonOffsetFactor: -4, polygonOffsetUnits: -4 }));
blob.rotation.x = -Math.PI / 2; blob.position.y = 0.06; jet.add(blob);
// nav/landing lights on the jet
const jl = new THREE.Group(); jet.add(jl);
const pt = (c, x, y, z, s) => { const p = glows(c, [V(x, y, z)], s); scene.remove(p); jl.add(p); };
pt(0xff3030, -6.7, 1.9, 0.5, 2.2); pt(0x30ff60, 6.7, 1.9, 0.5, 2.2); pt(0xffffff, 0, 1.2, 8.5, 4);
const land = new THREE.SpotLight(0xfff4dd, 600, 400, 0.35, 0.6, 1.6); land.position.set(0, 1.5, 8); jet.add(land); land.target.position.set(0, 0, 80); jet.add(land.target);
// sparks/debris from the right main gear
const SP = 160, spGeo = new THREE.BufferGeometry(); spGeo.setAttribute('position', new THREE.Float32BufferAttribute(new Float32Array(SP * 3), 3));
const sparks = new THREE.Points(spGeo, new THREE.PointsMaterial({ color: 0xffa040, size: 0.7, map: glowT, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending }));
scene.add(sparks); sparks.visible = false;

// ---------- simulation (t = seconds after 23:55:00 EDT); ground speeds from NTSB fig. 5/6 + sec. 1.1/2.2
const GK = [[-11, 0], [0, 72], [10.5, 131], [12, 137], [12.4, 139], [12.8, 141], [13, 142], [13.7, 144], [14, 144], [14.6, 143], [15.1, 142], [17, 141], [18.4, 133], [19.5, 130], [20.3, 128], [21.6, 126], [24.5, 123], [28.7, 125], [32, 124], [39, 114], [46, 103], [48, 70], [50, 0]];
function gs(t) { if (t <= GK[0][0]) return 0; for (let i = 1; i < GK.length; i++) if (t <= GK[i][0]) { const [a, va] = GK[i - 1], [c, vc] = GK[i]; return lerp(va, vc, (t - a) / (c - a)); } return 0; }
const DT = 0.02, S = []; { let s = 0; for (let t = -11; t <= 50; t += DT) { S.push(s); s += gs(t) * KT * DT / FT; } }
const sRaw = t => { const i = clamp((t + 11) / DT, 0, S.length - 1); const i0 = Math.floor(i); return lerp(S[i0], S[Math.min(i0 + 1, S.length - 1)], i - i0); };
// normalize: rumbling point (t=12) at 2,500 ft past start, forward-thrust point (t=27.3) at 6,100 ft
const k1 = 2500 / sRaw(12), sA = sRaw(12), sB = sRaw(24.5), k2 = (6100 - 2500) / (sB - sA);
function sOf(t) { const r = sRaw(t); if (t <= 12) return r * k1; return 2500 + (r - sA) * k2; }
function latOf(t) { if (t < 12) return -2.5; if (t < 13.6) return lerp(-2.5, 6.5, sm(seg(t, 12, 13.6))); if (t < 18) return lerp(6.5, 2, sm(seg(t, 13.6, 18))); return 2; }
const HIDE_FT = RWY + 1000 + 120;
function poseJet(t) {
  const s = sOf(t), p = at(s, latOf(t)), q = at(sOf(t + 0.3) + 0.5, latOf(t + 0.3));
  jet.position.copy(p); const d = q.clone().sub(p); jet.rotation.set(0, hdg(d.lengthSq() > 1e-4 ? d : dir), 0);
  jet.visible = s < HIDE_FT; return s;
}
const EV = [[-99, ''], [0, '“EIGHTY KNOTS. CROSSCHECK”'], [10.5, '“V-ONE” · V1 ≈136 KIAS'], [12, 'LOUD RUMBLING · RIGHT OUTBOARD TIRE · ≈138 KT'], [12.4, 'FO: “GO” … “GO GO GO”'],
  [14, 'CAPT: “GO?” · PEAK ≈144 KT'], [17, '“WE’RE NOT GOIN’ THOUGH”'], [19.5, '“FULL OUT” · REVERSERS + BRAKES'], [21.6, 'NOSEWHEEL STEERING DISCONNECT TONE · AIR MODE → REVERSERS STOW'],
  [24.5, 'FORWARD THRUST · ≈123 KT · ≈2,500 FT FROM END (TIME ESTIMATED)'], [28.7, 'FO: “SHUT ’EM OFF” · N1 ≈9,165 RPM'], [32.4, '“THEY’RE SHUT OFF”'], [36, 'RADIO: “ROLL THE EQUIPMENT WE’RE GOIN’ OFF THE END”'], [41.1, 'CVR RECORDING ENDS']];
function hud(t, show) {
  $('hud').style.opacity = show ? 1 : 0; $('ev').style.opacity = 0; if (!show) return;
  const s = sOf(t); $('hgs').textContent = t > 46.5 ? '—' : Math.round(gs(t)) + ' KT';
  $('hr').textContent = s < RWY ? (Math.round((RWY - s) / 50) * 50).toLocaleString('en-US') + ' FT' : 'NONE';
  $('ht').textContent = (t < 0 ? '−' : '+') + Math.abs(t).toFixed(1) + ' S';
  let e = ''; for (const [a, x] of EV) if (t >= a) e = x; if (e) { $('ev').textContent = e; $('ev').style.opacity = 1; }
}
function place(id, w3, show = 1) { const el = $(id), v = w3.clone().project(cam); el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080) + 'px'; el.style.opacity = (v.z < 1 && Math.abs(v.x) < 1.1 && Math.abs(v.y) < 1.1 && show) ? show : 0; }
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }
const rel = (p, back, side, up) => p.clone().add(dir.clone().multiplyScalar(-back)).add(right.clone().multiplyScalar(side)).add(V(0, up, 0));
function updSparks(t) {
  const on = t > 11.9 && t < 24; sparks.visible = on; if (!on) return;
  const a = spGeo.attributes.position.array; const g0 = jet.localToWorld(V(2.1, 0.3, -0.5));
  for (let i = 0; i < SP; i++) { const ph = ((i * 0.6180339) % 1); const age = ((t * 3 + ph) % 1); const r = (i * 7.31) % 1;
    const p = g0.clone().add(dir.clone().multiplyScalar(-age * 14)).add(right.clone().multiplyScalar((r - .5) * 3 * age)).add(V(0, Math.max(0, Math.sin(age * 3.1) * 1.2 * r), 0));
    a[i * 3] = p.x; a[i * 3 + 1] = p.y; a[i * 3 + 2] = p.z; }
  spGeo.attributes.position.needsUpdate = true;
}
const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_rwy', 'L_start', 'L_tire', 'L_fwd', 'L_end', 'L_rsa', 'L_road', 'L_rest', 'L_jet'];

function renderAt(t) {
  const L = lineAt(t), vis = L.vis, s0 = segStart(L), s1 = segEnd(L), U = seg(t, s0, s1), u = t - s0;
  CARDS.forEach(c => c.style.opacity = 0); LBLS.forEach(id => $(id).style.opacity = 0);
  ['recon', 'cred', 'hud', 'ev'].forEach(id => $(id).style.opacity = 0);
  const fadeIn = clamp(u / 0.35), fadeOut = clamp((s1 - t) / 0.35);
  if (vis[0] === 'card') {
    const c = $('c_' + vis[1]); c.style.opacity = Math.min(fadeIn, fadeOut);
    c.querySelectorAll('[data-from]').forEach(el => { const d = T[el.dataset.from]; el.style.opacity = d ? clamp((t - d.start) / 0.4) : 1; });
    if (vis[1] === 'status') $('sweep').setAttribute('transform', `rotate(${(t * 60) % 360})`);
    if (vis[1] === 'spectrum') {
      const x = 80 + (u * 140) % 1400; $('wheel').setAttribute('cx', x);
      let d = 'M0 60'; for (let i = 0; i <= 1560; i += 4) { const f = 0.02 + 0.06 * clamp(u / 12); d += ` L${i} ${60 + 30 * Math.sin(i * f + u * 8) * (i < x ? 1 : 0.15)}`; } $('wave').setAttribute('d', d);
    }
    return;
  }
  $('recon').style.opacity = 1; $('cred').style.opacity = .9;
  stripMat.opacity = 0; tickMat.opacity = .3; rsaMat.opacity = 0; redMat.opacity = 0; amberBar.material.opacity = 0;
  let st = 0, showHud = false; const sh = vis[1];
  if (sh === 'open_roll') {
    st = lerp(-6, 11.6, U); poseJet(st); const p = jet.position.clone();
    const k = U; look(rel(p, lerp(60, 26, k), lerp(-30, -9, k), lerp(14, 4, k)), rel(p, -20, 0, 2), 40);
    place('L_jet', p.clone().add(V(0, 7, 0)), seg(U, 0, .05) * (1 - seg(U, .25, .3)));
  } else if (sh === 'tire') {
    st = lerp(11.6, 14.8, U); poseJet(st); const p = jet.position.clone();
    look(rel(p, 26, 17, 3.2), rel(p, -4, 1, 1.2), 38); showHud = true;
  } else if (sh === 'open_side') {
    st = lerp(26, 36, U); poseJet(st); const p = jet.position.clone();
    look(rel(p, 70, -55, 22), rel(p, -40, 0, 2), 40);
    place('L_end', at(RWY).setY(2));
  } else if (sh === 'top') {
    st = -11; poseJet(-11); jet.visible = false; stripMat.opacity = .35 * fadeIn; rsaMat.opacity = .3;
    const mid = at(RWY * .62);
    look(mid.clone().add(V(0, lerp(1900, 1650, U), 0)).add(right.clone().multiplyScalar(lerp(1100, 1300, U))).add(dir.clone().multiplyScalar(-150)), mid, 40);
    place('L_rwy', at(RWY * .3).setY(2)); place('L_end', at(RWY).setY(2));
  } else if (sh === 'backtaxi') {
    const s = lerp(1500, 60, sm(seg(U, 0, .7))); const turn = sm(seg(U, .7, 1));
    jet.visible = true; jet.position.copy(at(s, lerp(0, 0, turn))); jet.rotation.set(0, hdg(dir) + Math.PI * (1 - turn), 0);
    look(rel(jet.position, -70, -60, 30), jet.position.clone().add(V(0, 2, 0)), 40); place('L_start', at(0).setY(2));
  } else if (sh === 'roll_follow') {
    st = lerp(-1, 12.3, U); showHud = true; poseJet(st); const p = jet.position.clone();
    look(rel(p, 34, -16, 7), rel(p, -25, 0, 2), 40);
    if (st > 11.5) { amberBar.material.opacity = .9; place('L_tire', at(2500).setY(1)); }
  } else if (sh === 'veer') {
    st = lerp(11.8, 18, U); showHud = true; poseJet(st); const p = jet.position.clone(); amberBar.material.opacity = .9;
    look(rel(p, 70, 0, 150), rel(p, -25, 0, 0), 40);
  } else if (sh === 'decel') {
    st = lerp(17, 22.5, U); showHud = true; poseJet(st); const p = jet.position.clone();
    look(rel(p, -30, 16, 4), rel(p, 0, 0, 1.5), 40);
  } else if (sh === 'fwd') {
    st = lerp(21.4, 30, U); showHud = true; poseJet(st); const p = jet.position.clone(); redMat.opacity = .9;
    look(rel(p, 55, 24, 16), rel(p, -60, 0, 0), 40); place('L_fwd', at(6100).setY(1), seg(st, 24, 25));
  } else if (sh === 'overrun_side') {
    st = lerp(28.5, 41.1, U); showHud = true; poseJet(st); const p = jet.position.clone(); rsaMat.opacity = .15;
    look(rel(p, lerp(40, 120, U), 38, lerp(10, 40, U)), rel(p, -50, 0, 1), 40);
    place('L_end', at(RWY).setY(1));
  } else if (sh === 'end_layout') {
    st = lerp(38, 46, seg(U, 0, .5)); poseJet(st); rsaMat.opacity = .35; redMat.opacity = 0;
    const c = at(RWY + 900);
    look(c.clone().add(right.clone().multiplyScalar(lerp(-520, -420, U))).add(dir.clone().multiplyScalar(lerp(-600, -480, U))).add(V(0, lerp(380, 320, U), 0)), c, 40);
    place('L_end', at(RWY).setY(1)); place('L_rsa', at(RWY + 1000).setY(1), seg(U, .1, .15));
    place('L_road', at(RWY + 1800, -60).setY(1), seg(U, .3, .35)); place('L_rest', REST.clone().setY(3), seg(U, .5, .55));
  } else if (sh === 'replay') {
    st = lerp(-1, 46.5, U); showHud = true; const s = poseJet(st); const p = jet.position.clone(); redMat.opacity = .8; amberBar.material.opacity = .8; rsaMat.opacity = .15;
    const w = seg(st, 36, 44); look(rel(p, lerp(45, 260, w), lerp(-22, -200, w), lerp(10, 120, w)), rel(p, -30 * (1 - w), 0, 1), 40);
    if (s > RWY - 1500) place('L_end', at(RWY).setY(1));
  } else if (sh === 'rest_orbit') {
    jet.visible = false; rsaMat.opacity = .3; const a = lerp(-0.9, 0.5, U); const c = at(RWY + 700);
    look(c.clone().add(V(Math.sin(a) * 900, lerp(420, 520, U), Math.cos(a) * 900)), c, 40);
    place('L_end', at(RWY).setY(1)); place('L_rsa', at(RWY + 1000).setY(1)); place('L_rest', REST.clone().setY(3));
  }
  hud(st, showHud); updSparks(st);
  flood.target.position.copy(jet.position); flood.position.copy(jet.position).add(V(-60, 120, 40));
  renderer.render(scene, cam);
}
window.THREE = THREE; window.renderAt = renderAt; window.SCN = scene; window.JET = jet; window.REN = renderer;
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
