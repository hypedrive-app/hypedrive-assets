# UI-skills pass layer (owned by the skills-pass agent). Appended very last.
XPASS = r"""
/* ===== XPASS · skills pass ===== */
/* calendar range days: text on the accent tint reaches AA (was 4.4:1) */
.cal .cg .rng { color: var(--hd-info-strong); }
/* initials in small avatars never drop under 10px */
.av[style*="width:20px"], .av[style*="width:21px"], .av[style*="width:22px"], .av[style*="width:23px"], .av[style*="width:24px"] { font-size: 10px !important; letter-spacing: 0; }
"""
