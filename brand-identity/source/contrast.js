() => {
  // Resolve any CSS colour (rgb, color(srgb), oklab, color-mix…) to RGBA through a canvas pixel.
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', { willReadFrequently: true });
  const rgba = (c) => {
    cx.clearRect(0, 0, 1, 1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1);
    const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255];
  };
  const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const over = (top, bot) => { const a = top[3]; return [top[0] * a + bot[0] * (1 - a), top[1] * a + bot[1] * (1 - a), top[2] * a + bot[2] * (1 - a), 1]; };
  const bgOf = (el) => {
    const stack = []; let e = el, unknown = false;
    while (e && e.nodeType === 1) {
      const s = getComputedStyle(e);
      if (s.backgroundImage && s.backgroundImage !== 'none') unknown = true;
      const c = rgba(s.backgroundColor); if (c[3] > 0) { stack.push(c); if (c[3] >= 1) break; }
      e = e.parentElement;
    }
    let col = [255, 255, 255, 1];
    for (let i = stack.length - 1; i >= 0; i--) col = over(stack[i], col);
    return { col, unknown };
  };
  const dimmed = (el) => { let e = el; while (e && e.nodeType === 1) { if (parseFloat(getComputedStyle(e).opacity) < 0.99) return true; e = e.parentElement; } return false; };
  const out = []; let checked = 0;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const t = walker.currentNode; const txt = t.textContent.trim(); if (!txt) continue;
    const el = t.parentElement; if (!el || seen.has(el)) continue; seen.add(el);
    const r = el.getBoundingClientRect(); if (r.width === 0 || r.height === 0) continue;
    if (el.closest('svg')) { /* chart labels */ }
    const s = getComputedStyle(el); if (s.visibility === 'hidden') continue;
    const fg = rgba(s.color); const { col: bg, unknown } = bgOf(el); const fgc = fg[3] < 1 ? over(fg, bg) : fg;
    const L1 = lum(fgc), L2 = lum(bg); const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const size = parseFloat(s.fontSize), weight = parseInt(s.fontWeight, 10);
    const large = size >= 24 || (size >= 18.66 && weight >= 700);
    const need = large ? 3 : 4.5; checked++;
    if (ratio < need && !dimmed(el)) {
      out.push({ text: txt.slice(0, 40), ratio: +ratio.toFixed(2), need, size, cls: (el.className && el.className.baseVal === undefined ? el.className : el.tagName).toString().slice(0, 40),
                 theme: el.closest('[data-theme]')?.getAttribute('data-theme') || 'root', bgUnknown: unknown, fg: s.color });
    }
  }
  return { checked, failures: out.slice(0, 80), total: out.length };
}
