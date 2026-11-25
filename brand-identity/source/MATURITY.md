# Maturity bar (owner, 2026-11-26): "make all pages fully mature"

The owner judged these three as the standard. Study them before touching anything:
- Creator Home: ~/Downloads/hypedrive-wordmark/BRAND/ui/screens/03-home.png (code: s_home in kit_build.py, xh.py)
- Brand Wallet: ~/Downloads/hypedrive-wordmark/BRAND/ui/hypedrive-desktop-6.png (code: d_wallet in desk_b2.py, `bw-` rules in xb2.py)
- Mediator TrustDrive: ~/Downloads/hypedrive-wordmark/BRAND/ui/screens/27-m-trustdrive.png (code: s_m_trust in mob_m.py)

Pages the owner called "ugly", "cluttered" or "not mature" all broke the same rules. Every page must pass this list.

## Structure
1. **Each card has one job and one hero.**
   - At most one big number per card.
   - Supporting figures go in ONE muted sentence ("₹96,320 on hold · …"), not in stat tiles, mini-tables or multi-column strips.
2. **Mark only the exceptions.**
   - The normal state carries no badge, pill or colour: Paid, Credited, Live and Verified are the norm.
   - Only what needs attention gets the warning colour or text (Void, Fix tasks, Pay back, Due).
3. **One signal per state.**
   - Never a pill AND a sentence AND a colour for the same fact.
   - If a section heading says "Your turn", the rows don't repeat it.
4. **One row style per list.**
   - Lead (icon tile, round avatar or square thumb, consistent within the list), title 15/600, ONE muted meta line, and an optional trailing value or ONE quiet action.
   - Never mix tile rows, star rows and button rows in one list.
5. **Actions are quiet unless primary.**
   - One primary button per screen or section.
   - Row actions are text links (color var(--hd-link), 600) or one small secondary.
   - No bordered buttons repeated down a list.
   - Put actions where the thing is (balance actions inside the balance card).
6. **No dead space and no cramming.**
   - Equal columns, full-width actions, and no half-empty wide cards.
   - Nothing truncated mid-word, no two-line labels in small tiles, no 5-column micro-stat strips.
7. **Ledgers are allowed as joined lists.**
   - Ledgers and statements (activity, invoices, TDS) can be one card with hairline rows.
   - Other data lists are separate rounded cards with gaps.
8. **No decoration.**
   - No icon tiles that only repeat the label, and no sparklines, charts, star strings, legends or dividers that carry no information.
   - No chevrons on rows unless the row navigates and nothing else signals it.

## Type and rhythm
- **Fonts:**
  - Page title: var(--font-brand) 28/32 (desktop 30–32) 700.
  - Section heading: var(--font-brand) 17–18/650.
  - Big number: var(--font-brand) 34–40/700.
  - Everything else: var(--font-ui) (Allo).
- **Row text:** title 15/600 (desktop 14.5/600), meta 13/18 muted, caption 12.5.
- **Spacing:**
  - Phone canvas padding 16; card padding 14–16 (desktop 20–24).
  - Gaps: 12 between cards, 8–10 between rows of a list, 20 between desktop sections.
- **Numbers:** Indian grouping, ₹ with no space, U+2212 minus; tabular figures where they align.

## Colour and surfaces
- Colours only via the --hd-* tokens: cobalt accent, deepened -subtle tints.
- Green only for money in. Warning only for something due or wrong. Red only for a final destructive confirm.
- No tinted borders, glows, grey slabs or heavy coloured discs. White cards with a 1px var(--hd-edge) on the var(--hd-canvas) background.

## Data
- Never invent concepts.
- Vocabulary and numbers come from CREATOR-SPEC.md, BRAND-SPEC.md and MEDIATOR-SPEC.md, and must agree across screens.

## Light and dark
- Every page must hold in dark: no invisible edges, no hard-coded light colours.
- Check dark by rendering a temporary copy with data-theme="dark" on the screen, or with the screen's theme param where one exists.
