---
name: youtube-visual-prompt
description: >
  The Integrated Visual Director V1.1. Connects the Script Engine (Master V7.0) with AI Image Generators.
  Uses 'Multi-Agent Brainstorming' for creative direction and 'Prompt Engineer' for optimization.
  Generates a cohesive Storyboard with Scene Matching, Style Consistency, and Retention Hooks.
version: 1.1.0
author: Antigravity & SonPM Master Concepts
category: visual-design
tags: [midjourney, runway, prompt-engineering, storyboard, visual-style, integration]
risk: safe
---

# YouTube Visual Prompt V1.1 (The Integrated Director)

## 🎯 PURPOSE
To transform a **Text Script (Master V7.0)** into a **Visual Storyboard**.
This skill orchestrates the creative process, leveraging other skills to ensure the visuals are not just "pretty pictures" but **Psychological Retention Anchors**.

## 🔄 THE INTEGRATED WORKFLOW

### STEP 1: CONTEXT INGESTION (From Script & Profile)
- **Input:** The `Voicescript` section from `youtube-script-master`.
- **Style:** The `Visual Language` section from the `Profile Skill` (e.g., Gen Z = Dark Academia).
- **Sensory Data:** The **P-A-S-T** elements (Place, Action) marked in the script.

### STEP 2: CREATIVE DIRECTION (Brainstorming)
*Use `@[skills/multi-agent-brainstorming]` to refine the Visual Strategy if needed.*

**The 3-Agent Creative Team:**
1.  **The Director:** Focuses on emotion and pacing. "This scene needs to feel lonely."
2.  **The DoP (Director of Photography):** Focuses on lighting and angles. "Use a Dutch Angle and Low Key lighting here."
3.  **The Editor:** Focuses on retention. "Cut to a fast-paced montage here to match the Staccato rhythm."

### STEP 3: STYLE SELECTION (The Aesthetic Engine)

**OPTION A: PRESET STYLES (Ready-to-Use)**
1. **Stickman / Minimalist:** `simple line art, hand-drawn black ink on white paper, expressive stick figures, minimalist, witty`
2. **CGI / 3D Render:** `3D render, Unreal Engine 5, octane render, isometric view, plastic texture, vibrant studio lighting`
3. **Cinematic Realism:** `movie still, shot on 35mm, anamorphic lens, bokeh, dramatic lighting, color graded`
4. **Dark Academia (Gen Z):** `moody, rain-soaked window, neon reflection, lo-fi aesthetic, grain, muted colors`
5. **Vintage Illustration:** `1950s editorial illustration, textured paper, retro color palette, grainy`
6. **Abstract / Metaphor:** `surreal conceptual art, double exposure, floating objects, dreamlike, fog`

**OPTION B: CUSTOM STYLE (Clone Mode)**
- **Input:** User provides a description of an image style OR a reference URL.
- **Action:** Analyze the core visual elements (Subject + Medium + Lighting + Color Palette + Composition).
- **Output:** A "Style Suffix" to append to every prompt.

---

## 🎬 STEP 4: STORYBOARD GENERATION (SCENE MATCHING)

**The skill will generate a structured table based on script segments:**

**1. THE HOOK SHOT (0:00 - 0:10)**
- **Goal:** Visual Impact / Disruption.
- **Prompt Formula:** `[SUBJECT: Shocking element] + [ACTION: Breaking/Exploding/Staring] + [STYLE] + [LIGHTING: Dramatic/Rim]`

**2. THE METAPHOR SHOT (Body Paragraphs)**
- **Goal:** Illustrate abstract concepts (Loneliness, Success, Anxiety).
- **Prompt Formula:** `[CONCEPT: Man trapping in a glass jar] + [STYLE] + [ATMOSPHERE: Foggy/Cold]`

**3. THE B-ROLL LOOP (Backgrounds)**
- **Goal:** Subtle movement, not distracting.
- **Prompt Formula:** `[SETTING: Empty office at night] + [ACTION: Dust motes floating] + [STYLE] + --tile (for seamless patterns)`

---

## 🛠️ STEP 5: PROMPT OPTIMIZATION (FINAL POLISH)
*Use `@[skills/prompt-engineer]` frameworks (RTF/Chain of Thought) to refine syntax.*

**MIDJOURNEY (v6)**
- Format: `/imagine prompt: [Subject] [Style Suffix] --ar 16:9 --stylize 250 --v 6.0`
- Tweak: Use `--no text` to avoid gibberish text.

**RUNWAY GEN-2 (Video)**
- Format: `[Camera Move: Pan Left] [Subject] [Style]`
- Tweak: Keep prompts under 40 words for better motion consistency.

**DALL-E 3 (Illustrative)**
- Format: Natural language description. "Create a [Style] image of..."

---

## 📦 FINAL OUTPUT TEMPLATE (THE STORYBOARD)

```markdown
## 🎬 VISUAL STORYBOARD (Profile: [Name])

| Time | Script Context | Visual Idea (Metaphor/Action) | AI Prompt (Midjourney/Runway) |
| :--- | :--- | :--- | :--- |
| **0:00 (Hook)** | "[Script Text]" | **Idea:** Extreme Close-up of an eye opening in shock. | `/imagine prompt: extreme close-up of a human eye wide open, iris reflecting a digital clock, cinematic lighting, hyper-realistic, [Style Suffix] --ar 16:9` |
| **0:15 (Intro)** | "[Script Text]" | **Idea:** A lone figure walking in rain (Metaphor for loneliness). | `/imagine prompt: wide shot of a solitary silhouette walking down an empty rainy street at night, neon reflections on wet asphalt, [Style Suffix] --ar 16:9` |
| **1:30 (Body)** | "[Script Text]" | **Idea:** Time-lapse of a flower wilting (Metaphor for exhaustion). | `/imagine prompt: time-lapse photography, a single rose wilting in a glass vase, dusty room, shaft of light, [Style Suffix] --ar 16:9` |
| ... | ... | ... | ... |
```

---

## ⚠️ PROMPT ENGINEERING TIPS

- **Lighting is Key:** Always specify lighting (Volumetric, Rim, Soft, Hard).
- **Camera Angles:** Use `Low angle` (Power), `High angle` (Vulnerability), `Dutch angle` (Chaos).
- **Negative Prompts (Midjourney):** `--no text, watermark, blurry, deformed hands, extra fingers.`
