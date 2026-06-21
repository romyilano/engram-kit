# Art Style Presets

Present these to the user in the intake step (the skill always asks — there is
no default). Once chosen, the **style block** is locked and restated *verbatim*
in every `page-XX.md` prompt so generated pages stay visually consistent.

Each preset below gives a short pitch (when it fits) and a ready-to-paste style
block. The user may also describe a custom style — capture it in the same
"style block" shape.

---

## 1 · Gekiga (default signature look)
*Best for: serious technical/scientific sources, protocols, security, systems.*

```
Style:
Classic gekiga.
Black and white.
Gray halftone shading.
Detailed pen and ink linework.
Realistic mature anatomy.
Lone Wolf and Cub influence.
Serious educational tone.
Not cute. Not chibi. Not moe. Not modern glossy anime. Not digital-painted.
```
Visual references: Lone Wolf and Cub, Golgo 13, Akira technical sequences,
Nausicaä engineering scenes, educational manga textbooks.

## 2 · Clean educational
*Best for: broad whitepapers, business/econ, onboarding, general audiences.*

```
Style:
Clean modern educational manga.
Black and white with light gray screentone.
Clear confident linework, generous negative space.
Friendly but professional; legible diagrams integrated into panels.
Approachable realistic proportions.
Not gritty. Not chibi. Not glossy 3D.
```

## 3 · Shonen explainer
*Best for: energetic topics, younger/teen audiences, "vs." framings.*

```
Style:
Shonen manga.
Black and white with dynamic screentone and speed lines.
Bold expressive linework, high energy, dramatic angles.
Expressive faces and motion.
Clean enough for diagrams and labels.
Not photorealistic. Not muddy.
```

## 4 · Watercolor / soft (Ghibli-adjacent)
*Best for: humanities, biology/nature, ethics, gentle introductions.*

```
Style:
Soft hand-painted watercolor manga.
Muted natural color palette.
Gentle linework, atmospheric backgrounds, warm lighting.
Calm, contemplative educational tone.
Studio-Ghibli-adjacent warmth (not a copy of any film).
Not harsh. Not neon. Not 3D-rendered.
```

## 5 · Technical noir
*Best for: cryptography, security, adversarial/threat-model material.*

```
Style:
High-contrast noir manga.
Black and white, heavy blacks, dramatic chiaroscuro shadows.
Sharp inked linework, moody atmosphere.
Tense, investigative tone.
Diagrams rendered as glowing schematics where useful.
Not soft. Not cute. Not low-contrast.
```

## 6 · Kid-friendly
*Best for: K–12, museum/outreach, very gentle intros.*

```
Style:
Friendly all-ages manga.
Black and white (or 2–3 flat colors) with simple clean linework.
Rounded approachable character designs (not babyish).
Big clear panels, large lettering space, simple backgrounds.
Cheerful encouraging tone.
Not dense. Not gritty. Not text-heavy.
```

---

## Picking & locking
- Recommend a preset based on the source (e.g. gekiga for a protocol spec,
  watercolor for a biology chapter), but let the user decide.
- Record the chosen preset name and its style block in `manifest.md`.
- Paste the style block into every page prompt unchanged.
