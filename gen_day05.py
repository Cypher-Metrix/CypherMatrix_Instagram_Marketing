import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

DAY5_DIR = os.path.join(WEEK1_DIR, 'Day_05_CypherMatrix_SecureBuildScale')
os.makedirs(DAY5_DIR, exist_ok=True)

def create_day5_infographic():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(540, 480, 500))
    add_header(img, draw, category="COMPANY CULTURE & AUTHORITY", slide_str="MANIFESTO", accent=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_sub = get_font(FONT_HELVETICA, 24)
    font_body = get_font(FONT_HELVETICA, 20)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_pill_badge(draw, 60, 140, "THE CYPHER MATRIX ETHOS", font_mono, accent_color=EMERALD)
    
    draw_safe_text(draw, 60, 205, "Why we pre-audit every line of code\nwith offensive security before deployment.", font_hero, WHITE, max_width=960, line_spacing=8)
    draw_safe_text(draw, 60, 320, "Most agencies build fast and patch later. We engineer bank-grade resilient platforms.", font_sub, TEXT_MUTED, max_width=960)
    
    # The 3 Pillars (Side by Side Grid)
    pillars = [
        ("SECURE.", CRIMSON, "OFFENSIVE SECURITY", [
            "Internal VAPT audit in every sprint",
            "Zero hardcoded secrets & TLS pinning",
            "OWASP Top 10 pre-deployment defense"
        ]),
        ("BUILD.", EMERALD, "ENTERPRISE SOFTWARE", [
            "High-speed Flutter & React engineering",
            "Offline-first mobile architecture",
            "Pixel-perfect, 60 FPS fluid interfaces"
        ]),
        ("SCALE.", CYAN, "GLOBAL CLOUD SYSTEMS", [
            "Resilient microservices & clean APIs",
            "Multi-tenant data isolation & RBAC",
            "Infrastructure built for high concurrency"
        ])
    ]
    
    card_w = 305
    for idx, (p_name, col, p_sub, bullets) in enumerate(pillars):
        px = 60 + idx * 328
        py = 390
        draw_glass_card(img, px, py, card_w, 440, radius=20, bg=(16, 22, 32, 245), border=(col[0], col[1], col[2], 140))
        draw.text((px + 20, py + 25), p_name, font=get_font(FONT_AVENIR, 32, index=2), fill=col)
        draw.text((px + 20, py + 72), p_sub, font=get_font(FONT_MENLO, 15), fill=WHITE)
        draw.line([(px + 20, py + 100), (px + card_w - 20, py + 100)], fill=CARD_BORDER, width=1)
        
        curr_y = py + 115
        for b in bullets:
            curr_y = draw_safe_text(draw, px + 20, curr_y, f"[+] {b}", font_body, TEXT_MUTED, max_width=card_w - 35, line_spacing=4) + 12
                
    # Traditional vs Cypher Matrix Comparison
    draw_glass_card(img, 60, 855, 960, 310, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.text((95, 885), "THE DIFFERENCE IN PRODUCTION OUTCOMES:", font=get_font(FONT_AVENIR, 24, index=2), fill=WHITE)
    
    # Left: Traditional
    draw.rounded_rectangle([95, 935, 510, 1130], radius=14, fill=(24, 14, 20, 255), outline=(255, 51, 102, 100))
    draw.text((115, 955), "TRADITIONAL DEV AGENCIES:", font=font_mono, fill=CRIMSON)
    t_lines = [
        "1. Rush functional code to meet deadline",
        "2. Accumulate technical & security debt",
        "3. Suffer data leak or fail compliance",
        "4. Spend $40,000 on emergency patches"
    ]
    for i, tl in enumerate(t_lines):
        draw_safe_text(draw, 115, 995 + i * 32, tl, font_body, TEXT_MUTED, max_width=380)
        
    # Right: Cypher Matrix
    draw.rounded_rectangle([530, 935, 985, 1130], radius=14, fill=(14, 24, 20, 255), outline=(0, 255, 136, 120))
    draw.text((550, 955), "CYPHER MATRIX ENGINEERING:", font=font_mono, fill=EMERALD)
    c_lines = [
        "1. VAPT & threat modeling built into sprint",
        "2. Zero technical debt; bank-grade code",
        "3. SOC2, ISO & enterprise audit-ready",
        "4. Seamless international product scaling"
    ]
    for i, cl in enumerate(c_lines):
        draw_safe_text(draw, 550, 995 + i * 32, cl, font_body, WHITE, max_width=415)
        
    add_footer(draw, w, h, cta_text="DM 'PROJECT' to build right ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY5_DIR, 'Creative_1080x1350.jpg'), quality=95)
    print("Re-generated Day 5 Infographic (Bounds Guaranteed)")

create_day5_infographic()
