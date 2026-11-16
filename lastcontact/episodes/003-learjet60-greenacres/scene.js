import * as THREE from 'three';
const TM = await (await fetch('timing.json')).json();
const T = {}; TM.forEach((d, i) => { d.i = i; T[d.id] = d; });
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const MI = 1609.34;

function lineAt(t) { let L = TM[0]; for (const d of TM) { if (d.start <= t + 1e-6) L = d; else break; } return L; }
const key = v => JSON.stringify(v.vis[0] === '3d' || v.vis[0] === 'card' ? v.vis.slice(0, 2) : v.vis);
function segStart(L) { let i = L.i; while (i > 0 && key(TM[i - 1]) === key(L)) i--; return i === 0 ? 0 : TM[i].start; }
function segEnd(L) { let i = L.i; while (i < TM.length - 1 && key(TM[i + 1]) === key(L)) i++; return i < TM.length - 1 ? TM[i + 1].start : TM[i].end + 2; }

// ---------- renderer
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(0.7); renderer.setSize(1920, 1080, false);
$('gl').style.width = '1920px'; $('gl').style.height = '1080px';
renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 2, 80000);
const loader = new THREE.TextureLoader();

// ================= SKY SCENE (cruise) =================
const sky = new THREE.Scene();
sky.background = new THREE.Color(0x5d6b7c); sky.fog = new THREE.Fog(0x5d6b7c, 3000, 22000);
sky.add(new THREE.HemisphereLight(0xdde6f0, 0x3a4048, 1.3));
const sSun = new THREE.DirectionalLight(0xfff2e0, 1.6); sSun.position.set(-3000, 5000, 2000); sky.add(sSun);
// cloud texture (procedural noise)
function noiseTex(n, seed, dark) {
  const c = document.createElement('canvas'); c.width = c.height = n; const g = c.getContext('2d');
  let s = seed; const rnd = () => (s = (s * 16807) % 2147483647) / 2147483647;
  g.fillStyle = dark ? '#4b5562' : '#c9d1da'; g.fillRect(0, 0, n, n);
  for (let k = 0; k < 2600; k++) {
    const x = rnd() * n, y = rnd() * n, r = 8 + rnd() * 70, a = 0.05 + rnd() * 0.12;
    const gr = g.createRadialGradient(x, y, 0, x, y, r);
    const col = dark ? (rnd() < .5 ? '30,36,44' : '120,130,142') : (rnd() < .6 ? '245,248,252' : '150,160,172');
    gr.addColorStop(0, `rgba(${col},${a})`); gr.addColorStop(1, `rgba(${col},0)`); g.fillStyle = gr; g.fillRect(x - r, y - r, 2 * r, 2 * r);
  }
  const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; return t;
}
const deckTex = noiseTex(1024, 7, false); deckTex.repeat.set(14, 14);
const deck = new THREE.Mesh(new THREE.PlaneGeometry(60000, 60000), new THREE.MeshStandardMaterial({ map: deckTex, roughness: 1 }));
deck.rotation.x = -Math.PI / 2; deck.position.y = -2600; sky.add(deck);
// storm towers: clusters of spheres
const towerMat = new THREE.MeshStandardMaterial({ color: 0xb4bdc8, roughness: 1, map: noiseTex(512, 3, false) });
const towers = new THREE.Group(); sky.add(towers);
let sd = 11; const r2 = () => (sd = (sd * 16807) % 2147483647) / 2147483647;
function tower(x, z, h, w) {
  const g = new THREE.Group();
  for (let k = 0; k < 26; k++) {
    const yy = -2600 + r2() * h, rr = w * (0.45 + r2() * 0.5) * (yy > -2600 + h * .8 ? 1.4 : 1);
    const m = new THREE.Mesh(new THREE.SphereGeometry(rr, 14, 10), towerMat);
    m.position.set(x + (r2() - .5) * w * 1.2, yy, z + (r2() - .5) * w * 1.2); g.add(m);
  }
  towers.add(g);
}
tower(5200, -9000, 3600, 1100); tower(-6200, -12000, 3200, 1300); tower(7600, -16000, 3900, 1500); tower(-3800, -7000, 2700, 900); tower(1500, -19000, 3800, 1700); tower(-9000, 3000, 3300, 1300); tower(9000, 4000, 3000, 1200);

