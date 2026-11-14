import * as THREE from 'three';
const TM = await (await fetch('timing.json')).json();
const GEO = await (await fetch('geo.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const FT = 0.3048;

// current line at time t
function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
// start time of the segment containing line L (first consecutive line with same visual key)
function segStart(L) {
  const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
  let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--;
  return i === 0 ? 0 : TM[i].start;
}
function segEnd(L) {
  const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
  let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++;
  return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2;
}

// ---------- renderer
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(0.7); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.shadowMap.enabled = true; renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.95;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x8d9aa8); scene.fog = new THREE.Fog(0x8d9aa8, 6000, 16000);
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 5, 40000);
scene.add(new THREE.HemisphereLight(0xdfe6ee, 0x4a4a40, 1.0));
const sun = new THREE.DirectionalLight(0xfff0dc, 1.9); sun.castShadow = true; sun.shadow.mapSize.set(2048, 2048);
Object.assign(sun.shadow.camera, { left: -150, right: 150, top: 150, bottom: -150, near: 10, far: 4000 });
scene.add(sun, sun.target);
const loader = new THREE.TextureLoader();
async function groundPlane(file, size, y, offs) {
  const tx = await loader.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), new THREE.MeshStandardMaterial({ map: tx, roughness: 1, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs }));
  m.rotation.x = -Math.PI / 2; m.position.y = y; m.receiveShadow = true; scene.add(m); return m;
}
await groundPlane('mia_wide.jpg', GEO.ground_wide, -0.6, 2);
await groundPlane('mia.jpg', GEO.ground, 0, -2);

// runway geometry (x east, z south)
const e30 = V(GEO.e30[0], 0, GEO.e30[1]), e12 = V(GEO.e12[0], 0, GEO.e12[1]), REST = V(GEO.rest[0], 0, GEO.rest[1]);
const dir = e12.clone().sub(e30).normalize();                 // landing direction (299 true)
const left = V(dir.z, 0, -dir.x);                              // to the left of landing direction
const THR = e30.clone().add(dir.clone().multiplyScalar(945 * FT));
const END = e12.clone();
const RWYLEN_FT = 8415;
const hdg = v => Math.atan2(-v.x, -v.z);
const at = sft => THR.clone().add(dir.clone().multiplyScalar(sft * FT));

// highlight strip for runway
const stripMat = new THREE.MeshBasicMaterial({ color: 0x3CFF8F, transparent: true, opacity: 0, depthWrite: false, depthTest: false });
const strip = new THREE.Mesh(new THREE.PlaneGeometry(46, e30.distanceTo(e12)), stripMat);
strip.rotation.set(-Math.PI / 2, 0, -Math.atan2(-dir.x, -dir.z) * -1); // align length with dir
strip.rotation.set(-Math.PI / 2, 0, Math.atan2(-dir.x, -dir.z)); strip.position.copy(e30.clone().lerp(e12, .5)).setY(.5); scene.add(strip);
// distance ticks every 1000 ft
const tickMat = new THREE.MeshBasicMaterial({ color: 0xEEF2F4, transparent: true, opacity: 0, depthWrite: false, depthTest: false });
const tdMat = new THREE.MeshBasicMaterial({ color: 0xFFB020, transparent: true, opacity: 0, depthWrite: false, depthTest: false });
function bar(sft, mat, w = 60, d = 4) { const m = new THREE.Mesh(new THREE.PlaneGeometry(w, d), mat); m.rotation.set(-Math.PI / 2, 0, Math.atan2(-dir.x, -dir.z)); m.position.copy(at(sft)).setY(.7); scene.add(m); return m; }
for (let s = 0; s <= 8000; s += 1000) bar(s, tickMat);
bar(3750, tdMat, 70, 8); bar(RWYLEN_FT - 2730, tdMat, 70, 3);

