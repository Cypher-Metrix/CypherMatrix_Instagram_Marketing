---
title: Mandatory Typography and Layout Bounds Rules
tags:
  - cyphermatrix/rules
  - typography
  - layout
  - boundaries
aliases:
  - Text Bounds Rule
  - Zero Overflow Rule
up: "[[00_CypherMatrix_MOC]]"
related:
  - "[[Brand_Strategy]]"
  - "[[Content_Strategy]]"
---

# MANDATORY TYPOGRAPHY & LAYOUT BOUNDS RULES

**Applies to:** All visual creatives, carousels, reels covers, story sequences, infographics, and marketing assets for Cypher Matrix.

---

## 1. THE ZERO TEXT-OVERFLOW LAW
**Under NO circumstances may any text string extend outside its designated card, container, or canvas edge.**

Every visual asset must pass strict bounds checking before export.

---

## 2. STRICT GEOMETRIC CONSTRAINTS

| Element | Constraint | Implementation |
| :--- | :--- | :--- |
| **Canvas Safe Margin** | Minimum 60px on all 4 edges | No container or text may begin closer than 60px from `(0, 0)` or `(width, height)`. |
| **Card Inner Padding** | Minimum 30px horizontal, 25px vertical | `draw_text_box` must inset `box_x + pad_x` to `box_x + box_w - pad_x`. |
| **Max Text Width (`max_width`)** | `container_width - (2 * inner_padding)` | Every line of text must be computed against this exact pixel width. |
| **Multi-line Wrapping** | Mandatory `wrap_text()` on every sentence | Never call `draw.text` with a raw string containing > 4 words without passing through word wrapping. |
| **Code Blocks & Monospace** | Strict truncation or font scaling | If code lines exceed container width, reduce font size or truncate with visual syntax ellipsis. |

---

## 3. PROGRAMMATIC ENFORCEMENT ENGINE (`draw_safe_text`)

All asset generation scripts must use the standardized `draw_safe_text` and `draw_wrapped_lines` methods:

```python
def draw_safe_text(draw, x, y, text, font, fill, max_width, line_spacing=10):
    """
    Renders text with strict line wrapping and bounds checking.
    Guarantees that no line exceeds max_width or clips the right edge.
    """
    words = text.split(' ')
    lines = []
    curr = []
    for w in words:
        test = ' '.join(curr + [w])
        bbox = draw.textbbox((0, 0), test, font=font)
        if (bbox[2] - bbox[0]) <= max_width:
            curr.append(w)
        else:
            if curr:
                lines.append(' '.join(curr))
            curr = [w]
    if curr:
        lines.append(' '.join(curr))
        
    curr_y = y
    for line in lines:
        draw.text((x, curr_y), line, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=font)
        curr_y += (bbox[3] - bbox[1]) + line_spacing
        
    return curr_y
```

---

## 4. PRE-EXPORT BOUNDS AUDIT PROCEDURE
Before saving any `.jpg` or `.png`:
1. Check horizontal coordinate: `x_start + text_width < container_x_end`.
2. Check vertical coordinate: `y_start + total_text_height < container_y_end`.
3. If an overflow is detected during dry-run, dynamically scale font size down by 2pt increments until fully enclosed.