// ---------- generic T-tail business jet (nose -Z, metres)
const white = new THREE.MeshStandardMaterial({ color: 0xe8edf2, roughness: .4, metalness: .15 });
const grey = new THREE.MeshStandardMaterial({ color: 0x8e99a8, roughness: .5, metalness: .35 });
const glass = new THREE.MeshStandardMaterial({ color: 0x18212c, roughness: .1, metalness: .6 });
const elevMat = new THREE.MeshStandardMaterial({ color: 0xe8edf2, roughness: .4, metalness: .15, emissive: 0x000000 });
const stripe = new THREE.MeshStandardMaterial({ color: 0x2a3a52, roughness: .5 });
const box = (w, h, d, m) => new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m);
let LELEV, HSTAB;
function makeJet() {
  const g = new THREE.Group(); const R = 0.95, L = 13;
  const fus = new THREE.Mesh(new THREE.CylinderGeometry(R, R * .9, L, 24), white); fus.rotation.x = Math.PI / 2; g.add(fus);
  const nose = new THREE.Mesh(new THREE.SphereGeometry(R, 24, 16, 0, Math.PI * 2, 0, Math.PI / 2), white); nose.rotation.x = -Math.PI / 2; nose.scale.set(1, 2.0, 1); nose.position.z = -L / 2; g.add(nose);
  const tail = new THREE.Mesh(new THREE.CylinderGeometry(R * .35, R * .9, 3.0, 24), white); tail.rotation.x = Math.PI / 2; tail.position.set(0, .2, L / 2 + 1.5); g.add(tail);
  const ws = box(1.3, .35, .9, glass); ws.position.set(0, .55, -L / 2 - .5); ws.rotation.x = .5; g.add(ws);
  const st = box(.06, .12, L * .9, stripe); for (const s of [-1, 1]) { const q = st.clone(); q.position.set(s * .93, -.05, 0); g.add(q); }
  for (const s of [-1, 1]) {
    const wing = box(6.4, .22, 2.1, white); wing.position.set(s * 3.6, -.55, .6); wing.rotation.y = s * -.32; wing.rotation.z = s * -.05; g.add(wing);
    const tip = box(.12, .7, 1.0, white); tip.position.set(s * 6.7, -.25, 2.5); g.add(tip);
    const eng = new THREE.Mesh(new THREE.CylinderGeometry(.55, .45, 2.8, 20), grey); eng.rotation.x = Math.PI / 2; eng.position.set(s * 1.75, .45, 4.6); g.add(eng);
    const py = box(.9, .18, .9, white); py.position.set(s * 1.2, .4, 4.6); g.add(py);
  }
  const fin = box(.22, 3.0, 2.2, white); fin.position.set(0, 2.1, 7.9); fin.rotation.x = .45; g.add(fin);
  HSTAB = new THREE.Group(); HSTAB.position.set(0, 3.45, 8.9); g.add(HSTAB);
  for (const s of [-1, 1]) {
    const hs = box(2.7, .14, 1.05, white); hs.position.set(s * 1.4, 0, 0); hs.rotation.y = s * -.25; HSTAB.add(hs);
    const el = box(2.4, .1, .45, s < 0 ? elevMat : white); el.position.set(s * 1.5, 0, 1.15); el.rotation.y = s * -.25; HSTAB.add(el);
    if (s < 0) LELEV = el;   // left elevator (pilot's left = -x with nose -Z)
  }
  return g;
}
const jet = makeJet(); sky.add(jet);

// ================= GROUND SCENE (site) =================
const ground = new THREE.Scene();
ground.background = new THREE.Color(0x9aa6b2); ground.fog = new THREE.Fog(0x9aa6b2, 14000, 40000);
ground.add(new THREE.HemisphereLight(0xffffff, 0x555555, 2.2));
async function groundPlane(file, size, y, offs) {
  const tx = await loader.loadAsync(file); tx.colorSpace = THREE.SRGBColorSpace; tx.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), new THREE.MeshBasicMaterial({ map: tx, polygonOffset: true, polygonOffsetFactor: offs, polygonOffsetUnits: offs }));
  m.rotation.x = -Math.PI / 2; m.position.y = y; ground.add(m); return m;
}
await groundPlane('wide.jpg', 17000, -0.5, 2);
const nearP = await groundPlane('near.jpg', 3200, 0, -2);
const flat = (mesh, y) => { mesh.rotation.x = -Math.PI / 2; mesh.position.y = y; ground.add(mesh); return mesh; };
const ringMat = c => new THREE.MeshBasicMaterial({ color: c, transparent: true, opacity: 0, depthWrite: false, depthTest: false, side: THREE.DoubleSide });
const ring1 = flat(new THREE.Mesh(new THREE.RingGeometry(1.3 * MI - 22, 1.3 * MI + 22, 160), ringMat(0xFFB020)), 3);
const ring2 = flat(new THREE.Mesh(new THREE.RingGeometry(3.8 * MI - 40, 3.8 * MI + 40, 220), ringMat(0xFFB020)), 3);
const band = flat(new THREE.Mesh(new THREE.RingGeometry(1.3 * MI, 3.8 * MI, 220), ringMat(0xFFB020)), 2);
const field = flat(new THREE.Mesh(new THREE.CircleGeometry(1, 64), ringMat(0xFFB020)), 4); field.scale.set(0.25 * MI, 0.2 * MI, 1);
const fieldEdge = flat(new THREE.Mesh(new THREE.RingGeometry(.97, 1, 96), ringMat(0xFFB020)), 4.5); fieldEdge.scale.copy(field.scale);
const site = flat(new THREE.Mesh(new THREE.RingGeometry(60, 85, 64), ringMat(0xFF2E2E)), 5);

