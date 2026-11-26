# ugly/broken sweep layer 3
XT3 = r"""
/* nw6: neutral hairline notices, equal-height pages with the action pinned low */
.nw6 .n-page { display: flex; flex-direction: column; align-items: center; }
.nw6 .n-page .n-c { margin-top: auto; padding-top: 16px; }
/* nw8: task screenshot tiles - one short scrim at the foot, not a full-height wash */
.nw8 .m-reel::before { display: none; }
.nw8 .m-reel::after { height: 34%; background: linear-gradient(to top, rgba(13,14,18,.62), rgba(13,14,18,0)); }
.nw8 .m-up.err { gap: 8px; }
/* nw9: description list values sit at the trailing edge */
.nw9 .n-dl > div { grid-template-columns: 1fr auto; }
.nw9 .t-head .t-lg, .nw9 .t-m .t-av .t-lg { border-radius: 50%; }
/* dm: white surfaces, no grey slabs */
.sec.dm .dm-rc .file, .sec.dm .dm-done, .sec.dm .dm-note { background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.sec.dm .dm-shots .s.add { background: var(--hd-surface); border: 1px dashed var(--hd-edge); }
.sec.dm .input.textarea { background: var(--hd-surface); }
.sec.dm .dm-task.slim { max-width: none; }
/* mn: wallet hero action is full width */
.mn-sec .mn-hb .btn { width: 100%; }
.mn-sec .mn-hb { align-self: stretch; }
/* mn: withdraw account option - white, one signal (the radio) */
.mn-sec .mn-opt.sel { background: var(--hd-surface); border-color: var(--hd-fg-muted); }
/* mn: blockers - white surface, hairline, glyph carries the meaning */
.mn-sec .mn-note, .mn-sec .mn-note.info, .mn-sec .mn-note.danger, .mn-sec .mn-note.warning { background: var(--hd-surface); border: 1px solid var(--hd-edge); }
.mn-sec .mn-note.info > .ic { color: var(--hd-accent); }
.mn-sec .mn-bar i { background: var(--hd-fg-muted); }
.mn-sec .mn-pt { display: flex; }
"""
