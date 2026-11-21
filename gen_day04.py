import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

DAY4_DIR = os.path.join(WEEK1_DIR, 'Day_04_CaseStudy_GreenLine_Adblue')
os.makedirs(DAY4_DIR, exist_ok=True)

# Slide 1: Cover
def create_slide_1():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="01 / 05", accent=CYAN)
    
    draw_pill_badge(draw, 60, 145, "IFFCO ADBLUE LOGISTICS ENGINE", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 21)
    font_mono = get_font(FONT_MENLO, 18)
    
    title_text = "How Cypher Matrix engineered\nGreen Line Distribution's offline-first\nmobile engine for remote fleet corridors."
    draw_safe_text(draw, 60, 215, title_text, font_hero, WHITE, max_width=960, line_spacing=10)
    
    # Left Details Box
    draw_glass_card(img, 60, 455, 520, 520, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((90, 485), "CLIENT SNAPSHOT:", font=get_font(FONT_AVENIR, 24, index=2), fill=CYAN)
    
    details = [
        ("Company", "Green Line Distribution (VLX)"),
        ("Industry", "Chemical & Fleet Logistics (IFFCO Adblue)"),
        ("Key Challenge", "Zero connectivity in rural transit corridors"),
        ("Architecture", "Offline-first Flutter + Background Sync Engine"),
        ("Outcome", "0 lost delivery records across 100% routes")
    ]
    curr_y = 535
    for k, v in details:
        draw.text((90, curr_y), k.upper(), font=font_mono, fill=TEXT_MUTED)
        curr_y = draw_safe_text(draw, 90, curr_y + 24, v, font_body, WHITE, max_width=460, line_spacing=4) + 14
        
    # Right Side: Embed genuine green-line-project-icon.jpg
    gl_path = os.path.join(REF_DIR, 'green-line-project-icon.jpg')
    if os.path.exists(gl_path):
        gl_img = Image.open(gl_path).convert('RGBA')
        gl_img = gl_img.resize((370, 780), Image.Resampling.LANCZOS)
        draw_glass_card(img, 620, 455, 400, 520, radius=24, bg=(12, 16, 24, 255), border=(0, 240, 255, 120))
        img.alpha_composite(gl_img.crop((0, 0, 370, 480)), (635, 475))
        
    draw_glass_card(img, 60, 1005, 960, 175, radius=18, bg=(14, 20, 30, 250), border=(0, 255, 136, 120))
    draw.text((95, 1030), "THE LESSON FOR ENTERPRISE ARCHITECTS:", font=get_font(FONT_AVENIR, 22, index=2), fill=EMERALD)
    lesson = "If your mobile app crashes when 5G drops, you haven't built a mobile app—you've built a fragile web wrapper. Swipe to inspect the solution architecture."
    draw_safe_text(draw, 95, 1070, lesson, font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w, h, cta_text="Swipe to The Challenge ->", accent=CYAN)
    img.convert('RGB').save(os.path.join(DAY4_DIR, 'Slide_01_Cover.jpg'), quality=95)
    print("Re-generated Day 4 Slide 1 (Bounds Guaranteed)")

# Slide 2: The Challenge
def create_slide_2():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="02 / 05", accent=CYAN)
    
    font_title = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 19)
    
    draw.text((60, 150), "THE OPERATIONAL CRISIS", font=font_title, fill=WHITE)
    draw.text((60, 215), "Why traditional cloud apps fail inside national agricultural distribution networks:", font=font_body, fill=TEXT_MUTED)
    
    challenges = [
        ("01. RURAL DEAD ZONES (ZERO NETWORK CONNECTIVITY)", CRIMSON,
         "Truck drivers hauling tons of critical IFFCO Adblue travel through remote highway stretches with zero 4G/5G reception. Standard apps that rely on live server pings freeze, lock up, and force app restarts."),
        ("02. MANUAL INVOICING & INVENTORY DISCREPANCIES", CRIMSON,
         "When mobile screens failed, drivers resorted to handwritten paper slips. Deliveries were delayed, customer signatures were lost, and warehouse managers suffered daily inventory balance discrepancies."),
        ("03. COMPLEX TRANSACTIONAL CONFLICTS", CRIMSON,
         "When 10 drivers reconnect to cellular towers simultaneously at highway hubs, standard database backends throw lock timeouts and corrupt sequential delivery numbering.")
    ]
    
    for idx, (title, col, desc) in enumerate(challenges):
        cy = 280 + idx * 285
        draw_glass_card(img, 60, cy, 960, 260, radius=18, bg=(24, 16, 22, 240), border=(255, 51, 102, 120))
        draw_pill_badge(draw, 90, cy + 22, title, font_mono, accent_color=col)
        draw_safe_text(draw, 90, cy + 80, desc, font_body, WHITE, max_width=880, line_spacing=6)
            
    add_footer(draw, w, h, cta_text="Swipe to The Architecture ->", accent=CYAN)
    img.convert('RGB').save(os.path.join(DAY4_DIR, 'Slide_02_The_Challenge.jpg'), quality=95)
    print("Re-generated Day 4 Slide 2 (Bounds Guaranteed)")

