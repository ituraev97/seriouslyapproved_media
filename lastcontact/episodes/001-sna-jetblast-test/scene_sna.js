import * as THREE from 'three';
const TM = await (await fetch('timing.json')).json();
const GEO = await (await fetch('geo.json')).json();
const T = {}; TM.forEach(d => T[d.id] = d);
const DUR = TM[TM.length - 1].end + 1.5;
window.DUR = DUR;

// ---------- helpers
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const eo = x => 1 - Math.pow(1 - x, 3);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
const $ = id => document.getElementById(id);
function fade(el, t, a, b, f = 0.35) { // visible in [a,b] with fades
  const o = Math.min(seg(t, a, a + f), 1 - seg(t, b - f, b));
  el.style.opacity = o; return o;
}
function typeText(el, full, t, a, cps = 40) {
  const n = Math.floor(clamp((t - a) * cps, 0, full.length));
  el.textContent = full.slice(0, n);
}

// ---------- renderer
const renderer = new THREE.WebGLRenderer({ canvas: $('gl'), antialias: true, preserveDrawingBuffer: true });
renderer.setSize(1920, 1080, false);
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.05;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x9fb4c8);
scene.fog = new THREE.Fog(0x9fb4c8, 4000, 9000);
const cam = new THREE.PerspectiveCamera(40, 1920 / 1080, 5, 20000);

scene.add(new THREE.HemisphereLight(0xdfeaff, 0x5b5040, 1.1));
const sun = new THREE.DirectionalLight(0xfff1dc, 2.4);
sun.position.set(-600, 900, 500); sun.castShadow = true;
sun.shadow.mapSize.set(2048, 2048);
const sc = sun.shadow.camera; sc.left = -120; sc.right = 120; sc.top = 120; sc.bottom = -120; sc.near = 10; sc.far = 3000;
scene.add(sun); scene.add(sun.target);

// ground
const G = GEO.ground;
const tex = await new THREE.TextureLoader().loadAsync('sna.jpg');
tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
const ground = new THREE.Mesh(new THREE.PlaneGeometry(G, G), new THREE.MeshStandardMaterial({ map: tex, roughness: 1 }));
ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);
const outer = new THREE.Mesh(new THREE.PlaneGeometry(40000, 40000), new THREE.MeshStandardMaterial({ color: 0x55584f, roughness: 1 }));
outer.rotation.x = -Math.PI / 2; outer.position.y = -0.5; scene.add(outer);
tex.anisotropy = renderer.capabilities.getMaxAnisotropy();
const ptex = await new THREE.TextureLoader().loadAsync('sna_patch.jpg'); ptex.colorSpace = THREE.SRGBColorSpace; ptex.anisotropy = renderer.capabilities.getMaxAnisotropy();
const patch = new THREE.Mesh(new THREE.PlaneGeometry(GEO.patch.size, GEO.patch.size), new THREE.MeshStandardMaterial({ map: ptex, roughness: 1, polygonOffset: true, polygonOffsetFactor: -4, polygonOffsetUnits: -4 }));
patch.rotation.x = -Math.PI / 2; patch.position.set(GEO.patch.cx, 0.05, GEO.patch.cz); patch.receiveShadow = true; scene.add(patch);
scene.background = new THREE.Color(0xa9c2db); scene.fog.color.set(0xa9c2db);

// runway geometry
const p02L = V(GEO.rw['02L'][0], 0, GEO.rw['02L'][1]), p20R = V(GEO.rw['20R'][0], 0, GEO.rw['20R'][1]);
const p02R = V(GEO.rw['02R'][0], 0, GEO.rw['02R'][1]), p20L = V(GEO.rw['20L'][0], 0, GEO.rw['20L'][1]);
const u = p20R.clone().sub(p02L).normalize();          // runway direction (NNE)
const r = V(-u.z, 0, u.x);                               // perpendicular to the east
const hdg = v => Math.atan2(-v.x, -v.z);                 // yaw so that model's -Z faces v

