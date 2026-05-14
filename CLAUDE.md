# Reich Graphic Novel

An educational graphic novel that teaches genetics from basics while walking through David Reich's first appearance on the Dwarkesh Podcast ("How one small tribe conquered the world 70,000 years ago"). The genetics education is woven into the interview's narrative — you learn what you need exactly when the interview demands it.

## Status

**Phase:** 3 in progress (Art Direction / page specs + generation)
**Scope:** 21 chapters + 6 intro pages, ~120 pages, 6 parts
**Storyboard:** `storyboard-v4.md` (current — expanded pacing, 4-8 pages per chapter, natural transitions)

### Pages completed (v4 storyboard — 33 pages, clean 00-32 sequence):

**Part I — THE LANGUAGE OF LIFE (fully generated):**
- 00: Prologue | 01: Part I Intro
- 02-06: Chapter 1 — The Molecule (5 pages)
- 07-13: Chapter 2 — Your Parents' Gift (7 pages — split Symphony of Genes into Polygenic Traits + Allele Frequency)
- 14-19: Chapter 3 — When the Code Changes (6 pages)
- 20-25: Chapter 4 — How Life Copies Itself (6 pages)

**Remaining (intros + epilogue from v3, renumbered):**
- 26: Part II Intro | 27: Part III Intro | 28: Part IV Intro | 29: Part V Intro
- 30: Epilogue Intro | 31-32: Epilogue (2 pages)

**Next up:** Chapter 5 — Three Histories in Your Body (Part I, Ch5, 6 pages, starts at page 26 — will push intros/epilogue numbering further)

**Note:** v3 pages archived in `output/archive-v3/` and `pages/archive-v3/`

### Panel Grid System
Every page uses a **4-column × 2-row grid = 8 slots** as the base structure. Panels can merge adjacent slots horizontally for wider compositions. Each slot = one beat (visual moment, dialogue, diagram, or reaction). Most pages end up with 5-7 visible panels. Full-width merges signal big moments; single slots signal beats or reactions.

## Production Pipeline

This project uses the zine/comic creation skill from `~/.claude/plugins/cache/claude-home-base/creative/1.2.0/skills/create-zine-comic/`. Read that skill's SKILL.md for the full pipeline — 5 phases with quality gates.

Key reference files for page spec quality:
- `~/.claude/plugins/cache/claude-home-base/creative/1.2.0/skills/create-zine-comic/references/` — 6 reference page specs showing different page types

### Review Judges

Every page spec goes through TWO independent reviews before image generation:

**Judge 1 — Quality & Consistency Review** (existing):
- Visual consistency with ALL prior page specs (character descriptions, style, color palette)
- Whether illustration ideas push beyond obvious/generic choices
- Whether the teaching is accurate for someone with zero genetics background
- Overall captivation and storytelling quality

**Judge 2 — Reader Pace Review** (new):
A first-time reader with zero genetics background, checking ONE question: **"Could I follow this at reading speed?"**
- **Concept load:** If a page introduces more than 2 genuinely new ideas, flag it. Dense panels are fine — dense *concepts* per page are not.
- **Transition quality:** Does each page flow from the previous one through *character-driven curiosity* (Nityesh reacting, asking, wondering)? If the last panel names the next section instead of raising a question the reader genuinely wants answered, REJECT.
- **Breathing room:** Are there panels where Nityesh reacts, processes, or asks a "wait, so you're saying..." question? If a page is 100% exposition with zero character response, it needs a rewrite.

No page gets generated until it passes BOTH reviews.

**DO NOT SKIP REVIEWS.** Write specs → run both judges → fix flagged issues → THEN generate images. Generating before reviewing wastes image credits and was explicitly called out by the cofounder as a process violation.

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
- Always pass BOTH character reference images: `--image characters/helix-concept.png --image characters/nityesh-cartoon-v2.png`
- **Parallel generation gotcha:** When running multiple `edit_image.py` calls in a single background Bash command with `&`, you MUST add `wait` at the end. Without it, the shell exits before the python processes finish and images silently don't get saved.

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

**CRITICAL — `build.py` is the source of truth for `pages.json`:**
The deploy workflow runs `python build.py` which regenerates `pages.json` from scratch. Any direct edits to `pages.json` will be overwritten on deploy. To change page metadata (titles, parts, chapters), edit `build.py` instead — specifically `PART_HEADERS`, `CHAPTERS`, and `TITLE_OVERRIDES` dicts.

**Reader hierarchy:** The reader displays three levels: **Part → Chapter → Page**. `build.py` maps each page (by its index in the sorted output list) to a chapter via the `CHAPTERS` dict. When adding new pages, add their chapter assignments to this dict. The bottom bar shows chapter name above page title, and the ToC groups pages under chapter headings.

**Renumbering gotcha:** Adding or splitting pages shifts ALL downstream page numbers. When this happens, you must update: (1) output PNG filenames, (2) page spec filenames in `pages/`, (3) `PART_HEADERS` and `CHAPTERS` indices in `build.py`. The indices are based on sort order of filenames in `output/`, not the page number in the filename. Run `python build.py` and inspect the output to verify.

## Key Decisions

- No page limit — this will be a full graphic novel, as long as it needs to be
- Genetics 101 is taught inline, not as a separate section — Helix explains basics as the interview demands them
- No Dwarkesh character — his questions appear as text/captions; Nityesh fills the "curious questioner" role
- Skip Dwarkesh as a character to reduce consistency complexity across 20+ pages
- Visual style: clean comic book illustration, thick outlines, bright colors
- Nityesh is pixel-art style; Helix and Reich are standard comic style

## Canonical Character Description Blocks

Copy-paste these VERBATIM into every page spec. Do not rephrase, shorten, or paraphrase.

**Nityesh:** A pixel-art style young Indian man with distinctive big curly black hair, rectangular glasses, light stubble, white t-shirt, and beaded necklace. Expressive cartoon eyes. The curly hair is his most defining visual feature — big, voluminous, immediately recognizable. Pixel-art aesthetic — visible chunky pixels, retro game feel, but clearly this specific person.

**Helix:** A small, friendly, anthropomorphic double-helix DNA strand. Coral/salmon pink strands with teal/cyan rungs (base pairs) connecting them. Expressive cartoon eyes near the top, small stubby arms and legs. Approachable, curious, slightly nerdy. Standard comic style (NOT pixel-art). About 1/4 of Nityesh's height — a small companion character.

## Lessons from v3 → v4 Rewrite

These are failure modes that actually happened. Check for them.

1. **v3 crammed too many concepts per page.** The Mendel page had 9 concepts. Max 2 per page.
2. **v3 used title-card hooks** ("Next: The Copy Machine"). Hooks must come from Nityesh's curiosity.
3. **v3 had abrupt chapter transitions.** Each chapter must bridge naturally through a question Nityesh asks at the end of the previous chapter.
4. **Review judges were skipped** in the first Ch2-4 generation run, and the cofounder caught it. The reviews found real issues (broken transition, concept overload) that required rewriting 5 pages and regenerating images. Reviews are not optional.
5. **Page spec style paragraphs were inconsistent.** Every HELIX TEACHING PAGE spec must include: "The style is polished, modern comic book — clean lines, vibrant colors, professional typography mixed with handwritten-style annotations."
