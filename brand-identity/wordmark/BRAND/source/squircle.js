// Squircles + tactile surfaces for the static kit (Zen/Firefox has no `corner-shape`).
// Each target gets an absolutely positioned SVG behind its content: a continuous-curvature
// (figma-squircle, smoothing 0.6) path carrying the fill, the hairline/border, the tactile lip
// and the layered shadow. Photos get the same path as a clip-path. No SVG <mask> anywhere.
(function () {
  const SMOOTH = 0.6, SCALE = 1.18;   // squircles read tighter than arcs at the same radius
  const rad = (d) => d * Math.PI / 180;
  function corner(r, s, budget) {
    let p = (1 + s) * r;
    if (p > budget) { s = Math.max(0, Math.min(s, budget / r - 1)); p = Math.min(p, budget); }
    const arc = 90 * (1 - s), arcLen = Math.sin(rad(arc / 2)) * r * Math.SQRT2;
    const alpha = (90 - arc) / 2, p34 = r * Math.tan(rad(alpha / 2)), beta = 45 * s;
    const c = p34 * Math.cos(rad(beta)), d = c * Math.tan(rad(beta));
    let b = (p - arcLen - c - d) / 3; if (b < 0) b = 0; const a = 2 * b;
    return { a, b, c, d, p, r, arcLen };
  }
  function path(w, h, r, inset = 0) {
    const W = w - inset * 2, H = h - inset * 2, R = Math.max(0, Math.min(r * SCALE, Math.min(W, H) / 2)) ;
    if (R <= 0.5) return `M${inset} ${inset}H${inset + W}V${inset + H}H${inset}Z`;
    const k = corner(R, SMOOTH, Math.min(W, H) / 2), { a, b, c, d, p, arcLen } = k, x0 = inset, y0 = inset;
    const f = (n) => n.toFixed(2);
    return `M${f(x0 + W - p)} ${f(y0)}` +
      `c${f(a)} 0 ${f(a + b)} 0 ${f(a + b + c)} ${f(d)}a${f(R)} ${f(R)} 0 0 1 ${f(arcLen)} ${f(arcLen)}c${f(d)} ${f(c)} ${f(d)} ${f(b + c)} ${f(d)} ${f(a + b + c)}` +
      `L${f(x0 + W)} ${f(y0 + H - p)}` +
      `c0 ${f(a)} 0 ${f(a + b)} ${f(-d)} ${f(a + b + c)}a${f(R)} ${f(R)} 0 0 1 ${f(-arcLen)} ${f(arcLen)}c${f(-c)} ${f(d)} ${f(-(b + c))} ${f(d)} ${f(-(a + b + c))} ${f(d)}` +
      `L${f(x0 + p)} ${f(y0 + H)}` +
      `c${f(-a)} 0 ${f(-(a + b))} 0 ${f(-(a + b + c))} ${f(-d)}a${f(R)} ${f(R)} 0 0 1 ${f(-arcLen)} ${f(-arcLen)}c${f(-d)} ${f(-c)} ${f(-d)} ${f(-(b + c))} ${f(-d)} ${f(-(a + b + c))}` +
      `L${f(x0)} ${f(y0 + p)}` +
      `c0 ${f(-a)} 0 ${f(-(a + b))} ${f(d)} ${f(-(a + b + c))}a${f(R)} ${f(R)} 0 0 1 ${f(arcLen)} ${f(-arcLen)}c${f(c)} ${f(-d)} ${f(b + c)} ${f(-d)} ${f(a + b + c)} ${f(-d)}Z`;
  }
  const cv = document.createElement('canvas').getContext('2d');
  function rgba(col) { cv.fillStyle = '#000'; cv.fillStyle = col; const s = cv.fillStyle; if (s[0] === '#') { const n = parseInt(s.slice(1), 16); return [n >> 16, (n >> 8) & 255, n & 255, 1]; } const m = s.match(/[\d.]+/g).map(Number); return [m[0], m[1], m[2], m[3] ?? 1]; }
  const mix = (c, t, k) => `rgba(${c.slice(0, 3).map((v, i) => Math.round(v + (t[i] - v) * k)).join(',')},${c[3]})`;
  function ringOf(cs) {   // border, else an inset 0 0 0 Npx ring in box-shadow
    const bw = parseFloat(cs.borderTopWidth);
    if (bw > 0 && cs.borderTopStyle !== 'none') return { w: bw, c: cs.borderTopColor };
    const m = cs.boxShadow.match(/(rgba?\([^)]+\)|#[0-9a-f]+)\s+0px\s+0px\s+0px\s+([\d.]+)px\s+inset|inset\s+0px\s+0px\s+0px\s+([\d.]+)px\s+(rgba?\([^)]+\))/i);
    if (m) return { w: parseFloat(m[2] || m[3]), c: m[1] || m[4] };
    const o2 = cs.boxShadow.match(/(rgba?\([^)]+\))\s+0px\s+0px\s+0px\s+([\d.]+)px(?!\s+inset)/);
    if (o2) return { w: parseFloat(o2[2]), c: o2[1] };
    return null;
  }
    const SURF = '.x-go, .x-disc';   // filled surfaces only; anything with a hairline (secondary, cards, tiles) stays native CSS so edges are crisp   // in-flow surfaces use native border + box-shadow: always crisp on any device-pixel ratio
  const IMG = 'img.lead, .x-hero, .rv-av, .media img, .row img, .card img[src*="products"]';
  const done = new WeakSet();
  const INK = [16, 20, 38];
  // Elevation specs: [dy, blur, spread, alpha]. blur = CSS box-shadow blur (stdDeviation = blur / 2).
  const LEVELS = {
    0: [[1, 0, 0, .05], [2, 4, -1, .035]],   // crisp: a no-blur 1px contact + a faint ambient
    2: [[1, 2, 0, .06], [4, 8, -2, .07], [12, 16, -4, .09]],
    3: [[2, 4, 0, .05], [8, 16, -2, .08], [24, 40, -8, .12]],
  };
  const spread3 = (c) => Math.max(c[0], c[1], c[2]) - Math.min(c[0], c[1], c[2]);
  // one filter, every shadow computed in parallel from the same alpha (no shadow-of-a-shadow smear)
  function shadowFilter(id, w, h, specs, rgb, dark) {
    let m = 0; specs.forEach(([dy, bl, sp]) => { m = Math.max(m, bl * 1.5 + Math.abs(dy) + Math.max(0, sp)); }); m = Math.ceil(m) + 2;
    let f = `<filter id="${id}" filterUnits="userSpaceOnUse" x="${-m}" y="${-m}" width="${w + 2 * m}" height="${h + 2 * m}" color-interpolation-filters="sRGB">`, names = '';
    specs.forEach(([dy, bl, sp, a], i) => {
      const al = dark ? Math.min(.6, a * 3.4) : a;
      let src = 'SourceAlpha';
      if (sp) { f += `<feMorphology in="SourceAlpha" operator="${sp < 0 ? 'erode' : 'dilate'}" radius="${Math.abs(sp)}" result="m${i}"/>`; src = `m${i}`; }
      f += `<feGaussianBlur in="${src}" stdDeviation="${bl / 2}" result="b${i}"/><feOffset in="b${i}" dy="${dy}" result="o${i}"/>` +
        `<feFlood flood-color="rgb(${rgb})" flood-opacity="${al}"/><feComposite in2="o${i}" operator="in" result="s${i}"/>`;
      names = `<feMergeNode in="s${i}"/>` + names;   // widest ambient at the back
    });
    return f + `<feMerge>${names}<feMergeNode in="SourceGraphic"/></feMerge></filter>`;
  }
  let uid = 0;
  function surface(el) {
    if (done.has(el) || el.closest('.no-sq, .btngroup, .seg') || el.classList.contains('foc') || el.offsetWidth < 16) return;
    const cs = getComputedStyle(el), r = parseFloat(cs.borderTopLeftRadius) || 0;
    if (r < 4 || r >= Math.min(el.offsetWidth, el.offsetHeight) / 2 - 0.5) return;   // pills and circles stay circles
    const gradBg = cs.backgroundImage !== 'none';   // CSS gradient/image fill stays; the squircle clips it and carries the hairline
    const dark = document.documentElement.dataset.theme === 'dark' || !!el.closest('[data-theme="dark"]');
    const D = window.devicePixelRatio || 1, snap = (v) => Math.round(v * D) / D, HAIR = Math.max(1, Math.round(D)) / D;   // whole device pixels
    const bb = el.getBoundingClientRect(), bwid = parseFloat(cs.borderTopWidth) || 0, w = snap(bb.width), h = snap(bb.height), bg = rgba(cs.backgroundColor);
    const snapX = snap(bb.left) - bb.left - bwid, snapY = snap(bb.top) - bb.top - bwid;   // land the SVG on the device-pixel grid so hairlines stay one crisp line
    const isBtn = el.classList.contains('btn'), solid = isBtn && (el.classList.contains('p') || el.classList.contains('d'));
    const sec = isBtn && el.classList.contains('s'), pressed = el.classList.contains('prs'), dis = el.classList.contains('dis');
    const level = el.matches('.dialog') ? 3 : el.matches('.menu, .toast, .suggest') ? 2 : 0;
    const edge = (cs.getPropertyValue(level ? '--hd-edge-2' : '--hd-edge') || '').trim() || (dark ? 'rgba(255,255,255,.10)' : 'rgba(16,20,38,.12)');
    // ring: the element's own coloured border/ring (selection, error) is kept; neutral hairlines become the shared edge token
    let ring = ringOf(cs);
    if (ring) { const c = rgba(ring.c); if (ring.w < 2 && spread3(c) < 34) ring = { w: 1, c: edge }; }
    else if (!isBtn) ring = { w: 1, c: edge };
    else if (sec) ring = { w: 1, c: edge };
    if (isBtn && !sec && !solid) ring = ring && ring.c !== edge ? ring : null;
    const NS = 'http://www.w3.org/2000/svg', svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'sq-bg'); svg.setAttribute('width', w); svg.setAttribute('height', h); svg.setAttribute('viewBox', `0 0 ${w} ${h}`); svg.setAttribute('aria-hidden', 'true');
    const id = 'q' + (++uid);
    let o = '', defs = '';
    const lip = dis || pressed ? 0 : solid ? 2 : sec ? 1 : 0;
    const body = path(w, h - lip, r), full = path(w, h, r);
    const opaque = bg[3] >= .95 && !gradBg;
    // shadows (buttons: the lip is the shadow; no blurry glow)
    const specs = isBtn ? null : opaque ? LEVELS[level] : null;
    const shadowed = !!specs;
    if (shadowed) defs += shadowFilter(id + 's', w, h, specs, dark ? '0,0,0' : INK.join(','), dark);
    if (lip) {
      const lc = solid ? mix(bg, [0, 0, 0], dark ? .45 : .32) : (dark ? 'rgba(0,0,0,.55)' : 'rgba(16,20,38,.16)');
      o += `<path d="${full}" fill="${lc}"/>`;
    }
    if (bg[3] > 0 && !gradBg) {
      let fill = cs.backgroundColor;
      if (solid && !dis) { defs += `<linearGradient id="${id}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(bg, [255, 255, 255], pressed ? 0 : .07)}"/><stop offset="1" stop-color="${mix(bg, [0, 0, 0], pressed ? .06 : 0)}"/></linearGradient>`; fill = `url(#${id}g)`; }
      if (shadowed) o += `<path d="${body}" fill="${fill}" filter="url(#${id}s)"/>`;   // shadow pass (filtered)
      o += `<path d="${body}" fill="${fill}"/>`;   // crisp pass: fill and edges never go through the filter
    }
    if (solid && !dis) {
      o += `<path d="${path(w, h - lip, r, .5)}" fill="none" stroke="${mix(bg, [0, 0, 0], .22)}" stroke-width="1"/>`;
      if (!pressed) { defs += `<linearGradient id="${id}h" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="rgba(255,255,255,.30)"/><stop offset=".45" stop-color="rgba(255,255,255,0)"/></linearGradient>`;
        o += `<path d="${path(w, h - lip, r, 1)}" fill="none" stroke="url(#${id}h)" stroke-width="1"/>`; }
    } else if (ring && ring.w > 0) {
      { const rw = ring.w <= 1.01 ? HAIR : Math.round(ring.w * D) / D; o += `<path d="${path(w, h, r)} ${path(w, h, r, rw)}" fill="${ring.c}" fill-rule="evenodd"/>`; }   // ring as a filled band: edges land on device pixels, so it stays one crisp line
    }
    if (dark && !isBtn && bg[3] > 0 && !gradBg && !(ring && ring.w >= 2)) {   // 1px top inner highlight: shadows alone vanish on dark
      defs += `<linearGradient id="${id}t" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="rgba(255,255,255,${level ? .08 : .05})"/><stop offset=".35" stop-color="rgba(255,255,255,0)"/></linearGradient>`;
      o += `<path d="${path(w, h, r, 1.5)}" fill="none" stroke="url(#${id}t)" stroke-width="1"/>`;
    }
    svg.innerHTML = (defs ? `<defs>${defs}</defs>` : '') + o;
    Object.assign(svg.style, { position: 'absolute', left: snapX + 'px', top: snapY + 'px', zIndex: '-1', pointerEvents: 'none', overflow: 'visible' });
    if (cs.position === 'static') el.style.position = 'relative';
    el.style.transition = 'none';   // the CSS bg/shadow must drop at once, not fade over 160ms (screenshots caught the old paint)
    el.style.isolation = 'isolate'; if (gradBg) el.style.clipPath = `path("${path(el.offsetWidth, el.offsetHeight, r)}")`; else el.style.background = 'transparent';
    el.style.setProperty('box-shadow', 'none', 'important');
    el.style.border = (parseFloat(cs.borderTopWidth) > 0 ? `${cs.borderTopWidth} solid transparent` : '');
    if (pressed) el.style.transform = 'translateY(1px)';
    el.prepend(svg); done.add(el);
    el.getBoundingClientRect(); requestAnimationFrame(() => requestAnimationFrame(() => { el.style.transition = ''; }));
  }
  function image(el) {
    if (done.has(el)) return; const r = parseFloat(getComputedStyle(el).borderTopLeftRadius) || 0;
    if (r < 4 || r >= Math.min(el.offsetWidth, el.offsetHeight) / 2 - 0.5) return;
    el.style.clipPath = `path("${path(el.offsetWidth, el.offsetHeight, r)}")`; el.style.borderRadius = '0'; done.add(el);
  }
  function run() { document.querySelectorAll(IMG).forEach(image); document.querySelectorAll(SURF).forEach(surface); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(run); else window.addEventListener('load', run);
})();