function runwayStrip(a, b, w, color) {
  const len = a.distanceTo(b), mid = a.clone().add(b).multiplyScalar(.5);
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, len), new THREE.MeshBasicMaterial({ color, transparent: true, opacity: 0, depthWrite: false }));
  m.rotation.x = -Math.PI / 2; m.rotation.z = -hdg(b.clone().sub(a)) ; m.position.copy(mid).setY(0.6);
  // align: plane's local Y (length) along a->b
  m.rotation.set(-Math.PI / 2, 0, Math.atan2(b.x - a.x, -(b.z - a.z)) * -1);
  scene.add(m); return m;
}
const stripL = runwayStrip(p02L, p20R, 46, 0xFFB000);
const stripR = runwayStrip(p02R, p20L, 23, 0x39C6F4);

// ---------- models
const white = new THREE.MeshStandardMaterial({ color: 0xe9eef3, roughness: .45, metalness: .1 });
const grey = new THREE.MeshStandardMaterial({ color: 0x9aa5b5, roughness: .5, metalness: .3 });
const dark = new THREE.MeshStandardMaterial({ color: 0x252a33, roughness: .6 });
const blue = new THREE.MeshStandardMaterial({ color: 0x24406e, roughness: .5 });
const glass = new THREE.MeshStandardMaterial({ color: 0x1b2533, roughness: .1, metalness: .6 });
function sh(m) { m.traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } }); return m; }
function box(w, h, d, mat) { return new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat); }

function makeJet() { // nose toward -Z, length ~39.5 m, span ~35.8 m
  const g = new THREE.Group();
  const fus = new THREE.Mesh(new THREE.CylinderGeometry(1.9, 1.9, 30, 24), white); fus.rotation.x = Math.PI / 2; fus.position.set(0, 3.2, 0); g.add(fus);
  const nose = new THREE.Mesh(new THREE.SphereGeometry(1.9, 24, 16, 0, Math.PI * 2, 0, Math.PI / 2), white); nose.rotation.x = -Math.PI / 2; nose.scale.set(1, 2.2, 1); nose.position.set(0, 3.2, -15); g.add(nose);
  const tail = new THREE.Mesh(new THREE.ConeGeometry(1.9, 8, 24), white); tail.rotation.x = Math.PI / 2; tail.position.set(0, 3.6, 19); g.add(tail);
  const belly = box(3.4, .5, 30, blue); belly.position.set(0, 1.55, 0); g.add(belly);
  const ws = box(.5, .25, 1, glass); ws.scale.set(5, 1, 1.2); ws.position.set(0, 4.35, -15.8); g.add(ws);
  for (const s of [-1, 1]) {
    const wing = new THREE.Mesh(new THREE.BoxGeometry(16.5, .45, 4.5), white);
    wing.position.set(s * 9.5, 2.0, 1.5); wing.rotation.y = s * 0.45; wing.rotation.z = s * -0.08; g.add(wing);
    const eng = new THREE.Mesh(new THREE.CylinderGeometry(1.0, .85, 4.2, 20), grey); eng.rotation.x = Math.PI / 2; eng.position.set(s * 5, 1.25, -2.6); g.add(eng);
    const inlet = new THREE.Mesh(new THREE.CircleGeometry(.95, 20), dark); inlet.position.set(s * 5, 1.25, -4.72); inlet.rotation.y = Math.PI; g.add(inlet);
    const hs = box(6.5, .25, 2.4, white); hs.position.set(s * 3.6, 4.1, 19.5); hs.rotation.y = s * 0.5; g.add(hs);
    const mg = box(.4, 1.6, .4, dark); mg.position.set(s * 2.9, .8, 2.5); g.add(mg);
    const mw = new THREE.Mesh(new THREE.CylinderGeometry(.55, .55, .5, 16), dark); mw.rotation.z = Math.PI / 2; mw.position.set(s * 2.9, .55, 2.5); g.add(mw);
  }
  const vs = new THREE.Mesh(new THREE.BoxGeometry(.4, 7.5, 5), blue); vs.position.set(0, 8, 19.5); vs.rotation.x = -0.45; g.add(vs);
  const ng = box(.3, 1.5, .3, dark); ng.position.set(0, .8, -12.5); g.add(ng);
  g.userData.engines = [V(-5, 1.25, -0.5), V(5, 1.25, -0.5)];
  return sh(g);
}
function makeCessna() { // nose toward -Z, length 8.3 m, span 11 m. Origin = main-gear ground contact.
  const g = new THREE.Group(), body = new THREE.Group(); g.add(body);
  const fus = box(1.15, 1.35, 4.2, white); fus.position.set(0, 1.35, -0.9); body.add(fus);
  const cowl = box(1.0, 1.0, 1.2, white); cowl.position.set(0, 1.15, -3.5); body.add(cowl);
  const boom = new THREE.Mesh(new THREE.CylinderGeometry(.25, .6, 3.6, 12), white); boom.rotation.x = Math.PI / 2; boom.position.set(0, 1.45, 2.9); body.add(boom);
  const stripe = box(1.17, .18, 4.2, blue); stripe.position.set(0, 1.0, -0.9); body.add(stripe);
  const wing = box(11, .16, 1.55, white); wing.position.set(0, 2.15, -1.2); body.add(wing);
  const cab = box(1.1, .55, 1.4, glass); cab.position.set(0, 1.95, -1.5); body.add(cab);
  const hs = box(3.4, .1, .95, white); hs.position.set(0, 1.55, 4.5); body.add(hs);
  const vs = box(.1, 1.55, 1.1, white); vs.position.set(0, 2.25, 4.45); vs.rotation.x = -.35; body.add(vs);
  const prop = box(1.8, .1, .06, dark); prop.position.set(0, 1.15, -4.15); body.add(prop); g.userData.prop = prop;
  for (const s of [-1, 1]) { const w = new THREE.Mesh(new THREE.CylinderGeometry(.27, .27, .18, 14), dark); w.rotation.z = Math.PI / 2; w.position.set(s * 1.15, .27, 0); body.add(w);
    const st = box(.08, .5, .08, grey); st.position.set(s * .9, .5, 0); st.rotation.z = s * .6; body.add(st); }
  const nw = new THREE.Mesh(new THREE.CylinderGeometry(.22, .22, .14, 12), dark); nw.rotation.z = Math.PI / 2; nw.position.set(0, .22, -3.0); body.add(nw);
  g.userData.body = body;
  return sh(g);
}
const jet = makeJet(); scene.add(jet);
const ces = makeCessna(); scene.add(ces);

