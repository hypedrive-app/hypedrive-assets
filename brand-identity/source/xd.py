# Section polish layer (xd). Appended after XLEAD.
XD = r"""
/* product card: lighter scrims so the photo stays a photo */
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(10,12,18,.86) 0%, rgba(10,12,18,.68) 34%, rgba(10,12,18,0) 64%, rgba(10,12,18,0) 68%, rgba(10,12,18,.66) 100%) !important; }
/* media: 3-photo mosaic, no counter + dots together */
.m-mos { grid-template-columns: repeat(3, 1fr) !important; aspect-ratio: 3 / 2 !important; }
/* share sheet in a clean frame, no fake page behind it */
.n-shd.n-shclean { height: auto !important; padding: 16px; border-radius: 16px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.n-shclean .n-shs { position: relative !important; border-radius: 20px !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); box-shadow: 0 8px 24px rgba(16,20,38,.08); }
[data-theme="dark"] .n-shclean .n-shs { box-shadow: 0 8px 24px rgba(0,0,0,.4); }
/* swipe rows: the row narrows to the free space and its text ellipsizes before the actions */
.n-sr.left, .n-sr.off { transform: none !important; box-shadow: none !important; margin: 0 !important; }
.n-sr.left { width: calc(100% - 152px) !important; } .n-sr.off { margin-left: 76px !important; width: calc(100% - 76px) !important; }
.n-sr .tx { flex: 1; min-width: 0; } .n-sr .tx b { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; } .n-sr > .t-cap { flex: none; }
/* chat: grouped corners, read receipt, composer states */
.t-m.in:not(.last) .t-file { border-bottom-left-radius: 6px; } .t-m.out:not(.last) .t-img { border-bottom-right-radius: 6px; }
.t-m.out:not(.last) + .t-m.out .t-b { border-top-right-radius: 6px; }
.t-rd { display: inline-flex; align-items: center; gap: 3px; color: var(--hd-info-strong); }
.t-field .t-txt { font-size: 15px; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }
.t-field { transition: none; } .t-field.on { border-color: var(--hd-border-strong, var(--hd-border-input)); }
.t-comp .btn.t-send[disabled] { background: var(--hd-control) !important; color: var(--hd-fg-subtle) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.12)) !important; box-shadow: none !important; opacity: 1 !important; }
.t-comps .t-comp:first-child { border-top: 0; }
[data-theme="dark"] .t-file .x-tile { background: var(--hd-surface); }
/* nw6/nw9: .t-body is the chat scroll area; inside empty/success cards it is body copy */
.n-page .t-body, .n-ea .t-body { background: none !important; padding: 0 !important; display: block; align-self: auto; }
.n-g4 { align-items: stretch !important; } .n-g4 > .box { display: flex; flex-direction: column; } .n-g4 > .box > .n-page { flex: 1; }
.n-page .n-sum { margin-top: 8px; }
/* chat: avatar sits on the bubble's bottom edge, meta stays beneath */
.t-m.hm .t-av { margin-bottom: 20px; }
.t-av .av { width: 28px; height: 28px; font-size: 11px; }
.t-av .av, .t-head .av { color: #4a3300; }
[data-theme="dark"] .t-av .av, [data-theme="dark"] .t-head .av { color: #2a1d00; }
.t-b { overflow-wrap: anywhere; }
.t-typ { display: flex; align-items: center; gap: 4px; height: 39px; padding: 0 14px !important; }
.t-typ i { width: 6px; height: 6px; border-radius: 50%; background: var(--hd-fg-subtle); }
.t-typ i:nth-child(2) { opacity: .65; } .t-typ i:nth-child(3) { opacity: .35; }
.t-m.in .t-typ { border-bottom-left-radius: 6px; }
.t-meta { line-height: 16px; }
.t-file { min-width: 0; width: 300px; max-width: 100%; }
.t-thr .t-body { gap: 4px; }
/* empty-with-action icon: white tile with hairline, not a grey slab */
.n-eai { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); box-shadow: 0 1px 2px rgba(16,20,38,.06), 0 2px 6px rgba(16,20,38,.04); }
[data-theme="dark"] .n-eai { background: var(--hd-surface-raised) !important; }
.n-dvprof > div { min-width: 0; } .n-vrow { flex-wrap: nowrap; white-space: nowrap; }

/* product card: lighter scrims so the photo stays a photo */
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(10,12,18,.86) 0%, rgba(10,12,18,.68) 34%, rgba(10,12,18,0) 64%, rgba(10,12,18,0) 68%, rgba(10,12,18,.66) 100%) !important; }
/* media: 3-photo mosaic, no counter + dots together */
.m-mos { grid-template-columns: repeat(3, 1fr) !important; aspect-ratio: 3 / 2 !important; }
/* share sheet in a clean frame, no fake page behind it */
.n-shd.n-shclean { height: auto !important; padding: 16px; border-radius: 16px; background: var(--hd-bg-subtle); border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); }
.n-shclean .n-shs { position: relative !important; border-radius: 20px !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.12)); box-shadow: 0 8px 24px rgba(16,20,38,.08); }
[data-theme="dark"] .n-shclean .n-shs { box-shadow: 0 8px 24px rgba(0,0,0,.4); }
/* swipe rows: the row narrows to the free space and its text ellipsizes before the actions */
.n-sr.left, .n-sr.off { transform: none !important; box-shadow: none !important; margin: 0 !important; }
.n-sr.left { width: calc(100% - 152px) !important; } .n-sr.off { margin-left: 76px !important; width: calc(100% - 76px) !important; }
.n-sr .tx { flex: 1; min-width: 0; } .n-sr .tx b { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; } .n-sr > .t-cap { flex: none; }
/* chat: grouped corners, read receipt, composer states */
.t-m.in:not(.last) .t-file { border-bottom-left-radius: 6px; } .t-m.out:not(.last) .t-img { border-bottom-right-radius: 6px; }
.t-m.out:not(.last) + .t-m.out .t-b { border-top-right-radius: 6px; }
.t-rd { display: inline-flex; align-items: center; gap: 3px; color: var(--hd-info-strong); }
.t-field .t-txt { font-size: 15px; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; min-width: 0; }
.t-field { transition: none; } .t-field.on { border-color: var(--hd-border-strong, var(--hd-border-input)); }
.t-comp .btn.t-send[disabled] { background: var(--hd-control) !important; color: var(--hd-fg-subtle) !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.12)) !important; box-shadow: none !important; opacity: 1 !important; }
.t-comps .t-comp:first-child { border-top: 0; }
[data-theme="dark"] .t-file .x-tile { background: var(--hd-surface); }
/* horizontal product card: flush photo, one tight column, Apply centred */
.card.n-ph2 { display: flex; align-items: stretch; gap: 0 !important; padding: 0 !important; overflow: hidden; min-height: 112px; }
.card.n-ph2 > img { width: 112px !important; height: auto !important; min-height: 112px; border-radius: 0 !important; object-fit: cover; flex: none; }
.n-ph2 .n-hb { flex: 1; min-width: 0; display: flex; flex-direction: column; justify-content: center; gap: 2px !important; padding: 12px 12px 12px 16px !important; }
.n-ph2 .n-hbr { display: inline-flex; align-items: center; gap: 4px; font-size: 13px; line-height: 18px; color: var(--hd-fg-muted); }
.n-ph2 .n-hpt { font-size: 17px; line-height: 22px; font-weight: 600; letter-spacing: -0.01em; color: var(--hd-fg); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.n-ph2 .n-hee { font-size: 14px; line-height: 20px; color: var(--hd-fg-muted); } .n-ph2 .n-hee b { color: var(--hd-fg); font-weight: 650; }
.n-ph2 .n-hlf { font-size: 13px; line-height: 18px; color: var(--hd-fg-subtle); }
.n-ph2 .n-he { display: flex !important; flex-direction: row !important; align-items: center !important; justify-content: center !important; padding: 0 16px 0 0 !important; }
.n-ph2 .n-he .btn { margin: 0 !important; }
.n-swr > .row.n-sr.off { margin-left: 76px !important; }
.n-pc .n-brand, .n-pc .n-pt, .n-pc .n-meta { text-shadow: 0 1px 2px rgba(0,0,0,.35); }
.t-img { width: 240px; height: 180px; border-radius: 18px !important; border: 1px solid var(--hd-edge, rgba(16,20,38,.14)); box-sizing: border-box; }
.t-m.out:not(.last) .t-img { border-bottom-right-radius: 6px !important; }
.t-m.in .t-meta { padding-left: 14px; } .t-m.out .t-meta { padding-right: 14px; }
.t-comps { margin-bottom: 4px; }

/* lead: bottom scrim starts earlier so the slot line + action sit on dark; track visible on white photos */
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(10,12,18,.86) 0%, rgba(10,12,18,.66) 34%, rgba(10,12,18,0) 60%, rgba(10,12,18,.10) 66%, rgba(10,12,18,.78) 100%) !important; }
.card.n-pc .n-line { background: rgba(255,255,255,.28) !important; height: 3px !important; border-radius: 3px; }

/* ===== lead fixes: share sheet, dividers, empty-with-action ===== */
/* share sheet = a phone-width sheet, centred in its demo */
.n-shd.n-shclean { display: flex; justify-content: center; padding: 20px 16px 0 !important; overflow: hidden; }
.n-shclean .n-shs { width: 390px; max-width: 100%; border-radius: 24px 24px 0 0 !important; border-bottom: 0 !important; padding: 8px 16px 24px !important; gap: 16px !important; box-shadow: 0 -1px 0 var(--hd-edge), 0 -8px 24px rgba(16,20,38,.06) !important; }
.n-shclean .n-shh { display: flex; align-items: center; justify-content: space-between; }
.n-shclean .n-shh .t-h2 { font-size: 17px !important; font-weight: 600; }
.n-shclean .n-shx { width: 30px !important; height: 30px !important; }
.n-shclean .n-shp { border: 0 !important; padding: 0 !important; background: none !important; gap: 12px; }
.n-shclean .n-shp img { width: 44px !important; height: 44px !important; border-radius: 8px !important; }
.n-shclean .n-shp b { font-size: 15px; font-weight: 600; } .n-shclean .n-shp span { font-size: 13px !important; }
.n-shclean .n-apps { gap: 0 !important; padding: 4px 0; border-top: 1px solid var(--hd-edge); border-bottom: 1px solid var(--hd-edge); padding: 14px 0 !important; }
.n-shclean .n-app { width: 52px !important; height: 52px !important; border-radius: 14px !important; }
.n-shclean .n-apps small { font-size: 12px; margin-top: 2px; }
.n-shclean .n-shg { background: var(--hd-bg-subtle) !important; border: 0 !important; border-radius: 14px !important; }
.n-shclean .n-shg .gi { height: 48px !important; background: none !important; border-top: 0 !important; position: relative; }
.n-shclean .n-shg .gi + .gi::before { content: ''; position: absolute; top: 0; left: 46px; right: 0; height: 1px; background: var(--hd-edge); }
.n-shclean .n-shg .gi b { font-size: 15px; font-weight: 500; }
[data-theme="dark"] .n-shclean .n-shs { box-shadow: 0 -1px 0 var(--hd-edge), 0 -8px 24px rgba(0,0,0,.35) !important; }
/* dividers: single 1px hairlines, even rhythm */
.n-dvi + .n-dvi::before { height: 1px !important; background: var(--hd-edge) !important; left: 48px !important; }
.n-dvl .n-dvi { height: 48px; }
.n-dvfeed { gap: 0 !important; } .n-dvfeed .n-hrl { height: 28px; margin-top: 6px; } .n-dvfeed .n-hrl:first-child { margin-top: 0; }
.n-dvfeed .n-dvr { height: 40px !important; }
.n-dvprof { display: flex; align-items: center; gap: 12px; } .n-dvprof img { width: 48px !important; height: 48px !important; border-radius: 50%; object-fit: cover; }
.n-dvprof b { font-size: 15px; } .n-vrow { display: flex; align-items: center; gap: 10px; margin-top: 2px; font-size: 13px; color: var(--hd-fg-muted); } .n-vrow b { font-size: 13px; color: var(--hd-fg); font-weight: 600; } .n-vr { width: 1px; height: 12px; background: var(--hd-edge); display: inline-block; }
.n-dvbreak { border-top: 1px solid var(--hd-edge) !important; }
.n-dvbreak .n-dvr { height: 44px !important; font-size: 14px; }
.n-band2 { height: 8px; background: var(--hd-bg-subtle); border-top: 1px solid var(--hd-edge); border-bottom: 1px solid var(--hd-edge); }
.n-dvbreak .n-band { display: none !important; }
/* empty with action: compact, one message, numbered strip, balanced actions */
.card.n-ea.n-ea3 { gap: 0 !important; padding: 32px 24px 28px !important; }
.n-ea3 img { width: 104px !important; height: 104px !important; margin-bottom: 16px; }
.n-ea3 .t-h2 { font-size: 20px !important; line-height: 26px; }
.n-eap { margin: 6px 0 0; max-width: 380px; font-size: 14.5px; line-height: 21px; color: var(--hd-fg-muted); text-wrap: pretty; }
.n-steps3 { list-style: none; margin: 20px 0 0; padding: 0; display: flex; gap: 0; border: 1px solid var(--hd-edge); border-radius: 12px; overflow: hidden; }
.n-steps3 li { display: flex; align-items: center; gap: 8px; padding: 10px 14px; font-size: 13px; font-weight: 500; color: var(--hd-fg); white-space: nowrap; }
.n-steps3 li + li { border-left: 1px solid var(--hd-edge); }
.n-steps3 i { font-style: normal; width: 20px; height: 20px; border-radius: 50%; display: grid; place-items: center; font-size: 11.5px; font-weight: 600; background: var(--hd-accent-subtle); color: var(--hd-accent-strong); font-variant-numeric: tabular-nums; }
.n-eab { display: flex; gap: 10px; margin-top: 20px; justify-content: center; } .n-eab .btn { height: 44px; }

.n-shclean .n-shg { background: var(--hd-surface) !important; border: 1px solid var(--hd-edge) !important; border-radius: 14px !important; box-shadow: 0 1px 2px rgba(16,20,38,.05) !important; }
.n-shclean .n-shg .gi + .gi::before { background: var(--hd-edge) !important; left: 46px; }
.n-shclean .n-shg .gi .ic { color: var(--hd-fg) !important; }
[data-theme="dark"] .n-shclean .n-shg { background: var(--hd-surface-raised) !important; box-shadow: none !important; }

/* product card v4: photo stays full colour; content sits on short progressive-blur bands (top + bottom), no grey wash */
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(8,10,16,.62) 0%, rgba(8,10,16,.34) 24%, rgba(8,10,16,0) 42%, rgba(8,10,16,0) 66%, rgba(8,10,16,.40) 84%, rgba(8,10,16,.66) 100%) !important; z-index: 1; }
.card.n-pc > .n-ph::before { content: ''; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  -webkit-backdrop-filter: blur(14px) saturate(1.1); backdrop-filter: blur(14px) saturate(1.1);
  -webkit-mask-image: linear-gradient(180deg, #000 0%, #000 20%, transparent 38%, transparent 70%, #000 86%, #000 100%);
  mask-image: linear-gradient(180deg, #000 0%, #000 20%, transparent 38%, transparent 70%, #000 86%, #000 100%); }
.card.n-pc .n-pb { position: relative; z-index: 2; }
.card.n-pc .n-pt, .card.n-pc .n-meta, .card.n-pc .n-brand, .card.n-pc .n-pb b { text-shadow: 0 1px 1px rgba(0,0,0,.25) !important; }
.card.n-pc .n-line { background: rgba(255,255,255,.30) !important; }

.card.n-pc > .n-ph > img { position: relative; z-index: 0; }
.card.n-pc > .n-ph::before { z-index: 1 !important; }
.card.n-pc > .n-ph::after { z-index: 1 !important; background: linear-gradient(180deg, rgba(8,10,16,.72) 0%, rgba(8,10,16,.48) 22%, rgba(8,10,16,.12) 36%, rgba(8,10,16,0) 44%, rgba(8,10,16,0) 66%, rgba(8,10,16,.42) 82%, rgba(8,10,16,.70) 100%) !important; }

.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(8,10,16,.80) 0%, rgba(8,10,16,.58) 24%, rgba(8,10,16,.16) 38%, rgba(8,10,16,0) 46%, rgba(8,10,16,0) 66%, rgba(8,10,16,.42) 82%, rgba(8,10,16,.70) 100%) !important; }
.card.n-pc .n-meta { font-weight: 500 !important; color: rgba(255,255,255,.92) !important; }

/* ===== product card v5 (final): clean full-colour photo, content anchored bottom on one smooth scrim; no blur, no top wash ===== */
.card.n-pc > .n-ph::before { display: none !important; }
.card.n-pc > .n-ph::after { background: linear-gradient(180deg, rgba(8,10,16,.18) 0%, rgba(8,10,16,0) 16%, rgba(8,10,16,0) 38%, rgba(8,10,16,.38) 54%, rgba(8,10,16,.74) 72%, rgba(8,10,16,.90) 100%) !important; }
.card.n-pc .n-pb { padding-top: 0 !important; justify-content: flex-end !important; flex: 1 1 auto !important; margin-top: 0 !important; }
.card.n-pc .n-pb > .n-line { margin-top: 12px !important; margin-bottom: 14px !important; }
.card.n-pc .n-pt { font-size: 22px !important; line-height: 27px !important; margin-top: 2px !important; }
.card.n-pc .n-meta { margin-top: 4px !important; font-size: 14px !important; color: rgba(255,255,255,.86) !important; font-weight: 450 !important; }
.card.n-pc .n-meta b { color: #fff; font-weight: 650; }
.card.n-pc .n-pt, .card.n-pc .n-meta, .card.n-pc .n-pb b { text-shadow: none !important; }

/* ===== full-bleed media (v5 pattern): photo covers the card, one smooth bottom scrim, text anchored at the bottom ===== */
.m-reel::before, .m-yt::before { display: none !important; }
.m-reel::after, .m-yt::after { height: 62% !important; background: linear-gradient(to top, rgba(8,10,16,.90) 0%, rgba(8,10,16,.74) 34%, rgba(8,10,16,.38) 68%, rgba(8,10,16,0) 100%) !important; }
.m-reelw { gap: 0; }
.m-reel .m-meta { gap: 6px; left: 14px; right: 14px; bottom: 14px; }
.m-reel .m-cap { margin: 0; color: #fff; font-size: 14px; line-height: 19px; }
.m-reel .m-views { color: rgba(255,255,255,.80); }
.m-dur { background: rgba(13,14,18,.72); }
.m-yt .m-dur { top: 12px !important; bottom: auto !important; right: 12px; }
.m-yt .m-ytb { position: absolute; left: 20px; right: 20px; bottom: 18px; z-index: 2; align-items: center; color: #fff; }
.m-yt .m-ytb b { color: #fff; font-size: 17px; line-height: 22px; } .m-yt .m-ytb .t-small { color: rgba(255,255,255,.82); display: flex; align-items: center; gap: 4px; }
.m-yt .m-av.l { width: 40px; height: 40px; }
"""
