# Reich Graphic Novel

An educational graphic novel that teaches genetics from basics while walking through David Reich's first appearance on the Dwarkesh Podcast ("How one small tribe conquered the world 70,000 years ago"). The genetics education is woven into the interview's narrative — you learn what you need exactly when the interview demands it.

## Status

**Phase:** 3 in progress (Art Direction / page specs + generation)
**Scope:** 20 chapters, ~79 pages, 6 parts
**Storyboard:** `storyboard-v3.md` (final)

### Pages completed:
- page-00-prologue.png — DONE (Prologue)
- page-01-the-molecule.png — DONE (Ch1 P1)
- page-02-central-dogma.png — DONE v3 (Ch1 P2, includes protein shake moment)
- page-03-inheritance.png — DONE (Ch1 P3)
- page-04-mutations.png — DONE (Ch1 P4)
- page-77-the-return.png — DONE (Epilogue P1)
- page-78-helix-goodbye.png — DONE (Epilogue P2)

**Next up:** Chapter 2 (How Life Copies Itself — DNA replication, meiosis, recombination)

## Production Pipeline

This project uses the zine/comic creation skill from `~/.claude/plugins/cache/claude-home-base/creative/1.2.0/skills/create-zine-comic/`. Read that skill's SKILL.md for the full pipeline — 5 phases with quality gates.

Key reference files for page spec quality:
- `~/.claude/plugins/cache/claude-home-base/creative/1.2.0/skills/create-zine-comic/references/` — 6 reference page specs showing different page types

## Characters

Three characters, reference sheets in `characters/`:

| Character | File | Role | Description |
|-----------|------|------|-------------|
| **Helix** | `characters/helix-concept.png` | Genetics guide / mascot | Small, friendly, anthropomorphic double-helix DNA strand. Coral/salmon pink strands with teal/cyan rungs (base pairs). Expressive cartoon eyes, stubby arms and legs. Pops in whenever a genetics concept needs explaining. Approachable, curious, slightly nerdy. |
| **Nityesh** | `characters/nityesh-cartoon-v2.png` | The curious learner | Pixel-art style. Young Indian man with distinctive big curly black hair, rectangular glasses, light stubble, white t-shirt, beaded necklace. Asks the "dumb" questions. Reference photo: `characters/nityesh-headshot.jpg` |
| **David Reich** | `characters/reich-cartoon-v2.png` | The professor / teacher | Head and shoulders only (no full body). Middle-aged, short brown receding hair, blue collared shirt. Warm, enthusiastic academic energy. Shares findings with genuine excitement. |

**Character consistency rules:**
- Copy-paste the EXACT same character description block into every page spec. Never rephrase — the image model treats variations as different characters.
- Always pass character reference images with `--image` flag during generation.
- Helix's description and Nityesh's pixel-art style must remain identical across all pages.

## Image Generation

```bash
SCRIPTS_DIR="/Users/luo/.claude/plugins/cache/claude-home-base/more-ai/1.2.0/skills/openai-imagegen/scripts"
PYTHON="${SCRIPTS_DIR}/.venv/bin/python3"

# Generate (no input image)
$PYTHON "${SCRIPTS_DIR}/generate_image.py" "prompt" output.png --size 2048x1440 --quality medium

# Edit (with reference image)
$PYTHON "${SCRIPTS_DIR}/edit_image.py" "prompt" output.png --image ref.png --size 2048x1440 --quality medium
```

- Use `medium` quality for iteration, `high` for final versions
- Pages are 2048x1440px landscape
- OPENAI_API_KEY is available as an environment variable

## Source Material

- `source-transcript.md` — Full transcript of Dwarkesh Podcast x David Reich (first appearance)
- David Reich's book: "Who We Are and How We Got Here" — reference for context beyond what the podcast covers

## Directory Structure

```
characters/          # Character reference sheets
  helix-concept.png
  nityesh-cartoon-v2.png
  nityesh-headshot.jpg
  reich-cartoon-v2.png
source-transcript.md # The podcast transcript
project-brief.md     # All creative decisions from Phase 1
pages/               # Page specs (markdown) — one file per page
output/              # Generated page images
```

## GitHub Pages Reader

**Live at:** https://nityeshaga.github.io/reich-graphic-novel/
**Repo:** https://github.com/nityeshaga/reich-graphic-novel

The reader is a static `index.html` — swipe/arrow-key navigation, table of contents, progress bar, remembers position. Optimized for iPad.

**After generating new pages:** The reader auto-discovers PNGs from `output/` at build time via a GitHub Actions workflow that generates a `pages.json` manifest. Just commit new images to `output/` and push — the reader updates automatically.

**Deployment:** GitHub Pages via `.github/workflows/deploy.yml`. Pushes to `main` trigger a rebuild.

## Key Decisions

- No page limit — this will be a full graphic novel, as long as it needs to be
- Genetics 101 is taught inline, not as a separate section — Helix explains basics as the interview demands them
- No Dwarkesh character — his questions appear as text/captions; Nityesh fills the "curious questioner" role
- Skip Dwarkesh as a character to reduce consistency complexity across 20+ pages
- Visual style: clean comic book illustration, thick outlines, bright colors
- Nityesh is pixel-art style; Helix and Reich are standard comic style