// placement (illustrative)
const thr = p02L.clone().add(u.clone().multiplyScalar(70));
const jetPos = thr.clone().add(r.clone().multiplyScalar(105));       // holding east of runway, nose toward runway (-r)
jet.position.copy(jetPos); jet.rotation.y = hdg(r.clone().negate());
const jetTail = jetPos.clone().add(r.clone().multiplyScalar(22));
// cessna path: southbound on a taxiway behind the jet, then left turn (east)
const lane = r.clone().multiplyScalar(160);
const P0 = thr.clone().add(lane).add(u.clone().multiplyScalar(260));
const P1 = thr.clone().add(lane).add(u.clone().multiplyScalar(20));
const P2 = thr.clone().add(lane).add(u.clone().multiplyScalar(-6)).add(r.clone().multiplyScalar(18));
const curve = new THREE.CatmullRomCurve3([P0, P0.clone().lerp(P1, .5), P1, P1.clone().lerp(P2, .5).add(r.clone().multiplyScalar(-2)), P2]);
const pathLen = curve.getLength();
const pathMat = new THREE.MeshBasicMaterial({ color: 0x39C6F4, transparent: true, opacity: 0 });
const pathMesh = new THREE.Mesh(new THREE.TubeGeometry(curve, 120, .6, 6), pathMat); pathMesh.position.y = .4; scene.add(pathMesh);

