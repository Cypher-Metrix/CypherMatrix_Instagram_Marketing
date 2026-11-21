import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

DAY2_DIR = os.path.join(WEEK1_DIR, 'Day_02_Flutter_vs_ReactNative')
os.makedirs(DAY2_DIR, exist_ok=True)

# 1. Reel Cover (1080x1920)
def create_reel_cover():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 40), glow_pos=(540, 960, 600))
    
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 80), Image.Resampling.LANCZOS)
        img.alpha_composite(logo, (w // 2 - logo.size[0] // 2, 140))
        
    font_badge = get_font(FONT_MENLO, 22)
    font_hero = get_font(FONT_AVENIR, 60, index=2)
    font_sub = get_font(FONT_AVENIR, 34, index=2)
    font_body = get_font(FONT_HELVETICA, 26)
    font_mono = get_font(FONT_MENLO, 22)
    
    draw_pill_badge(draw, (w - 420) // 2, 260, "2026 ARCHITECTURE TEARDOWN", font_badge, accent_color=CYAN)
    
    draw.text((w // 2, 380), "FLUTTER", font=font_hero, fill=CYAN, anchor='mm')
    draw.text((w // 2, 450), "VS", font=get_font(FONT_AVENIR, 38, index=2), fill=TEXT_MUTED, anchor='mm')
    draw.text((w // 2, 530), "REACT NATIVE", font=font_hero, fill=EMERALD, anchor='mm')
    
    draw.text((w // 2, 640), "Real Production Benchmarks from 13+ Apps", font=font_sub, fill=WHITE, anchor='mm')
    draw.text((w // 2, 695), "Why we chose Flutter to save 4 months of engineering.", font=font_body, fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img, 80, 770, 920, 770, radius=24, bg=(16, 22, 32, 245), border=(0, 240, 255, 120))
    draw.text((120, 815), "PERFORMANCE TELEMETRY (IMPELLER ENGINE):", font=font_mono, fill=CYAN)
    
    metrics = [
        ("Frame Rate Stability (Low-end Android)", "FLUTTER: 60 FPS (Rock Solid)", "RN: 48 - 56 FPS (Microstutter)", EMERALD),
        ("Engineering Delivery Timeline", "16 Weeks Saved via Unified UI", "Separate Bridge Configurations", CYAN),
        ("Cold App Startup Time", "180 ms AOT Native Binary", "320 ms Hermes JS Bytecode", EMERALD),
        ("Cross-Platform Pixel Parity", "100% Identical Canvas Rendering", "Native Component Variations", CYAN)
    ]
    
    for idx, (title, fl_val, rn_val, col) in enumerate(metrics):
        box_y = 875 + idx * 155
        draw.rounded_rectangle([120, box_y, 960, box_y + 130], radius=14, fill=(10, 14, 22, 255), outline=CARD_BORDER)
        draw.text((145, box_y + 16), title, font=get_font(FONT_AVENIR, 22, index=2), fill=WHITE)
        draw.text((145, box_y + 54), f"[+] {fl_val}", font=font_mono, fill=col)
        draw.text((145, box_y + 88), f"[-] {rn_val}", font=font_mono, fill=TEXT_MUTED)
        
    draw_glass_card(img, 80, 1590, 920, 180, radius=20, bg=(14, 18, 26, 245), border=(0, 255, 136, 140))
    draw.text((w // 2, 1645), "WATCH THIS 45-SECOND REEL TEARDOWN", font=get_font(FONT_AVENIR, 28, index=2), fill=EMERALD, anchor='mm')
    draw.text((w // 2, 1700), "DM 'PROJECT' to discuss your 2027 mobile tech stack.", font=font_body, fill=WHITE, anchor='mm')
    
    draw.text((w // 2, 1840), "CYPHER MATRIX  |  @cyphermatrixpvtltd", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY2_DIR, 'Reel_Cover_1080x1920.jpg'), quality=95)
    print("Re-generated Day 2 Reel Cover (Bounds Guaranteed)")

# 2. Telemetry Card (1080x1920)
def create_telemetry_card():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 35), glow_pos=(540, 1100, 500))
    
    font_badge = get_font(FONT_MENLO, 22)
    font_title = get_font(FONT_AVENIR, 48, index=2)
    font_mono = get_font(FONT_MENLO, 20)
    font_body = get_font(FONT_HELVETICA, 24)
    
    draw_pill_badge(draw, 80, 120, "PRODUCTION BENCHMARK CARD", font_badge, accent_color=EMERALD)
    
    draw.text((80, 200), "THE 3 ARCHITECTURAL CRITERIA", font=font_title, fill=WHITE)
    draw.text((80, 265), "What startup founders must know before choosing Flutter in 2026:", font=font_body, fill=TEXT_MUTED)
    
    cards = [
        ("01. THE RENDERING ENGINE: IMPELLER VS BRIDGE", CYAN, [
            "Flutter compiles directly to native ARM machine code via Impeller.",
            "Eliminates the JavaScript bridge entirely—zero runtime serialization lag.",
            "Result: 60 FPS locked even on low-cost $100 Android devices."
        ]),
        ("02. CODE REUSABILITY: 98% ACROSS MOBILE, WEB & DESKTOP", EMERALD, [
            "Single codebase for Android, iOS, and POS terminal hardware.",
            "One engineering sprint delivers 3 platforms simultaneously.",
            "Saved 16 weeks of development on our Green Line logistics deployment."
        ]),
        ("03. OFFENSIVE SECURITY RESILIENCE", CRIMSON, [
            "AOT binary compilation makes decompilation significantly harder.",
            "Obfuscated symbol trees prevent automated reverse-engineering attacks.",
            "Pre-audited with Cypher Matrix internal VAPT protocols."
        ])
    ]
    
    for idx, (head, col, bullets) in enumerate(cards):
        cy = 350 + idx * 425
        draw_glass_card(img, 80, cy, 920, 390, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw_pill_badge(draw, 110, cy + 25, head, font_mono, accent_color=col)
        curr_y = cy + 85
        for b in bullets:
            curr_y = draw_safe_text(draw, 110, curr_y, f"[+] {b}", font_body, WHITE, max_width=860, line_spacing=6) + 10
            
    draw_glass_card(img, 80, 1660, 920, 180, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 160))
    draw.text((w // 2, 1715), "BUILDING A CROSS-PLATFORM MOBILE PRODUCT?", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD, anchor='mm')
    draw.text((w // 2, 1765), "DM 'PROJECT' to schedule an engineering scoping call.", font=font_body, fill=WHITE, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY2_DIR, 'OnScreen_Telemetry_1080x1920.jpg'), quality=95)
    print("Re-generated Day 2 Telemetry Card (Bounds Guaranteed)")

create_reel_cover()
create_telemetry_card()