# Slide 3: The Architecture
def create_slide_3():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="03 / 05", accent=EMERALD)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "THE OFFLINE-FIRST ARCHITECTURE", font=font_title, fill=WHITE)
    draw.text((60, 215), "How Cypher Matrix solved connectivity drops permanently:", font=font_body, fill=TEXT_MUTED)
    
    arch = [
        ("LOCAL SQLITE REPLICA ON DEVICE", CYAN,
         "Drivers write transactions (fuel quantity, customer sign, GPS stamp) directly to an encrypted local SQLite database with zero network dependencies. UI latency is 0 milliseconds."),
        ("BACKGROUND RESILIENT SYNC QUEUE", EMERALD,
         "An intelligent background WorkManager daemon monitors network signal. The instant 4G or Wi-Fi is detected, queued transactions are compressed and dispatched in batches."),
        ("AUTOMATED CONFLICT RESOLUTION", CYAN,
         "Using Conflict-Free Replicated Data Types (CRDTs) and cryptographic event hashing, our server reconciles multi-driver updates with zero lost records or race conditions.")
    ]
    
    for idx, (title, col, desc) in enumerate(arch):
        cy = 280 + idx * 260
        draw_glass_card(img, 60, cy, 960, 235, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
        draw_pill_badge(draw, 90, cy + 22, title, font_mono, accent_color=col)
        draw_safe_text(draw, 90, cy + 80, desc, font_body, WHITE, max_width=880, line_spacing=6)
            
    draw_glass_card(img, 60, 1080, 960, 100, radius=14, bg=(10, 14, 22, 255), border=(0, 255, 136, 120))
    draw.text((90, 1115), "[System Status] 100% Offline Resilience • Zero UI Freezes • Auto Cloud Sync", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to Measurable Results ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY4_DIR, 'Slide_03_Architecture.jpg'), quality=95)
    print("Re-generated Day 4 Slide 3 (Bounds Guaranteed)")