// cessna pose: k in [0,1] along path, flip in [0,1]
const FLIPK = 0.93;
function poseCessna(k, flip) {
  const p = curve.getPointAt(clamp(k)), tg = curve.getTangentAt(clamp(Math.min(k, .999)));
  ces.position.copy(p); ces.rotation.set(0, hdg(tg), 0);
  const body = ces.userData.body;
  body.position.set(0, 0, 0); body.rotation.set(0, 0, 0);
  if (flip <= 0) return;
  const tot = ease(clamp(flip)) * Math.PI * 0.985;
  const piv = V(0, 0, -3.0);
  const R = new THREE.Matrix4().makeRotationX(-tot);
  const o = V(0, 0, 0).sub(piv).applyMatrix4(R).add(piv);
  body.position.copy(o); body.rotation.x = -tot;
  body.position.y += 2.4 * Math.pow(seg(tot, Math.PI * 0.45, Math.PI), 1.3) + 0.25 * Math.sin(Math.PI * clamp(flip));
  body.rotation.z = 0.18 * Math.sin(Math.PI * clamp(flip));
}
// ---------- jet blast particles
const NP = 900;
const pg = new THREE.BufferGeometry(); const ppos = new Float32Array(NP * 3); pg.setAttribute('position', new THREE.BufferAttribute(ppos, 3));
const pseed = Array.from({ length: NP }, (_, i) => [Math.random(), Math.random(), Math.random(), i % 2]);
const spr = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d'); const gr = x.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,255,255,1)'); gr.addColorStop(1, 'rgba(255,255,255,0)'); x.fillStyle = gr; x.fillRect(0, 0, 64, 64); return new THREE.CanvasTexture(c); })();
const pmat = new THREE.PointsMaterial({ map: spr, color: 0xffd28a, size: 0.9, transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending });
const pts = new THREE.Points(pg, pmat); scene.add(pts);
function blast(t, power) { // power 0..1
  pmat.opacity = 0.5 * power;
  const back = r.clone(), side = u.clone();
  for (let i = 0; i < NP; i++) {
    const [a, b, c, e] = pseed[i];
    const ph = ((t * (0.35 + power * 0.9)) + a) % 1;      // travel phase
    const d = ph * (90 + 70 * power);
    const spread = 1.0 + d * 0.11;
    const eng = jet.userData.engines[e].clone().applyMatrix4(jet.matrixWorld);
    const p = eng.clone().add(back.clone().multiplyScalar(d + 2)).add(side.clone().multiplyScalar((b - .5) * spread * 2)).setY(1.25 + (c - .5) * spread * .8 + d * 0.012);
    ppos[i * 3] = p.x; ppos[i * 3 + 1] = Math.max(.2, p.y); ppos[i * 3 + 2] = p.z;
  }
  pg.attributes.position.needsUpdate = true;
}

// ---------- labels
function place(el, w3, dy = 0) {
  const v = w3.clone().project(cam);
  el.style.left = ((v.x + 1) / 2 * 1920) + 'px'; el.style.top = ((1 - v.y) / 2 * 1080 + dy) + 'px';
}

// ---------- camera helpers
function look(pos, tgt, fov = 40) { cam.position.copy(pos); cam.fov = fov; cam.updateProjectionMatrix(); cam.lookAt(tgt); }
function orbit(center, radius, height, angle, fov = 40) { look(center.clone().add(V(Math.sin(angle) * radius, height, Math.cos(angle) * radius)), center, fov); }
const site = P2.clone();
const mid = p02L.clone().lerp(p20R, .5);

const FAA_TXT = "“A Cessna 172 was blown over while taxiing behind United Airlines Flight 2611 at John Wayne Airport in Santa Ana, California, around 2:30 p.m. on Saturday, Nov. 7. Two people were on board. The FAA will investigate.”";
const ACCT = [
  ["acct2", "He began a left turn toward the entrance as the Boeing increased power to enter Runway 02L."],
  ["acct3", "At almost the same moment the Cessna was “struck by a sudden jet blast.”"],
  ["acct4", "In a written statement quoted by the Orange County Register, the student said the blast lifted the tail; the airplane rolled forward and went over."],
];
const M1 = "METAR KSNA 072253Z 26006KT 10SM CLR 29/03 A2997";
const M2 = "METAR KSNA 072153Z 33006KT 10SM CLR 30/02 A2996";

const ALL = ['recon','srcline','imgcred','lt1','lt2','faa','title','rL','rR','jetL','cesL','rwyfacts','acct','two','metar','jb','ntsb','aim','status','endcard'];

