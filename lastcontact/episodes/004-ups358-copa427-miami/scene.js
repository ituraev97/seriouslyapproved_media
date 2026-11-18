import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { RGBELoader } from 'three/addons/loaders/RGBELoader.js';
const TM = await (await fetch('timing.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const sm = x => x * x * (3 - 2 * x);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);

function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
function segStart(L) { let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--; return i === 0 ? 0 : TM[i].start; }
function segEnd(L) { let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++; return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2; }

// ---------- renderer
const PR = +(new URLSearchParams(location.search).get('pr') || window.PR || 0.7);
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(PR); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const cam = new THREE.PerspectiveCamera(38, 1920 / 1080, 0.3, 6000);

const scene = new THREE.Scene();
const hdr = await new RGBELoader().loadAsync('night.hdr');
hdr.mapping = THREE.EquirectangularReflectionMapping;
scene.environment = hdr; scene.environmentIntensity = 0.7;
scene.background = hdr; scene.backgroundIntensity = 0.35; scene.backgroundBlurriness = 0.15;
scene.fog = new THREE.Fog(0x1a2230, 500, 2600);
scene.add(new THREE.HemisphereLight(0x8fa6c8, 0x1a1a1a, 0.55));
const flood = new THREE.DirectionalLight(0xffe2b8, 2.4); flood.position.set(-120, 160, 90); flood.castShadow = true;
flood.shadow.mapSize.set(2048, 2048); const sc = flood.shadow.camera; sc.left = -140; sc.right = 140; sc.top = 140; sc.bottom = -140; sc.near = 10; sc.far = 600; flood.shadow.bias = -0.0004;
scene.add(flood); scene.add(flood.target);
const fill = new THREE.DirectionalLight(0x9db8ff, 0.5); fill.position.set(150, 80, -120); scene.add(fill);

// ---------- ground: generic intersection. Taxiway A along X (z=0), taxiway B along Z (x=0)
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; }
let sd = 5; const rnd = () => (sd = (sd * 16807) % 2147483647) / 2147483647;
const grassT = canvasTex(512, 512, (g, w, h) => { g.fillStyle = '#1d2a1c'; g.fillRect(0, 0, w, h); for (let i = 0; i < 9000; i++) { g.fillStyle = `rgba(${40 + rnd() * 40},${55 + rnd() * 40},${35 + rnd() * 25},.35)`; g.fillRect(rnd() * w, rnd() * h, 2, 2); } });
grassT.wrapS = grassT.wrapT = THREE.RepeatWrapping; grassT.repeat.set(60, 60);
const ground = new THREE.Mesh(new THREE.PlaneGeometry(5000, 5000), new THREE.MeshStandardMaterial({ map: grassT, roughness: 1 }));
ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
const concT = canvasTex(512, 512, (g, w, h) => { g.fillStyle = '#6b6e72'; g.fillRect(0, 0, w, h); for (let i = 0; i < 14000; i++) { const v = 85 + rnd() * 45; g.fillStyle = `rgba(${v},${v},${v + 3},.25)`; g.fillRect(rnd() * w, rnd() * h, 2, 2); } g.strokeStyle = 'rgba(40,40,40,.35)'; g.lineWidth = 2; for (let k = 0; k <= 4; k++) { g.beginPath(); g.moveTo(k * w / 4, 0); g.lineTo(k * w / 4, h); g.stroke(); g.beginPath(); g.moveTo(0, k * h / 4); g.lineTo(w, k * h / 4); g.stroke(); } });
concT.wrapS = concT.wrapT = THREE.RepeatWrapping;
const TW = 23; // taxiway width ~75 ft
function pave(w, l, x, z, rotZ, y) { const t = concT.clone(); t.needsUpdate = true; t.repeat.set(w / 20, l / 20); const m = new THREE.Mesh(new THREE.PlaneGeometry(w, l), new THREE.MeshStandardMaterial({ map: t, roughness: .92, polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -1 })); m.rotation.x = -Math.PI / 2; m.rotation.z = rotZ || 0; m.position.set(x, y, z); m.receiveShadow = true; scene.add(m); return m; }
pave(TW, 1400, 0, 0, Math.PI / 2, 0.03);   // taxiway A (along X)
pave(TW, 1400, 0, 0, 0, 0.04);             // taxiway B (along Z)
pave(TW + 16, TW + 16, 0, 0, 0, 0.05);     // fillet
const shMat = new THREE.MeshStandardMaterial({ color: 0x3b3d40, roughness: 1 });
for (const s of [-1, 1]) { const a = new THREE.Mesh(new THREE.PlaneGeometry(1400, 8), shMat); a.rotation.x = -Math.PI / 2; a.position.set(0, 0.015, s * (TW / 2 + 4)); a.receiveShadow = true; scene.add(a);
  const b = new THREE.Mesh(new THREE.PlaneGeometry(8, 1400), shMat); b.rotation.x = -Math.PI / 2; b.position.set(s * (TW / 2 + 4), 0.012, 0); b.receiveShadow = true; scene.add(b); }
const yel = new THREE.MeshStandardMaterial({ color: 0xd8a516, emissive: 0x3a2a00, roughness: .6 });
const cl1 = new THREE.Mesh(new THREE.PlaneGeometry(1400, .25), yel); cl1.rotation.x = -Math.PI / 2; cl1.position.y = .08; scene.add(cl1);
const cl2 = new THREE.Mesh(new THREE.PlaneGeometry(.25, 1400), yel); cl2.rotation.x = -Math.PI / 2; cl2.position.y = .085; scene.add(cl2);
function lights(color, pts, r) { const g = new THREE.SphereGeometry(r, 8, 6); const m = new THREE.MeshBasicMaterial({ color }); const im = new THREE.InstancedMesh(g, m, pts.length); const o = new THREE.Object3D(); pts.forEach((p, i) => { o.position.copy(p); o.updateMatrix(); im.setMatrixAt(i, o.matrix); }); scene.add(im); return im; }
const blue = [], green = [];
for (let d = -700; d <= 700; d += 30) { if (Math.abs(d) < TW) continue; for (const s of [-1, 1]) { blue.push(V(d, .45, s * (TW / 2 + .8))); blue.push(V(s * (TW / 2 + .8), .45, d)); } }
for (let d = -700; d <= 700; d += 15) { green.push(V(d, .12, 0)); if (Math.abs(d) > 2) green.push(V(0, .12, d)); }
lights(0x3a6bff, blue, .32); lights(0x46ff8a, green, .18);
const glowT = canvasTex(64, 64, (g) => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(.25, 'rgba(255,255,255,.35)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
function glows(color, pts, s) { const geo = new THREE.BufferGeometry().setFromPoints(pts); const m = new THREE.PointsMaterial({ color, size: s, map: glowT, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true }); scene.add(new THREE.Points(geo, m)); }
glows(0x4f7dff, blue, 3.2); glows(0x5cff9a, green, 2.0);
const bmat = new THREE.MeshStandardMaterial({ color: 0x20252c, roughness: 1 });
const winPts = [];
for (let k = 0; k < 26; k++) { const a = rnd() * Math.PI * 2, r = 650 + rnd() * 700; const w = 40 + rnd() * 120, h = 10 + rnd() * 30, d = 30 + rnd() * 60;
  const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), bmat); b.position.set(Math.cos(a) * r, h / 2, Math.sin(a) * r); b.rotation.y = rnd() * 3; scene.add(b);
  for (let q = 0; q < 6; q++) winPts.push(V(b.position.x + (rnd() - .5) * w, h + 3, b.position.z + (rnd() - .5) * d)); }
glows(0xffc77a, winPts, 14);

// ---------- aircraft models (clean livery, nose to +X, scaled to real length)
const loader = new GLTFLoader();
async function plane(file, lenTarget, opts) {
  const g = await loader.loadAsync(file); const o = g.scene;
  o.traverse(m => {
    if (!m.isMesh) return; m.castShadow = true; m.receiveShadow = true;
    if (opts.hide && opts.hide.includes(m.name)) { m.visible = false; return; }
    const mats = Array.isArray(m.material) ? m.material : [m.material];
    const nm = mats.map(mt => {
      const n = (mt.name || '').toLowerCase();
      const glass = mt.transparent || /glass|window|transp/.test(n);
      return new THREE.MeshStandardMaterial({ color: glass ? 0x14202c : 0xeceef0, roughness: glass ? .08 : .38, metalness: glass ? .6 : .12, side: THREE.DoubleSide });
    });
    m.material = Array.isArray(m.material) ? nm : nm[0];
  });
  const wrap = new THREE.Group(); const inner = new THREE.Group(); inner.add(o); wrap.add(inner);
  inner.rotation.y = opts.rotY || 0; inner.updateMatrixWorld(true);
  let b = new THREE.Box3().setFromObject(inner); const s = lenTarget / (b.max.x - b.min.x); inner.scale.setScalar(s); inner.updateMatrixWorld(true);
  b = new THREE.Box3().setFromObject(inner); inner.position.set(-(b.min.x + b.max.x) / 2, -b.min.y, -(b.min.z + b.max.z) / 2); inner.updateMatrixWorld(true);
  wrap.userData.box = new THREE.Box3().setFromObject(inner);
  scene.add(wrap); return wrap;
}
const B767 = await plane('b767.glb', 54.94, { rotY: window.R767 ?? Math.PI });
const B738 = await plane('b738.glb', 39.47, { rotY: window.R738 ?? Math.PI / 2, hide: ['Object_19'] });
const H767 = B767.userData.box, H738 = B738.userData.box;
const half738 = (H738.max.z - H738.min.z) / 2, nose767 = H767.max.x;

function place(id, w3, show = 1) {
  const el = $(id), v = w3.clone().project(cam);
  el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080) + 'px';
  el.style.opacity = (v.z < 1 && show) ? show : 0;
}
function look(p, tg, fov = 38) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }
const ring = new THREE.Mesh(new THREE.RingGeometry(1.6, 2.1, 48), new THREE.MeshBasicMaterial({ color: 0xff2e2e, transparent: true, opacity: 0, side: THREE.DoubleSide, depthTest: false }));
ring.renderOrder = 10; scene.add(ring);