function place(id, w3, show = 1) {
  const el = $(id), v = w3.clone().project(cam);
  el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080) + 'px';
  el.style.opacity = (v.z < 1 && show) ? show : 0;
}
function look(p, tg, fov = 40) { cam.position.copy(p); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tg); cam.updateMatrixWorld(); }

// ---------- radio calls list (card)
const CALLS = [
  ['~12:47', '35,000 ft · Miami Center — crew reports light clear ice, “manageable”', 't2'],
  ['~12:47', 'Moderate turbulence · altitude deviations ~700 ft', 't3'],
  ['~12:47', 'Outside air temperature −47 °C · precipitation', 't4'],
  ['~12:47', 'Crew requests climb to 37,000 ft · ATC approves', 't5'],
  ['< 30 s', 'Transmission announces the descent · then a mayday call', 't6'],
  ['~12:48', '“…overspeed condition, descending…” · rest unintelligible', 't7'],
  ['later', 'Rapid descent described · altitude callouts', 't8'],
  ['~12:51', 'Impact', 't8']];
$('callin').innerHTML = CALLS.map(([a, b], i) => `<div class="cv" id="cl${i}"><div class="t" style="width:150px">${a}</div><div>${b}</div></div>`).join('');

const CARDS = [...document.querySelectorAll('.card')];
const LBLS = ['L_site', 'L_field', 'L_r1', 'L_r2', 'L_rings', 'L_elev', 'L_hs', 'L_jet'];

function poseJetCruise(t, dive) {
  const z = -t * 230; jet.position.set(0, 0, z); jet.rotation.set(0, 0, 0); jet.rotation.order = 'YXZ';
  jet.rotation.z = Math.sin(t * 1.3) * 0.05 + Math.sin(t * 3.7) * 0.02; // turbulence wobble
  jet.position.y = Math.sin(t * 0.9) * 6 + Math.sin(t * 2.3) * 2.5;
  if (dive) { jet.rotation.x = -0.45 * dive; jet.position.y -= dive * dive * 260; }
  deck.position.z = 0; towers.position.z = jet.position.z;
}

