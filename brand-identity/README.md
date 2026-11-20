# Hypedrive brand identity: working archive (Nov 2026)

This is the full brand-identity and design-system work, kept here so the rebrand can restart from this point.

**Start with `wordmark/BRAND/HANDOFF.md`.** Section 9 lists the final decisions, the rules the owner set, and the mistakes not to repeat.

## Layout
| Path | What it is |
|---|---|
| `wordmark/BRAND/Hypedrive-Brand-Guidelines.pdf` / `.html` | The brand book (97 pages). **Final = the "colourful" version**, debugged and refined. |
| `wordmark/BRAND/ui/` | UI kit (light and dark), 12 mobile screens, 4 desktop pages, icon and illustration sheets, comparison boards |
| `wordmark/BRAND/assets/` | Exported logos, favicons, app icons, packaging, labels, merch, social, campaign, motifs, patterns, print |
| `wordmark/BRAND/tokens/` | `colors.css`, `tokens.json`, type tokens |
| `wordmark/BRAND/versions/` | `current-colourful/` (approved), `calm-0711/` (rejected), `original-baseline.pdf`, `compare.html` |
| `wordmark/` (other folders) | Logo and wordmark explorations: concepts, refined, final-box, isometric, packages |
| `source/` | Python/JS generators for the book, UI kit, screens, icons and isometric illustrations, plus the CSS layers, `BRIEF.md` (rules for agents) and `requirements.txt` |

## Rebuilding
- The scripts assume the working directory `/tmp/hdwm` (sources) and `~/Downloads/hypedrive-wordmark/BRAND` (outputs). Copy `source/` to `/tmp/hdwm` and `wordmark/` to `~/Downloads/hypedrive-wordmark`, or update the path constants at the top of `uikit.py` and `brand.py`.
- Python: create a venv and run `pip install -r source/requirements.txt`.
- Commands:
  - UI kit and screens: `python -I kit_build.py && bash render_ui.sh`
  - Brand book: `python -I brand.py` (see the bottom of the file for the PDF step)
- **The Nucleo icon data is not included.** `nucleo_outline.json` / `nucleo_fill.json` hold licensed Nucleo UI icons, which must not be redistributed. To regenerate them, run `nucleo_extract.py` / `nucleo_fill.py` against your licensed Nucleo package. The rendered HTML/PNG already contain the icons as drawn.

## Not final
- `source/xw*.py` belong to the rejected "Direction A" (Geist-only display, warm canvas). They are not loaded by `kit_build.py`. Kept for reference only.