// ---------- 767 model (nose -Z), ~55 m long
const white = new THREE.MeshStandardMaterial({ color: 0xe9eef3, roughness: .45, metalness: .1 });
const grey = new THREE.MeshStandardMaterial({ color: 0x9aa5b5, roughness: .5, metalness: .3 });
const dark = new THREE.MeshStandardMaterial({ color: 0x252a33, roughness: .6 });
const glass = new THREE.MeshStandardMaterial({ color: 0x1b2533, roughness: .1, metalness: .6 });
const box = (w, h, d, m) => new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m);
function make767() {
  const g = new THREE.Group();
  const R = 2.5, L = 42;
  const fus = new THREE.Mesh(new THREE.CylinderGeometry(R, R, L, 28), white); fus.rotation.x = Math.PI / 2; fus.position.set(0, 4.2, 0); g.add(fus);
  const nose = new THREE.Mesh(new THREE.SphereGeometry(R, 28, 18, 0, Math.PI * 2, 0, Math.PI / 2), white); nose.rotation.x = -Math.PI / 2; nose.scale.set(1, 2.4, 1); nose.position.set(0, 4.2, -L / 2); g.add(nose);
  const tail = new THREE.Mesh(new THREE.ConeGeometry(R, 10, 28), white); tail.rotation.x = Math.PI / 2; tail.position.set(0, 4.7, L / 2 + 5); g.add(tail);
  const ws = box(3.2, .3, 1.2, glass); ws.position.set(0, 5.6, -L / 2 - 1.2); g.add(ws);
  const belly = box(4.6, .5, L, grey); belly.position.set(0, 2.0, 0); g.add(belly);
  for (const s of [-1, 1]) {
    const wing = box(21, .55, 6, white); wing.position.set(s * 12.5, 2.6, 2); wing.rotation.y = s * 0.5; wing.rotation.z = s * -0.07; g.add(wing);
    const eng = new THREE.Mesh(new THREE.CylinderGeometry(1.45, 1.2, 5.6, 22), grey); eng.rotation.x = Math.PI / 2; eng.position.set(s * 7.6, 1.8, -3.5); g.add(eng);
    const inl = new THREE.Mesh(new THREE.CircleGeometry(1.4, 22), dark); inl.position.set(s * 7.6, 1.8, -6.32); inl.rotation.y = Math.PI; g.add(inl);
    const hs = box(9, .3, 3.2, white); hs.position.set(s * 4.8, 5.4, L / 2 + 6.5); hs.rotation.y = s * 0.55; g.add(hs);
    const mg = box(.5, 2.0, .5, dark); mg.position.set(s * 4.6, 1.0, 3.5); g.add(mg);
    for (const z of [2.6, 4.4]) { const w = new THREE.Mesh(new THREE.CylinderGeometry(.62, .62, 1.2, 16), dark); w.rotation.z = Math.PI / 2; w.position.set(s * 4.6, .62, z); g.add(w); }
  }
  const vs = box(.5, 10, 7, white); vs.position.set(0, 10, L / 2 + 6); vs.rotation.x = -0.5; g.add(vs);
  const ng = box(.4, 2.2, .4, dark); ng.position.set(0, 1.1, -L / 2 + 3); g.add(ng);
  g.traverse(o => { if (o.isMesh) { o.castShadow = true; } });
  return g;
}
const jet = make767(); scene.add(jet);

