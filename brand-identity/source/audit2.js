() => {
  const cv = document.createElement('canvas'); cv.width = cv.height = 1;
  const cx = cv.getContext('2d', { willReadFrequently: true });
  const rgba = (c) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = '#000'; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255]; };
  const lum = ([r, g, b]) => { const f = (v) => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const over = (t, b) => { const a = t[3]; return [t[0] * a + b[0] * (1 - a), t[1] * a + b[1] * (1 - a), t[2] * a + b[2] * (1 - a), 1]; };
  const ratio = (a, b) => { const L1 = lum(a), L2 = lum(b); return (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05); };
  const bgOf = (el) => { const st = []; let e = el; while (e && e.nodeType === 1) { const c = rgba(getComputedStyle(e).backgroundColor); if (c[3] > 0) { st.push(c); if (c[3] >= 1) break; } e = e.parentElement; } let col = [255, 255, 255, 1]; for (let i = st.length - 1; i >= 0; i--) col = over(st[i], col); return col; };
  const parentBg = (el) => bgOf(el.parentElement || el);
  const where = (el) => { const ph = el.closest('figure')?.querySelector('figcaption')?.textContent || el.closest('section')?.querySelector('h2')?.textContent || ''; return `${ph} · ${(el.className?.baseVal ?? el.className) || el.tagName}`.slice(0, 70); };
  const out = { nonText: [], clipped: [], tiny: [], target: [], inlineHex: 0 };
  // 2. non-text: tab underline, input/checkbox borders, switch track
  document.querySelectorAll('.tabs > .on').forEach((el) => {
    const sh = getComputedStyle(el).boxShadow; const m = sh.match(/(rgba?\([^)]+\)|color\([^)]+\)|#[0-9a-f]+)/i);
    if (!m || !/inset/.test(sh)) { out.nonText.push({ what: 'tab underline missing', at: where(el) }); return; }
    const r = ratio(rgba(m[1]), parentBg(el)); if (r < 3) out.nonText.push({ what: `tab underline ${r.toFixed(2)}:1`, at: where(el) });
  });
  document.querySelectorAll('.input:not(.dis), .check:not(.on), .radio:not(.on), .switch:not(.on):not(:checked)').forEach((el) => {
    const s = getComputedStyle(el); const isSwitch = el.classList.contains('switch');
    const col = isSwitch ? rgba(s.backgroundColor) : rgba(s.borderTopColor); const r = ratio(over(col, parentBg(el)), parentBg(el));
    const need = el.classList.contains('input') ? 1.5 : 3;   // input boundaries: hairline allowed (label + fill identify it); toggles need 3:1
    if (r < need) out.nonText.push({ what: `${el.className} boundary ${r.toFixed(2)}:1 (need ${need})`, at: where(el) });
  });
  // 3. clipped / overflowing text
  document.querySelectorAll('b, span, small, p, div, button, label').forEach((el) => {
    if (!el.childNodes.length || ![...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) return;
    const s = getComputedStyle(el); if (s.display === 'inline') return;
    if (el.scrollWidth > el.clientWidth + 2 && s.overflow !== 'visible' && s.textOverflow !== 'ellipsis') out.clipped.push({ what: `text overflows by ${el.scrollWidth - el.clientWidth}px: "${el.textContent.trim().slice(0, 30)}"`, at: where(el) });
  });
  // 5. tiny text
  const seen = new Set(); const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) { const t = w.currentNode; const el = t.parentElement; if (!t.textContent.trim() || seen.has(el) || el.closest('svg')) continue; seen.add(el); const fs = parseFloat(getComputedStyle(el).fontSize); if (fs < 11) out.tiny.push({ what: `${fs}px "${t.textContent.trim().slice(0, 24)}"`, at: where(el) }); }
  // 4. tap targets inside phones
  document.querySelectorAll('.phone .btn, .phone .chip, .phone .iconbtn, .phone .tabbar > div, .phone .topbar > .ic').forEach((el) => { const r = el.getBoundingClientRect(); if (r.height < 32 || r.width < 32) out.target.push({ what: `${Math.round(r.width)}×${Math.round(r.height)}`, at: where(el) }); });
  // 6. inline hex colours
  document.querySelectorAll('[style]').forEach((el) => { if (/#[0-9a-f]{3,6}\b/i.test(el.getAttribute('style'))) out.inlineHex++; });
  const cap = (a) => a.slice(0, 25);
  return { nonText: cap(out.nonText), nNonText: out.nonText.length, clipped: cap(out.clipped), nClipped: out.clipped.length, tiny: cap(out.tiny), nTiny: out.tiny.length, target: cap(out.target), nTarget: out.target.length, inlineHex: out.inlineHex };
}
