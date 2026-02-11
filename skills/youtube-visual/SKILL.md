---
name: youtube-visual
description: >
  Visual Architect for YouTube (V1.0). Transforms scripts into metaphorical, high-emotion 
  image prompts optimized for automation (Runware/Python). Focuses on character consistency, 
  cinematic style, and visual rhythm.
version: 1.0.0
author: Antigravity & SonPM Master Concepts
category: content-creation
tags: [youtube, image-generation, runware, midjourney, metaphors, automation, visual-storytelling]
risk: safe
---

# YouTube Visual Architect V1.0 (Automation-Ready)

This skill is designed to bridge the gap between a written script and a high-end cinematic video production. It transforms text into a structured "Visual Data Payload" optimized for batch image generation.

---

## 🛠️ THE CORE DIRECTIVES

1.  **Metaphor Over Literal:** Avoid literal illustrations. Use symbolic, high-emotion metaphors to represent abstract concepts (e.g., "Silence" -> "A lone tree in a vacuum-sealed glass jar").
2.  **Visual DNA Consistency:** Every prompt must include `[GLOBAL_STYLE]` and `[CHARACTER_DESC]` anchors to ensure stability across 100+ images.
3.  **Automation-First Formatting:** Output must be structured (JSON or Python List) to be easily parsed by Python scripts using the Runware SDK.
4.  **Visual Rhythm:** Apply varied camera angles (Extreme Close-up, Wide, POV, Bird's eye) to prevent visual stagnation. Never use the same shot type more than twice in a row.
5.  **Sensory Descriptions:** Use vivid, sensory-rich verbs and lighting terms (volumetric, backlight, bokeh, 35mm film grain).

---

## 📋 THE 6-PHASE WORKFLOW

### PHASE 0: VISUAL BRANDING & DNA EXTRACTION
1.  **Analyze References:** The user provides a character image/description and a style image/description.
2.  **Define Constants:** Extract and define:
    *   `CHARACTER_ANCHOR`: The immutable physical traits of the character.
    *   `STYLE_ANCHOR`: The specific lighting, color palette, and camera specs.
3.  **Validation:** AI presents these anchors for user confirmation.

### PHASE 1: SEMANTIC SCENE SLICING
1.  **Input:** VoiceScript from `youtube-script-master`.
2.  **Slice:** Break the script into small scenes based on semantic meaning (usually 1-2 sentences per scene).
3.  **Duration Mapping:** Estimate the duration of each scene based on word count.

### PHASE 2: METAPHORICAL CONCEPT LAB
1.  **Brainstorm:** For each scene, create a high-impact metaphorical concept that illustrates the *feeling* of the words.
2.  **Select:** Choose the most cinematic and "viral" metaphor.

### PHASE 3: COMPOSITION & RHYTHM MAPPING
1.  **Shot Type Assignment:** For each scene, assign a cinematic shot type (Vd: CU, MCU, WS, Bird's Eye).
2.  **Pacing Check:** Ensure the visual rhythm is dynamic and matches the script's emotional peaks.

### PHASE 4: PROMPT ALCHEMY (RUNWARE OPTIMIZED)
1.  **Formula:** Construct the final prompt: `[Subject/Action] + [Metaphor Concept] + [CHARACTER_ANCHOR] + [STYLE_ANCHOR] + [Shot Type]`.
2.  **Polish:** Ensure the prompt uses keywords optimized for high-end models like Flux.1 or SDXL (via Runware).

### PHASE 5: THE MASTER EXPORT (HANDOFF)
1.  **Format:** Export to a `.txt` file.
2.  **Default Structure:** Ready-to-Paste Python List (per scene indices).
3.  **Alternative:** Optional Markdown table or JSON format.

---

## 🎯 INTEGRATED ENGINE DEFINITIONS
- **Semantic Mapping:** Slicing script by logic/emotion clusters, not just sentence count.
- **Visual Anchoring:** Rigid repetition of style tokens to prevent "style drift."
- **Automation Ready:** Clean strings without AI conversational filler, strictly formatted for dev-ops.