function renderAt(t) {
  const L = lineAt(t), vis = L.vis, s0 = segStart(L), s1 = segEnd(L), u = t - s0, U = seg(t, s0, s1);
  CARDS.forEach(c => c.style.opacity = 0); LBLS.forEach(id => $(id).style.opacity = 0);
  ['recon', 'cred', 'hud', 'ev', 'ovs'].forEach(id => $(id).style.opacity = 0);
  const fadeIn = clamp(u / 0.35), fadeOut = clamp((s1 - t) / 0.35);
  if (vis[0] === 'card') {
    const c = $('c_' + vis[1]); c.style.opacity = Math.min(fadeIn, fadeOut);
    c.querySelectorAll('[data-from]').forEach(el => { const d = T[el.dataset.from]; el.style.opacity = d ? clamp((t - d.start) / 0.4) : 1; });
    if (vis[1] === 'calls') {
      const recap = L.id[0] === 'k';
      CALLS.forEach(([, , id], i) => { const d = T[id]; const on = recap || t >= d.start; const el = $('cl' + i); el.style.opacity = on ? 1 : 0;
        el.classList.toggle('on', recap ? ((L.id === 'k2' && i <= 3) || (L.id === 'k3' && i >= 4)) : id === L.id); });
    }
    if (vis[1] === 'status') $('sweep').setAttribute('transform', `rotate(${(t * 60) % 360})`);
    return;
  }
  const sh = vis[1]; let scn = sky;
  $('recon').style.opacity = 1;
  [ring1, ring2, band, field, fieldEdge, site].forEach(m => m.material.opacity = 0);
  for (const m of LELEV ? [LELEV.material] : []) m.emissive.setHex(0x000000);
  if (sh === 'cruise' || sh === 'overspeed') {
    poseJetCruise(u, 0); const p = jet.position.clone();
    const a = sh === 'cruise' ? lerp(-2.55, -1.9, U) : lerp(2.4, 2.0, U);
    look(p.clone().add(V(Math.sin(a) * 30, 6 + 3 * U, Math.cos(a) * 30)), p.clone().add(V(0, 0, 1)), 38);
    if (sh === 'cruise') { $('hud').style.opacity = fadeIn; $('htm').textContent = '12:47'; $('hal').textContent = '35,000 FT';
      place('L_jet', p.clone().add(V(0, 4.5, 0)), seg(u, .5, 1) * (1 - seg(u, 6, 6.5))); }
    else {
      $('ovs').style.opacity = fadeIn; const k = ease(seg(t, T.e9.start, T.e9.start + 4));
      $('ovbar').style.width = (40 + 46 * k) + '%'; $('ovbar').style.background = k > 0.82 ? 'var(--red)' : 'var(--green)';
      $('ovw').style.opacity = k > 0.82 ? (Math.floor(t * 2.5) % 2 ? 1 : .35) : 0;
    }
  } else if (sh === 'cruise_dive') {
    const k = ease(U); poseJetCruise(u + 20, k); const p = jet.position.clone();
    look(p.clone().add(V(-28 - 12 * k, 8 + 10 * k, 24 + 14 * k)), p, 38);
    $('hud').style.opacity = 1; $('htm').textContent = U < 0.55 ? '12:47' : '~12:48'; $('hal').textContent = 'NOT PUBLISHED';
    $('ev').textContent = U < 0.55 ? 'DESCENT ANNOUNCED · MAYDAY CALL (NTSB)' : '“OVERSPEED CONDITION, DESCENDING” (NTSB)'; $('ev').style.opacity = 1;
  } else if (sh === 'tail') {
    poseJetCruise(u * 0.2, 0); jet.rotation.z = 0; const p = jet.position.clone();
    const tl = p.clone().add(V(0, 3.4, 8.9)); const a = lerp(0.5, 1.1, U);
    look(tl.clone().add(V(-Math.sin(a) * 13, 4 + 1.5 * U, Math.cos(a) * 13)), tl.clone().add(V(0, -0.8, -2)), 38);
    const pulse = 0.5 + 0.5 * Math.sin(t * 4); LELEV.material.emissive.setRGB(1.0 * pulse, 0.55 * pulse, 0.05 * pulse);
    LELEV.rotation.x = Math.sin(t * 1.5) * 0.25;
    place('L_elev', tl.clone().add(V(-1.8, 0.6, 0.9)), fadeIn); place('L_hs', tl.clone().add(V(1.6, 0.8, 0)), fadeIn);
  } else {
    scn = ground; $('cred').style.opacity = .9;
    const O = V(0, 0, 0);
    if (sh === 'site_wide') {
      look(V(lerp(-2600, -1200, ease(U)), lerp(9000, 3800, ease(U)), lerp(5200, 2600, ease(U))), O, 40);
      site.material.opacity = .9; place('L_site', V(0, 0, 0), seg(u, 1, 1.6));
    } else if (sh === 'site_field') {
      look(V(lerp(-900, -500, U), lerp(2100, 1600, U), lerp(1400, 1000, U)), O, 40);
      field.material.opacity = .28 * fadeIn; fieldEdge.material.opacity = .95 * fadeIn; site.material.opacity = .9;
      place('L_field', V(0, 0, -0.2 * MI), seg(u, .6, 1.2)); place('L_site', V(0, 0, 0), .0);
    } else if (sh === 'site_rings') {
      const k = ease(clamp(u / 6));
      look(V(0, lerp(9000, 17500, k), lerp(4000, 6500, k)), V(0, 0, -300), 42);
      ring1.material.opacity = .95 * seg(u, .3, 1); ring2.material.opacity = .95 * seg(u, 1, 1.7); band.material.opacity = .13 * seg(u, 1, 1.7);
      site.material.opacity = 1; site.scale.setScalar(4);
      place('L_r1', V(1.3 * MI * .707, 0, -1.3 * MI * .707), seg(u, .5, 1)); place('L_r2', V(3.8 * MI * .707, 0, -3.8 * MI * .707), seg(u, 1.2, 1.8));
      const el = $('L_rings'); el.style.left = '56px'; el.style.top = '120px'; el.style.opacity = seg(u, 1.5, 2.1);
    }
    if (sh !== 'site_rings') site.scale.setScalar(1);
  }
  renderer.render(scn, cam);
}
window.renderAt = renderAt;
window.DUR = TM[TM.length - 1].end + 2;
window.READY = true;
