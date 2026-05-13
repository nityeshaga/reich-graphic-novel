# Project Brief — Reich Graphic Novel

## What This Is

A full-length educational graphic novel that teaches Nityesh genetics from the ground up while walking him through David Reich's first appearance on the Dwarkesh Podcast: *"How one small tribe conquered the world 70,000 years ago."*

The genetics education and the interview's narrative are woven together — you learn each concept exactly when the interview demands it. This is NOT a textbook + interview summary. It's a journey where you start knowing nothing about genetics and end understanding one of the most fascinating conversations about human origins.

## Origin Story

Nityesh has been fascinated by two things: genetics and ancient history. This Dwarkesh episode sits at the intersection — and it's one of Dwarkesh's most popular episodes. But Nityesh couldn't follow it. He doesn't remember high school genetics, and the interview assumes background knowledge he doesn't have. After keeping it on the shelf for a few months, AI finally became competent enough to be a personal tutor. So here we are — Helix, the DNA character guide, will answer all his "dumb" questions as they walk through this epic interview together.

## Source Material

- **Primary:** Full transcript of Dwarkesh Podcast x David Reich (first appearance) — `source-transcript.md`
- **Secondary:** David Reich's book "Who We Are and How We Got Here" — referenced where it adds context beyond the podcast, but the podcast is the narrative spine

## Characters (finalized)

### 1. Helix — The Genetics Guide
- **What:** Small, friendly, anthropomorphic double-helix DNA strand mascot
- **Look:** Coral/salmon pink strands with teal/cyan rungs (base pairs). Expressive cartoon eyes, stubby arms and legs. Standard comic style (not pixel-art).
- **Role:** Genetics 101 guide. Pops in whenever a concept needs explaining. Think of Helix as the friendly science tutor who appears in sidebar panels or teaching moments.
- **Tone:** Approachable, curious, slightly nerdy
- **Reference:** `characters/helix-concept.png`

### 2. Nityesh — The Curious Learner
- **What:** The reader's avatar, based on Nityesh's real appearance
- **Look:** Pixel-art style. Young Indian man with distinctive big curly black hair, rectangular glasses, light stubble, white t-shirt, beaded necklace.
- **Role:** Asks the questions the reader is thinking. Not afraid to say "wait, what does that mean?" Reacts with genuine curiosity, confusion, and mind-blown moments.
- **Reference:** `characters/nityesh-cartoon-v2.png` (source photo: `characters/nityesh-headshot.jpg`)

### 3. David Reich — The Professor
- **What:** Cartoon version of the real David Reich, Harvard geneticist
- **Look:** Head and shoulders only (no full body). Middle-aged, short brown receding hair, blue collared shirt. Warm, enthusiastic academic energy.
- **Role:** Shares his findings with genuine excitement. The teacher you wish you had.
- **Reference:** `characters/reich-cartoon-v2.png`

### 4. No Dwarkesh Character
- His interview questions appear as text prompts or caption boxes
- Adding a third human character would make consistency harder across 20+ pages
- Nityesh already fills the "curious questioner" role

## Creative Decisions

### Opening (Page 1)
- Opens on Nityesh putting on headphones, pressing play on the podcast
- Establishes: "I've been fascinated by genetics and ancient history. This episode sits at the intersection. One of Dwarkesh's most popular episodes. But I couldn't follow it."
- "After months on the shelf, AI was finally competent enough to be my personal tutor. So here we are."
- Introduces Helix as the study companion

### Tone & Voice
- Structured as Nityesh sitting down with the podcast, with Helix as his study companion
- When Reich explains something complex, Nityesh pauses: "wait, what does that mean?" — Helix jumps in with the primer
- Three registers:
  - **Helix teaching moments** — warm, clear, slightly playful science explainer
  - **Reich presenting findings** — enthusiastic academic sharing breakthroughs
  - **Nityesh reacting** — genuine curiosity, confusion, aha moments, mind-blown reactions
- NOT a dry textbook. NOT dumbed-down. An intelligent person learning something new with a great guide.

### Visual Style
- Clean comic book illustration, thick outlines, bright colors
- Nityesh rendered in pixel-art style (chunkier, retro game aesthetic)
- Helix and Reich in standard comic style
- Pages: 2048x1440px landscape, 4-column x 2-row grid format

### Scope
- **No page limit.** As long as it needs to be — potentially 20-40+ pages
- Every major concept from the interview gets covered
- Genetics basics taught inline, not front-loaded
- The book is referenced where it adds depth, but the interview is the spine

## Visual Design Rules

### Helix Primer Pages vs Interview Pages
The Helix teaching moments (where Nityesh pauses the podcast and Helix explains a concept) must feel visually DISTINCT from the main interview pages:
- **Interview pages:** Clean white/cool background, rigid 4x2 grid, comic book style. The podcast is playing.
- **Helix primer pages:** Warm cream/chalkboard background tone, freeform layout (less rigid grid), Helix drawing diagrams and annotations. Feels like the podcast is paused and you've stepped into a side room with your tutor. "Whiteboard mode" vs "comic mode."

### Page-Turn Captivation
Every page must end with a hook that creates genuine "I need to know what happens next" energy. Not transitional connective tissue — real curiosity. Vary the rhythm: dense teaching page → dramatic revelation page → quiet character moment → bombshell. A great graphic novel controls reading speed through pacing.

### Independent Review Gate
Before generating any page image, the page spec goes through TWO independent reviews:

**Judge 1 — Quality & Consistency:**
- Visual consistency with ALL prior page specs (character descriptions, style, color palette)
- Whether illustration ideas push beyond obvious/generic choices
- Whether the teaching is accurate for someone with zero genetics background
- Overall captivation and storytelling quality

**Judge 2 — Reader Pace:**
A first-time reader with zero genetics background, checking: "Could I follow this at reading speed?"
- **Concept load:** Max 2 genuinely new ideas per page. Dense panels are fine — dense concepts per page are not.
- **Transition quality:** Pages must flow through character-driven curiosity (Nityesh reacting, wondering), NOT by naming the next section in the final panel. Title-card hooks = automatic reject.
- **Breathing room:** Every page needs at least one panel where Nityesh reacts, processes, or asks a question. Pure exposition with zero character response = reject.

No page gets generated until it passes BOTH reviews.

## Key Topics from the Interview

These are the major threads that will need genetics primers woven in:

1. **Archaic vs modern humans** — what makes us "modern," Neanderthals, Denisovans
2. **DNA basics** — what DNA is, how it's inherited, nuclear vs mitochondrial vs Y chromosome
3. **Gene flow / admixture** — how DNA moves between populations, what "2% Neanderthal" means
4. **Ancient DNA techniques** — how you extract and sequence DNA from 50,000-year-old bones
5. **Out of Africa** — the "one small tribe" story, population bottleneck
6. **Mitochondrial DNA vs nuclear DNA** — why they tell different stories
7. **Natural selection** — how it shapes populations, selective advantage
8. **Population genetics** — allele frequencies, drift, founder effects
9. **Epigenetics / methylation** — the FOXP2 / vocal tract discovery
10. **The Ptolemy epicycles metaphor** — how scientific models accumulate patches
11. **Bubonic plague / Yersinia pestis** — disease reshaping history
12. **Yamnaya expansion** — steppe people replacing European farmers
13. **The India story** — ANI/ASI mixture, implications
14. **Two-step migration patterns** — male/female dynamics in population replacement
15. **The "are we even modern humans?" question** — 10-20% Neanderthal ancestors vs 2% DNA