// ---------- motion (illustrative). 737 along +X on z=0; 767 heading +Z on x=0
const C737X = window.C737X ?? 4.6;
const C767Z = -half738 + 0.8 - nose767;
function pose(k) {
  B738.position.set(C737X - (1 - k) * 160, 0, 0); B738.rotation.set(0, 0, 0);
  B767.position.set(0, 0, C767Z - (1 - k) * 95); B767.rotation.set(0, -Math.PI / 2, 0);
}
const CONTACT = () => V(0, window.CY ?? 4.4, -half738 + 0.3);
const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_cmp', 'L_ups', 'L_hit', 'L_wl', 'L_d767', 'L_d737', 'L_tip'];

function renderAt(t) {
  const L = lineAt(t), vis = L.vis, s0 = segStart(L), s1 = segEnd(L), u = t - s0, U = seg(t, s0, s1);
  CARDS.forEach(c => c.style.opacity = 0); LBLS.forEach(id => $(id).style.opacity = 0);
  ['recon', 'cred', 'hud', 'ev'].forEach(id => $(id).style.opacity = 0);
  const fadeIn = clamp(u / 0.35), fadeOut = clamp((s1 - t) / 0.35);
  if (vis[0] === 'card') {
    const c = $('c_' + vis[1]); c.style.opacity = Math.min(fadeIn, fadeOut);
    c.querySelectorAll('[data-from]').forEach(el => { const d = T[el.dataset.from]; el.style.opacity = d ? clamp((t - d.start) / 0.4) : 1; });
    if (vis[1] === 'status') $('sweep').setAttribute('transform', `rotate(${(t * 60) % 360})`);
    return;
  }
  return render3d(vis[1], u, U, s0, s1, fadeIn);
}
function render3d(sh, u, U, s0, s1, fadeIn) {
  $('recon').style.opacity = 1; $('cred').style.opacity = .85; ring.material.opacity = 0;
  B767.visible = B738.visible = true;
  if (sh === 'open_wide') {
    pose(lerp(0.0, 0.45, U)); const k = ease(U);
    look(V(lerp(-230, -170, k), lerp(95, 70, k), lerp(-210, -150, k)), V(-40, 0, -40), 40);
    $('hud').style.opacity = fadeIn;
    place('L_cmp', B738.position.clone().add(V(0, 15, 0)), seg(u, 2, 2.6)); place('L_ups', B767.position.clone().add(V(0, 19, 0)), seg(u, 5, 5.6));
  } else if (sh === 'approach') {
    pose(lerp(0.45, 0.8, U));
    look(V(lerp(-95, -80, U), 26, lerp(-95, -80, U)), V(-12, 3, -25), 40);
    place('L_cmp', B738.position.clone().add(V(0, 14, 0)), fadeIn); place('L_ups', B767.position.clone().add(V(0, 18, 0)), fadeIn);
    $('ev').textContent = 'ATC TO UPS 358: GIVE WAY TO THE COPA FLIGHT (FAA)'; $('ev').style.opacity = seg(u, .5, 1);
  } else if (sh === 'contact') {
    const k = clamp(U / 0.62); pose(lerp(0.8, 1.0, sm(k)));
    const a = lerp(-0.75, -0.45, U); const c = CONTACT();
    look(c.clone().add(V(Math.cos(a) * 42, 7, Math.sin(a) * 42)), c.clone().add(V(-4, -1, 0)), 36);
    if (U >= 0.62) { const p = (u - 0.62 * (s1 - s0)); ring.position.copy(c); ring.quaternion.copy(cam.quaternion); ring.scale.setScalar(1 + 0.15 * Math.sin(p * 5)); ring.material.opacity = .95;
      place('L_hit', c.clone().add(V(0, 2.5, 0)), clamp(p / .4)); }
    $('ev').textContent = U < 0.62 ? 'NTSB: UPS 358 DID NOT STOP' : 'NTSB: COPA LEFT WINGLET IMPACTED THE NOSE OF UPS 358'; $('ev').style.opacity = 1;
  } else if (sh === 'replay') {
    pose(ease(clamp(U / 0.75)));
    look(V(-60, 120, -120), V(-15, 0, -20), 42);
    place('L_cmp', B738.position.clone().add(V(0, 14, 0)), 1); place('L_ups', B767.position.clone().add(V(0, 18, 0)), 1);
    if (U > 0.75) { const c = CONTACT(); ring.position.copy(c); ring.quaternion.copy(cam.quaternion); ring.scale.setScalar(3); ring.material.opacity = .95; place('L_hit', c.clone().add(V(0, 3, 0)), seg(U, .75, .8)); }
  } else if (sh === 'sizes') {
    B767.position.set(0, 0, -30); B767.rotation.set(0, 0, 0); B738.position.set(-7.7, 0, 28); B738.rotation.set(0, 0, 0);
    const k = ease(U); look(V(lerp(-6, 0, k), lerp(175, 160, k), lerp(70, 60, k)), V(0, 0, 4), 40);
    place('L_d767', V(0, 0, -30 - 25), seg(u, .5, 1.1)); place('L_d737', V(-7.7, 0, 28 + 20), seg(u, 3, 3.6));
  } else if (sh === 'wingview') {
    B738.visible = false; B767.position.set(0, 0, 0); B767.rotation.set(0, 0, 0);
    look(V(lerp(36, 18, ease(U)), lerp(26, 20, ease(U)), -56), V(0, 3, -12), 44); place('L_tip', V(-7.1, 5.6, -23.8), seg(u, .6, 1.2));
  } else if (sh === 'winglet') {
    B767.visible = false; B738.position.set(0, 0, 0); B738.rotation.set(0, 0, 0);
    const a = lerp(-2.3, -1.4, ease(U)); const tip = V(window.WLX ?? -4.8, window.WLY ?? 5.2, -half738 + .3);
    look(tip.clone().add(V(Math.cos(a) * 24, 2, Math.sin(a) * 24)), tip.clone().add(V(4, -1, 6)), 40);
    place('L_wl', tip.clone().add(V(0, 1.8, 0)), seg(u, .6, 1.2));
  }
  const tg = cam.position.clone().setY(0).lerp(V(0, 0, 0), .7);
  flood.target.position.copy(tg); flood.position.copy(tg).add(V(-120, 160, 90));
  renderer.render(scene, cam);
}
window.renderAt = renderAt;
window.shot3d = (sh, U, dur = 10) => render3d(sh, U * dur, U, 0, dur, 1);
window.dbg = { B767, B738, H767, H738, half738, nose767, cam, scene, renderer, pose, look };
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