// ---------- simulation from NTSB data points (time 0 = threshold)
const SK = [[-60, -17900], [0, 0], [13, 3750], [28, 7485], [32, 8000], [33.3, 8415], [42.5, 9615]];
const GK = [[-60, 177], [0, 177], [13, 160], [20, 146], [24, 134], [28, 120], [32, 117], [33.3, 113], [35, 100], [36, 96], [42.5, 65]];
function interp(K, t) { if (t <= K[0][0]) return K[0][1]; for (let i = 1; i < K.length; i++) if (t <= K[i][0]) { const [a, va] = K[i - 1], [b, vb] = K[i]; return lerp(va, vb, (t - a) / (b - a)); } return K[K.length - 1][1]; }
function sOf(t) { // smooth monotone via Catmull-ish blend of linear segments
  return interp(SK, t);
}
function hOf(t) { if (t <= 0) return 105 + (-sOf(t)) * Math.tan(3 * Math.PI / 180); if (t < 13) return 105 * Math.pow(1 - t / 13, 1.5); return 0; }
function posOf(t) {
  const s = sOf(t);
  let p;
  if (s <= RWYLEN_FT) p = at(s);
  else { const k = clamp((s - RWYLEN_FT) / 1200); const straight = at(s); p = straight.lerp(REST, k * k); }
  p.y = hOf(t) * FT; return p;
}
function poseJet(t) {
  const p = posOf(t), q = posOf(t + 0.25); const d = q.clone().sub(p); d.y = 0;
  jet.position.copy(p);
  const pitch = t < 0 ? 0.02 : (t < 13 ? 0.06 : 0);
  jet.rotation.set(0, 0, 0); jet.rotation.order = 'YXZ'; jet.rotation.y = d.length() > 0.01 ? hdg(d) : hdg(dir); jet.rotation.x = pitch;
  if (t >= 42.5) { jet.position.copy(REST); jet.rotation.y = hdg(REST.clone().sub(END)); jet.rotation.z = 0.05; }
}
const EVENTS = [[-99, ''], [0, 'THRESHOLD · 105 FT · 177 KT'], [13, 'TIRE MARKS BEGIN · ≈160 KT'], [14, 'WEIGHT-ON-WHEELS: AIR ↔ GROUND (≈7 S)'], [20, 'WHEEL BRAKES APPLIED · 146 KT'],
  [28, 'BRAKES RELEASED · GO-AROUND THRUST · 120 KT · 930 FT LEFT'], [32, 'IDLE · BRAKES AGAIN · 117 KT · 415 FT LEFT'], [33.3, 'OFF THE RUNWAY END · 113 KT'],
  [35, 'LOCALIZER + APPROACH LIGHTS · ≈100 KT'], [42.5, 'LAST RECORDED GROUNDSPEED · 65 KT']];
function hud(t, show) {
  $('hud').style.opacity = show ? 1 : 0; $('ev').style.opacity = 0;
  if (!show) return;
  $('hgs').textContent = Math.round(interp(GK, t)) + ' KT';
  const h = hOf(t); $('hh').textContent = h > 0.5 ? Math.round(h) + ' FT' : 'ON GROUND';
  const s = sOf(t); $('hr').textContent = s < 0 ? '8,415 FT' : (s < RWYLEN_FT ? Math.round((RWYLEN_FT - s) / 5) * 5 + ' FT' : 'NONE');
  let e = ''; for (const [a, txt] of EVENTS) if (t >= a) e = txt;
  if (e) { $('ev').textContent = e; $('ev').style.opacity = 1; }
}
function place(id, w3, show = 1) {
  const el = $(id), v = w3.clone().project(cam);
  el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080) + 'px';
  el.style.opacity = (v.z < 1 && show) ? show : 0;
}
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); }

// ---------- CVR list
const CVR = [
  ['06:02', 'Captain calls for flaps 1', 'c2'], ['04:18', 'Checked in with Miami tower · cleared to land runway 30', 'c3'],
  ['02:53', 'Captain calls for flaps 5', 'c4'], ['02:37', 'Landing gear lowered', 'c4'], ['02:14', 'Captain calls for flaps 15', 'c4'],
  ['01:42', 'Captain calls for flaps 20 · first officer cautions they are too fast', 'c5'], ['', 'More comments on excessive speed through the end · no consistent verbal response (NTSB)', 'c6'],
  ['01:23', 'Sounds consistent with autopilot disconnect', 'c7'], ['01:12', '“One thousand” (electronic callout)', 'c8'], ['01:04', '“Sink rate, sink rate”', 'c8'],
  ['00:58', '“Five hundred”', 'c8'], ['00:57', '“Sink rate, sink rate”', 'c8'], ['00:54', '“One hundred”', 'c8'], ['00:50', '“Minimums”', 'c8'],
  ['00:48', '“Too low terrain” × 4', 'c9'], ['00:41', 'Captain calls for flaps 30', 'c10'], ['00:40', '“Forty”', 'c10'], ['00:39', '“Too low terrain”', 'c10'], ['00:36', '“Ten”', 'c10'],
  ['00:31', 'Sounds similar to touchdown', 'c11'], ['00:15', 'Captain calls for a go-around', 'c11'], ['00:10', 'Sounds similar to leaving the paved surface', 'c11'], ['00:00', 'Recording ends', 'c11']];