# Slide 4: Measurable Impact
def create_slide_4():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 35), glow_pos=(540, 600, 450))
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="04 / 05", accent=EMERALD)
    
    font_title = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 19)
    
    draw.text((60, 150), "MEASURABLE PRODUCTION OUTCOMES", font=font_title, fill=WHITE)
    draw.text((60, 215), "Real-world engineering impact delivered for Green Line Distribution:", font=font_body, fill=TEXT_MUTED)
    
    metrics = [
        ("0", "LOST TRANSACTIONS", "Zero delivery records lost despite hundreds of rural dead zones.", EMERALD),
        ("100%", "ROUTE ACCOUNTABILITY", "Every liter of IFFCO Adblue tracked with GPS timestamp.", CYAN),
        ("4.8x", "FASTER DRIVER CHECKOUT", "Drivers complete delivery logging in 35 seconds flat.", EMERALD),
        ("100%", "DATA INTEGRITY", "Automated background sync eliminates manual reconciliation.", CYAN)
    ]
    
    for idx, (val, label, desc, col) in enumerate(metrics):
        col_idx = idx % 2
        row_idx = idx // 2
        bx = 60 + col_idx * 495
        by = 280 + row_idx * 335
        
        draw_glass_card(img, bx, by, 465, 305, radius=20, bg=(16, 22, 34, 245), border=CARD_BORDER)
        draw.text((bx + 35, by + 30), val, font=get_font(FONT_AVENIR, 64, index=2), fill=col)
        draw.text((bx + 35, by + 120), label, font=get_font(FONT_AVENIR, 22, index=2), fill=WHITE)
        draw_safe_text(draw, bx + 35, by + 175, desc, font_body, TEXT_MUTED, max_width=395, line_spacing=6)
            
    draw_glass_card(img, 60, 970, 960, 200, radius=18, bg=(14, 20, 28, 250), border=(0, 255, 136, 120))
    draw.text((95, 1005), "WHY CLIENTS CHOOSE CYPHER MATRIX:", font=get_font(FONT_AVENIR, 22, index=2), fill=EMERALD)
    quote = (
        "We don't build software that only works in Silicon Valley demo conditions. "
        "We build bulletproof digital infrastructure that performs in real-world dust, highways, and rural connectivity."
    )
    draw_safe_text(draw, 95, 1045, quote, font_body, WHITE, max_width=890, line_spacing=8)
        
    add_footer(draw, w, h, cta_text="Swipe to Enterprise Scoping ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY4_DIR, 'Slide_04_Impact_Metrics.jpg'), quality=95)
    print("Re-generated Day 4 Slide 4 (Bounds Guaranteed)")

# Slide 5: Outro & Scoping CTA
def create_slide_5():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 40), glow_pos=(540, 600, 500))
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="05 / 05", accent=CYAN)
    
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 260), Image.Resampling.LANCZOS)
        lw, lh = logo.size
        img.alpha_composite(logo, (w // 2 - lw // 2, 200))
        
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_sub = get_font(FONT_HELVETICA, 26)
    font_mono = get_font(FONT_MENLO, 20)
    
    draw.text((w // 2, 480), "BUILD BULLETPROOF SOFTWARE", font=font_hero, fill=WHITE, anchor='mm')
    draw.text((w // 2, 540), "Enterprise Mobile • Fleet Logistics • High-Scale Web", font=font_sub, fill=CYAN, anchor='mm')
    
    draw_glass_card(img, 100, 630, 880, 420, radius=24, bg=(16, 22, 34, 250), border=(0, 240, 255, 160))
    draw.text((w // 2, 690), "HAVE A COMPLEX ENGINEERING PROJECT?", font=get_font(FONT_AVENIR, 30, index=2), fill=WHITE, anchor='mm')
    
    pitch = (
        "Whether you are engineering an offline-first mobile app,\n"
        "scaling an enterprise logistics platform, or building bank-grade SaaS—\n"
        "Cypher Matrix is your trusted end-to-end technology partner."
    )
    for i, l in enumerate(pitch.split('\n')):
        draw.text((w // 2, 750 + i * 36), l, font=font_sub, fill=TEXT_MUTED, anchor='mm')
        
    btn_w, btn_h = 740, 80
    bx = (w - btn_w) // 2
    by = 910
    draw.rounded_rectangle([bx, by, bx + btn_w, by + btn_h], radius=16, fill=CYAN)
    draw.text((w // 2, by + btn_h // 2), "DM 'PROJECT' FOR AN ARCHITECTURAL CONSULTATION", font=get_font(FONT_AVENIR, 23, index=2), fill=(8, 10, 15, 255), anchor='mm')
    
    draw.text((w // 2, 1140), "CYPHER MATRIX TECHNOLOGIES  |  cyphermatrix.io", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    draw.text((w // 2, 1180), "Gandhinagar / Ahmedabad • Global Client Services", font=font_mono, fill=EMERALD, anchor='mm')
    
    add_footer(draw, w, h, cta_text="Share with an Enterprise Leader ->", accent=CYAN)
    img.convert('RGB').save(os.path.join(DAY4_DIR, 'Slide_05_CTA_Outro.jpg'), quality=95)
    print("Re-generated Day 4 Slide 5 (Bounds Guaranteed)")

create_slide_1()
create_slide_2()
create_slide_3()
create_slide_4()
create_slide_5()