function renderAt(t) {
  ALL.forEach(id => $(id).style.opacity = 0);
  stripL.material.opacity = 0; stripR.material.opacity = 0; pathMat.opacity = 0;
  pmat.opacity = 0; renderer.toneMappingExposure = 1.05; scene.fog.near = 2500;
  let k = 0, flip = 0, power = 0, src = '';
  jet.visible = true; ces.visible = true;
  jet.updateMatrixWorld(true);

  // ---- A: hook
  if (t < T.faa.start) {
    const a = T.hook1.start, b = T.hook2.start, c = T.hook3.start;
    if (t < b) { // descending establishing shot
      const s = ease(seg(t, 0, b));
      const fc = site.clone().lerp(jetTail, .4);
      const q = seg(t, 0, b), s2 = 1 - Math.pow(1 - q, 2);  // smooth ease-out, no whip
      const pos = fc.clone().add(V(lerp(-420, -110, s2), lerp(520, 80, s2), lerp(420, 90, s2)));
      look(pos, fc, 40);
      k = lerp(0.35, FLIPK - 0.02, seg(t, 0, b)); power = lerp(0.15, 0.6, seg(t, b - 2, b));
      fade($('lt1'), t, 1.2, b - 0.2);
    } else if (t < c) { // the flip
      const s = seg(t, b, T.hook2.end);
      k = FLIPK; flip = ease(clamp(s * 1.15)); power = 1;
      orbit(site.clone().lerp(jetTail, .4), 105, 42, lerp(2.25, 2.45, s), 38);
    } else {
      k = FLIPK; flip = 1; power = lerp(1, .15, seg(t, c, c + 2));
      orbit(site, 75, 32, lerp(2.5, 3.2, seg(t, c, T.faa.start)), 38);
      fade($('lt2'), t, c + .2, T.faa.start - .1);
    }
    $('recon').style.opacity = 1; $('imgcred').style.opacity = .9;
  }
  // ---- B: FAA statement
  else if (t < T.title.start) {
    fade($('faa'), t, T.faa.start, T.title.start, .3);
    typeText($('faatext'), FAA_TXT, t, T.faa.start + .2, 34);
    orbit(site, 300, 200, 1, 40); k = FLIPK; flip = 1;
  }
  // ---- C: title (top view behind)
  else if (t < T.rwy1.start) {
    orbit(mid, 1, 2600, 0.0001, 40); fade($('title'), t, T.title.start, T.rwy1.start, .3); k = FLIPK; flip = 1;
    renderer.toneMappingExposure = .7;
  }
  // ---- D: runways
  else if (t < T.pos1.start) {
    const s = ease(seg(t, T.rwy1.start, T.pos1.start));
    look(mid.clone().add(V(lerp(0, 300, s), lerp(2500, 1700, s), lerp(10, 900, s))), mid.clone().add(V(0, 0, lerp(0, 150, s))), 40);
    stripL.material.opacity = .55 * seg(t, T.rwy2.start, T.rwy2.start + .6);
    stripR.material.opacity = .65 * seg(t, T.rwy3.start, T.rwy3.start + .6);
    if (t > T.rwy2.start) { $('rL').style.opacity = seg(t, T.rwy2.start, T.rwy2.start + .5); place($('rL'), p02L.clone().lerp(p20R, .3)); }
    if (t > T.rwy3.start) { $('rR').style.opacity = seg(t, T.rwy3.start, T.rwy3.start + .5); place($('rR'), p02R.clone().lerp(p20L, .25)); }
    fade($('rwyfacts'), t, T.rwy2.start + .3, T.pos1.start, .3);
    jet.visible = false; ces.visible = false; src = 'RUNWAY DATA: FAA AIRPORT RECORDS VIA OURAIRPORTS';
    $('recon').style.opacity = 0;
  }
  // ---- E: positions
  else if (t < T.acct1.start) {
    const s = ease(seg(t, T.pos1.start, T.acct1.start));
    const c0 = jetPos.clone().lerp(P1, .5);
    look(c0.clone().add(V(lerp(-300, -190, s), lerp(240, 130, s), lerp(230, 170, s))), c0, 40);
    k = lerp(0.1, 0.75, seg(t, T.pos2.start, T.acct1.start)); power = .15;
    $('jetL').style.opacity = seg(t, T.pos1.start + .3, T.pos1.start + .8); place($('jetL'), jetPos.clone().setY(12));
    if (t > T.pos2.start) { $('cesL').style.opacity = seg(t, T.pos2.start, T.pos2.start + .5); ces.updateMatrixWorld(); place($('cesL'), ces.position.clone().setY(4)); pathMat.opacity = .8; }
    $('recon').style.opacity = 1; src = 'FLIGHT & DESTINATION: CNN · REGISTRATION: AVIATIONPROS / OC REGISTER';
  }
  // ---- F: account replay
  else if (t < T.wind1.start) {
    fade($('acct'), t, T.acct1.start + .2, T.wind1.start - .1);
    const lines = ACCT.filter(([id]) => t >= T[id].start - .1).map(([, s]) => s);
    $('acctBody').innerHTML = lines.map((s, i) => `<div style="margin-bottom:16px;${i < lines.length - 1 ? 'color:#9fb0c6' : ''}">${s}</div>`).join('');
    const a2 = T.acct2.start, a3 = T.acct3.start, a4 = T.acct4.start;
    if (t < a4) {
      k = lerp(.6, FLIPK, seg(t, a2, a3 + .3)); power = lerp(.15, 1, seg(t, a2 + 2.5, a3 + .3));
      flip = ease(seg(t, a3 + .4, a3 + 3.4));
      const s = seg(t, T.acct1.start, a4);
      orbit(site.clone().lerp(jetTail, .4), lerp(170, 115, s), lerp(85, 48, s), lerp(1.7, 2.25, s), 40);
    } else { // slow-motion side view
      k = FLIPK; power = 1; flip = ease(seg(t, a4 + .3, T.acct4.end + .3));
      const lat = V(-u.x, 0, -u.z);
      look(site.clone().add(lat.multiplyScalar(-62)).add(V(0, 16, 0)).add(r.clone().multiplyScalar(-10)), site.clone().add(V(0, 2, 0)).add(r.clone().multiplyScalar(16)), 36);
      $('srcline').style.opacity = 1;
    }
    $('recon').style.opacity = 1; src = "PILOT'S ACCOUNT: OCFC REPORT VIA FLYING MAGAZINE AND CNN · STUDENT QUOTE: ORANGE COUNTY REGISTER VIA AVIATIONPROS";
  }
  // ---- G: two explanations + weather
  else if (t < T.jb1.start) {
    k = FLIPK; flip = 1; orbit(site, 120, 60, 1, 40);
    if (t < T.wind3.start - .2) fade($('two'), t, T.wind1.start, T.wind3.start - .2, .3);
    else {
      fade($('metar'), t, T.wind3.start - .2, T.jb1.start, .3);
      typeText($('metarRaw'), M1, t, T.wind3.start, 30);
      typeText($('metarRaw2'), t > T.wind4.start ? M2 : '', t, T.wind4.start, 30);
      const rows = [
        [T.wind3.start + 1.6, 'TIME', '2:53 p.m. PST · Nov 7'],
        [T.wind3.start + 4.0, 'WIND', '260° at 6 knots'],
        [T.wind3.start + 7.0, 'SKY', 'Clear · visibility 10 miles'],
        [T.wind3.start + 9.0, 'TEMP', '29 °C'],
        [T.wind4.start + .5, '1 HR EARLIER', '330° at 6 knots'],
        [T.wind4.start + 2.0, 'GUSTS', 'None in either report'],
      ].filter(x => t > x[0]);
      $('decode').innerHTML = rows.map(([, a, b]) => `<div style="display:flex;font-size:38px;line-height:1.85"><div class="mono" style="width:330px;color:#8a97ab;font-size:28px;padding-top:6px">${a}</div><div style="font-weight:600">${b}</div></div>`).join('');
      $('compass').style.opacity = seg(t, T.wind3.start + 3.5, T.wind3.start + 4.2);
      $('arr2').setAttribute('opacity', seg(t, T.wind4.start + .5, T.wind4.start + 1));
      $('metarNote').style.opacity = seg(t, T.wind5.start, T.wind5.start + .4);
    }
  }
  // ---- H: jet blast explainer
  else if (t < T.ntsb1.start) {
    fade($('jb'), t, T.jb1.start, T.ntsb1.start, .3);
    jet.visible = false; ces.visible = false; look(V(0, 3000, 1), V(0, 0, 0));
    const pw = seg(t, T.jb3.start + 2, T.jb3.start + 4);
    $('plumePath').setAttribute('opacity', .25 + .75 * pw);
    $('plumePath').setAttribute('d', `M546 745 L${lerp(1100, 1900, pw)} ${lerp(690, 600, pw)} L${lerp(1100, 1900, pw)} ${lerp(810, 900, pw)} L546 755 Z`);
    // streaks
    const n = 26; let sv = '';
    for (let i = 0; i < n; i++) {
      const ph = ((t * (0.25 + pw * 0.8)) + i / n) % 1, x = 560 + ph * lerp(500, 1200, pw), y = 750 + Math.sin(i * 7.3) * ph * 110;
      sv += `<line x1="${x}" y1="${y}" x2="${x + 40 + pw * 50}" y2="${y}" stroke="#FFD27A" stroke-width="4" stroke-linecap="round" opacity="${(1 - ph) * (.35 + .65 * pw)}"/>`;
    }
    $('streaks').innerHTML = sv;
    fade($('jbW1'), t, T.jb2.start, T.jb3.start + .2, .3);
    fade($('jbW2'), t, T.jb3.start + .3, T.jb5.start, .3);
    $('jbW3').style.opacity = seg(t, T.jb5.start, T.jb5.start + .4);
    const fa = seg(t, T.jb5.start + .2, T.jb5.start + .8) * (1 - seg(t, T.jb5.start + 6.5, T.jb5.start + 7));
    $('forceArrow').setAttribute('opacity', fa);
    $('pivot').setAttribute('r', 22 * seg(t, T.jb5.start + 2.2, T.jb5.start + 2.6));
    // rotation about main gear (svg origin at main gear), nose right: nose-down = clockwise (positive)
    const rot = 10 * ease(seg(t, T.jb4.start + 1, T.jb4.start + 3)) + 90 * ease(seg(t, T.jb5.start + 3.4, T.jb5.start + 6.8));
    const r1 = Math.min(rot, 9), r2 = Math.max(0, rot - 9) * 1.75;
    const a = r1 * Math.PI / 180, nx = 150 * Math.cos(a) - (-5) * Math.sin(a), ny = 150 * Math.sin(a) + (-5) * Math.cos(a);
    const lift = -40 * seg(r2, 70, 165);
    $('c172').setAttribute('transform', `translate(0 ${lift}) rotate(${r2} ${nx} ${ny}) rotate(${r1})`);
  }
  // ---- I: NTSB precedent
  else if (t < T.aim.start) {
    fade($('ntsb'), t, T.ntsb1.start, T.aim.start, .3);
    $('nt1').style.opacity = seg(t, T.ntsb2.start + 6, T.ntsb2.start + 6.5);
    $('nt2').style.opacity = seg(t, T.ntsb3.start, T.ntsb3.start + .5);
    $('nt3').style.opacity = seg(t, T.ntsb4.start, T.ntsb4.start + .4);
    jet.visible = false; ces.visible = false; look(V(0, 3000, 1), V(0, 0, 0));
  }
  else if (t < T.end1.start) {
    fade($('aim'), t, T.aim.start, T.end1.start, .3);
    jet.visible = false; ces.visible = false; look(V(0, 3000, 1), V(0, 0, 0));
  }
  // ---- K: ending
  else {
    k = FLIPK; flip = 1;
    const s = seg(t, T.end1.start, DUR);
    orbit(site.clone().lerp(jetTail, .3), lerp(160, 520, s), lerp(60, 380, s), lerp(.6, 1.6, s), 40);
    fade($('status'), t, T.end1.start + .3, T.end3.start + .2, .3);
    fade($('endcard'), t, T.end3.end - 1.2, DUR + 1, .5);
    $('recon').style.opacity = 1; $('imgcred').style.opacity = .9;
  }
  if (src) { $('srcline').textContent = 'SOURCES: ' + src; $('srcline').style.opacity = 1; }

  poseCessna(k, flip);
  ces.userData.prop.rotation.z = flip > 0 ? 0.3 : t * 40;
  if (jet.visible) blast(t, power);
  // shadow follows the action
  sun.target.position.copy(site); sun.position.copy(site).add(V(-300, 500, 260));
  renderer.render(scene, cam);
}
window.renderAt = renderAt;
window.READY = true;