$('cvrin').innerHTML = CVR.map(([a, b], i) => `<div class="cv" id="cv${i}"><div class="t">${a}</div><div>${b}</div></div>`).join('');
const CVR_ORDER = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11'];

const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_thr', 'L_td', 'L_end', 'L_loc', 'L_road', 'L_rest', 'L_rwy', 'L_jet'];

function renderAt(t) {
  const L = lineAt(t), vis = L.vis, s0 = segStart(L), s1 = segEnd(L), u = t - s0, U = seg(t, s0, s1);
  CARDS.forEach(c => c.style.opacity = 0); LBLS.forEach(id => $(id).style.opacity = 0);
  ['recon', 'cred', 'hud', 'ev'].forEach(id => $(id).style.opacity = 0);
  stripMat.opacity = 0; tickMat.opacity = 0; tdMat.opacity = 0;
  const fadeIn = clamp(u / 0.35), fadeOut = clamp((s1 - t) / 0.35);
  if (vis[0] === 'card') {
    const c = $('c_' + vis[1]); c.style.opacity = Math.min(fadeIn, fadeOut);
    c.querySelectorAll('[data-from]').forEach(el => { const d = T[el.dataset.from]; el.style.opacity = d ? clamp((t - d.start) / 0.4) : 1; });
    if (vis[1] === 'cvr') {
      const cur = CVR_ORDER.indexOf(L.id); let last = -1;
      CVR.forEach(([, , id], i) => { const on = CVR_ORDER.indexOf(id) <= cur; const el = $('cv' + i); el.style.opacity = on ? 1 : 0; el.classList.toggle('on', id === L.id); if (on) last = i; });
      const target = Math.max(0, (last - 9)) * 66; // scroll
      const prev = parseFloat($('cvrin').dataset.y || 0); const y = lerp(prev, target, 0.15);
      $('cvrin').dataset.y = y; $('cvrin').style.top = (-y) + 'px';
    }
    if (vis[1] === 'decel') {
      const k = seg(t, T.d3.start, T.d3.start + 1.5); document.getElementById('spl').setAttribute('transform', `rotate(${-40 * k} 520 40)`);
      document.getElementById('rev').setAttribute('opacity', seg(t, T.d4.start, T.d4.start + .6));
    }
    if (vis[1] === 'status') $('sweep').setAttribute('transform', `rotate(${(t * 60) % 360})`);
    return; // no WebGL
  }
  // ---------- 3D shots
  $('recon').style.opacity = 1; $('cred').style.opacity = .9;
  let st = 42.5, showHud = false;
  const sh = vis[1];
  if (sh === 'approach') {
    st = lerp(-45, -6, U);
    poseJet(st); const p = jet.position.clone();
    look(p.clone().add(dir.clone().multiplyScalar(-130)).add(left.clone().multiplyScalar(-70)).add(V(0, 30, 0)), p.clone().add(dir.clone().multiplyScalar(250)), 42);
    tickMat.opacity = .6; place('L_jet', p.clone().add(V(0, 18, 0)), fadeIn);
  } else if (sh === 'threshold') {
    st = lerp(-4, 15, U); showHud = true; tickMat.opacity = .8; tdMat.opacity = .9;
    poseJet(st); const p = jet.position.clone();
    look(p.clone().add(dir.clone().multiplyScalar(-90)).add(left.clone().multiplyScalar(55)).add(V(0, 26, 0)), p.clone().add(dir.clone().multiplyScalar(60)), 40);
    place('L_thr', at(0).setY(2)); place('L_td', at(3750).setY(2));
  } else if (sh === 'overrun_fast') {
    st = lerp(15, 42.5, ease(U)); tickMat.opacity = .5;
    poseJet(st); const c = at(7600);
    look(c.clone().add(left.clone().multiplyScalar(-700)).add(dir.clone().multiplyScalar(-500)).add(V(0, 520, 0)), c.clone().lerp(REST, .45), 40);
    place('L_end', END.clone().setY(2)); place('L_rest', REST.clone().setY(8), seg(st, 40, 42.5));
  } else if (sh === 'top') {
    st = 42.5; stripMat.opacity = .45 * fadeIn; tickMat.opacity = .6;
    const mid = e30.clone().lerp(e12, .5);
    look(mid.clone().add(V(0, lerp(4200, 3300, U), lerp(300, 900, U))), mid, 40);
    place('L_rwy', e30.clone().lerp(e12, .35).setY(2)); place('L_rest', REST.clone().setY(5));
  } else if (sh === 'end_layout') {
    st = 42.5; tickMat.opacity = .6;
    const c = END.clone().lerp(REST, .5);
    look(c.clone().add(left.clone().multiplyScalar(lerp(-650, -480, U))).add(dir.clone().multiplyScalar(lerp(-420, -300, U))).add(V(0, lerp(520, 380, U), 0)), c, 40);
    place('L_end', END.clone().setY(2), seg(t, T.x1.start + 1, T.x1.start + 1.5));
    place('L_loc', END.clone().add(dir.clone().multiplyScalar(110)).setY(2), seg(t, T.x1.start + 6, T.x1.start + 6.5));
    place('L_road', REST.clone().add(dir.clone().multiplyScalar(-40)).add(left.clone().multiplyScalar(-60)).setY(2), seg(t, T.x1.start + 10, T.x1.start + 10.5));
    place('L_rest', REST.clone().setY(10), seg(t, T.x2.start, T.x2.start + .5));
  } else if (sh === 'land_follow') {
    const a = T.l3.start;
    st = L.id === 'l7' ? lerp(18, 21, U) : lerp(-1, 18, seg(t, a, s1)); showHud = true; tickMat.opacity = .8; tdMat.opacity = .9;
    poseJet(st); const p = jet.position.clone();
    look(p.clone().add(dir.clone().multiplyScalar(-110)).add(left.clone().multiplyScalar(-45)).add(V(0, 32, 0)), p.clone().add(dir.clone().multiplyScalar(70)), 40);
    place('L_td', at(3750).setY(2));
  } else if (sh === 'land_side') {
    st = lerp(25, 34, U); showHud = true; tickMat.opacity = .8; tdMat.opacity = .9;
    poseJet(st);
    const c = at(7700);
    look(c.clone().add(left.clone().multiplyScalar(260)).add(V(0, 70, 0)).add(dir.clone().multiplyScalar(-120)), at(lerp(7300, 8300, U)).setY(5), 40);
    place('L_end', END.clone().setY(2));
  } else if (sh === 'replay') {
    st = lerp(-4, 42.5, U); showHud = true; tickMat.opacity = .8; tdMat.opacity = .9;
    poseJet(st); const p = jet.position.clone();
    const back = st < 30 ? 1 : 1 - seg(st, 30, 38);
    look(p.clone().add(dir.clone().multiplyScalar(-150 * back - 40)).add(left.clone().multiplyScalar(-90 - 120 * (1 - back))).add(V(0, 45 + 80 * (1 - back), 0)), p.clone().add(dir.clone().multiplyScalar(60 * back)), 40);
    place('L_end', END.clone().setY(2), st > 26 ? 1 : 0);
  } else if (sh === 'rest_orbit') {
    st = 42.5; const a = lerp(0.6, 1.9, U);
    look(REST.clone().add(V(Math.sin(a) * 260, lerp(120, 200, U), Math.cos(a) * 260)), REST.clone().add(V(0, 5, 0)), 40);
    place('L_rest', REST.clone().setY(16));
  }
  if (sh !== 'approach' && sh !== 'replay' && sh !== 'threshold' && sh !== 'land_follow' && sh !== 'land_side' && sh !== 'overrun_fast') poseJet(42.5);
  hud(st, showHud);
  sun.target.position.copy(jet.position); sun.position.copy(jet.position).add(V(-400, 900, 300));
  renderer.render(scene, cam);
}
window.renderAt = renderAt;
window.SEGINFO = () => TM.map(d => [d.id, d.start, d.end, d.vis]);
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
