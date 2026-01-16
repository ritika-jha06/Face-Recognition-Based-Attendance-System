import cv2
import numpy as np

# =====================================================
# Canvas
# =====================================================
WIDTH, HEIGHT = 1280, 720
template = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 245

# =====================================================
# Colors (BGR)
# =====================================================
CORAL = (85, 105, 255)
CORAL_DARK = (70, 90, 235)
NAVY = (38, 45, 90)
WHITE = (255, 255, 255)
TEXT_GRAY = (80, 80, 80)
SHADOW = (210, 210, 210)

# =====================================================
# Subtle vertical gradient
# =====================================================
for y in range(HEIGHT):
    shade = 245 - int((y / HEIGHT) * 10)
    template[y, :] = (shade, shade, shade)

# =====================================================
# Helper: slightly rounded rectangle
# =====================================================
def soft_rect(img, pt1, pt2, r, color):
    x1, y1 = pt1
    x2, y2 = pt2

    cv2.rectangle(img, (x1+r, y1), (x2-r, y2), color, -1)
    cv2.rectangle(img, (x1, y1+r), (x2, y2-r), color, -1)

    cv2.circle(img, (x1+r, y1+r), r, color, -1)
    cv2.circle(img, (x2-r, y1+r), r, color, -1)
    cv2.circle(img, (x1+r, y2-r), r, color, -1)
    cv2.circle(img, (x2-r, y2-r), r, color, -1)

# =====================================================
# Header (almost rectangular)
# =====================================================
soft_rect(template, (45, 25), (900, 90), 10, CORAL)
cv2.putText(
    template,
    "FACE RECOGNITION & ATTENDANCE",
    (75, 72),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    WHITE,
    2,
    cv2.LINE_AA
)

# =====================================================
# Camera area (shadow + frame)
# =====================================================
soft_rect(template, (58, 158), (698, 638), 12, SHADOW)
soft_rect(template, (55, 150), (695, 630), 12, CORAL)

cv2.putText(
    template,
    "CAMERA FEED",
    (275, 395),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    WHITE,
    2,
    cv2.LINE_AA
)

# =====================================================
# Instruction text
# =====================================================
cv2.putText(
    template,
    "PRESS 'O' FOR TAKE ATTENDANCE",
    (235, 690),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    TEXT_GRAY,
    2,
    cv2.LINE_AA
)

# =====================================================
# Requirement panel (clean card)
# =====================================================
soft_rect(template, (940, 40), (1240, 680), 14, NAVY)

cv2.putText(
    template,
    "REQUIREMENT",
    (985, 105),
    cv2.FONT_HERSHEY_COMPLEX,
    1,
    CORAL,
    2,
    cv2.LINE_AA
)

requirements = [
    "1. PYTHON",
    "2. OPENCV",
    "3. SCIKIT-LEARN"
]

y = 180
for r in requirements:
    cv2.putText(
        template,
        r,
        (985, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        WHITE,
        2,
        cv2.LINE_AA
    )
    y += 65

# =====================================================
# Save
# =====================================================
cv2.imwrite("background.png", template)
print("✅ Clean professional template created (background.png)")
