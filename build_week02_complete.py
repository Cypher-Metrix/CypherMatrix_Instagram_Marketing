import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, BILL_MITRA_LOGO_PATH, REF_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

WEEK2_DIR = os.path.join(BASE_DIR, '04_Post_Creatives', 'Week_02')
os.makedirs(WEEK2_DIR, exist_ok=True)

w_port, h_port = 1080, 1350
w_reel, h_reel = 1080, 1920

# ==============================================================================
# DAY 09: TRACTOR HISAB REEL (1080x1920 Cover + Telemetry Card)
# ==============================================================================
d9_dir = os.path.join(WEEK2_DIR, 'Day_09_Tractor_Hisab_Agritech')
os.makedirs(d9_dir, exist_ok=True)

def build_day09():
    # Reel Cover
    img, draw = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 40), glow_pos=(540, 960, 550))
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 80), Image.Resampling.LANCZOS)
        img.alpha_composite(logo, (w_reel // 2 - logo.size[0] // 2, 140))
        
    draw_pill_badge(draw, (w_reel - 380) // 2, 260, "AGRITECH PRODUCT SHOWCASE", get_font(FONT_MENLO, 20), accent_color=EMERALD)
    draw.text((w_reel // 2, 380), "TRACTOR HISAB", font=get_font(FONT_AVENIR, 64, index=2), fill=EMERALD, anchor='mm')
    draw.text((w_reel // 2, 455), "Tractor chal raha hai par maheene ke end mein hisab gayab?", font=get_font(FONT_AVENIR, 28, index=2), fill=WHITE, anchor='mm')
    draw.text((w_reel // 2, 510), "Har tractor maalik yeh 3 badi galatiyan karta hai:", font=get_font(FONT_HELVETICA, 24), fill=TEXT_MUTED, anchor='mm')
    
    # 3 Mistakes Card
    draw_glass_card(img, 80, 580, 920, 980, radius=24, bg=(16, 22, 32, 245), border=(0, 255, 136, 120))
    draw.text((120, 625), "3 BIGGEST LOSSES IN TRACTOR BUSINESS:", font=get_font(FONT_MENLO, 20), fill=CYAN)
    
    mistakes = [
        ("01. Kisaano ki jotai diary mein likhna", "Khet ki jotai ghante ke hisab se hui ya bigha ke hisab se—kagaz phat jata hai ya diary kho jati hai. Lakho rupaye ki udhari fas jati hai."),
        ("02. Driver diesel aur advance hisab", "Driver ne kitna diesel dala aur kitna advance cash liya, maheene ke end mein tractor malik aur driver ke beech jhagda hota hai."),
        ("03. Pending payments follow-up na hona", "Kis kisaan par kitna paisa baaki hai yaad nahi rehta. Season nikal jane ke baad vasooli mushkil ho jati hai.")
    ]
    for idx, (m_head, m_desc) in enumerate(mistakes):
        my = 675 + idx * 280
        draw.rounded_rectangle([120, my, 960, my + 250], radius=16, fill=(10, 14, 22, 255), outline=CARD_BORDER)
        draw_pill_badge(draw, 145, my + 20, m_head, get_font(FONT_MENLO, 18), accent_color=CRIMSON)
        draw_safe_text(draw, 145, my + 75, m_desc, get_font(FONT_HELVETICA, 22), WHITE, max_width=770, line_spacing=6)
        
    draw_glass_card(img, 80, 1600, 920, 175, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 160))
    draw.text((w_reel // 2, 1650), "TRACTOR HISAB: SMART DIGITAL KHATABOOK", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD, anchor='mm')
    draw.text((w_reel // 2, 1705), "Watch this 40-second Reel to automate your farming accounts.", font=get_font(FONT_HELVETICA, 24), fill=WHITE, anchor='mm')
    draw.text((w_reel // 2, 1840), "CYPHER MATRIX PRODUCT  |  @cyphermatrixpvtltd", font=get_font(FONT_MENLO, 20), fill=TEXT_MUTED, anchor='mm')
    
    img.convert('RGB').save(os.path.join(d9_dir, 'Reel_Cover_1080x1920.jpg'), quality=95)
    
    # Telemetry Feature Card
    t_img, t_draw = create_base_canvas(w_reel, h_reel, glow_color=(0, 240, 255, 35), glow_pos=(540, 1000, 500))
    draw_pill_badge(t_draw, 80, 120, "TRACTOR HISAB FEATURES", get_font(FONT_MENLO, 22), accent_color=EMERALD)
    t_draw.text((80, 200), "HOW TRACTOR HISAB SOLVES IT", font=get_font(FONT_AVENIR, 48, index=2), fill=WHITE)
    t_draw.text((80, 265), "Built specifically for rural tractor owners & farming contractors:", font=get_font(FONT_HELVETICA, 24), fill=TEXT_MUTED)
    
    feats = [
        ("AUTOMATIC WORKING-HOUR TRACKER", CYAN, "Timer chalu karein—app automatically ghante aur minute ka exact hisab rupaye mein nikal deta hai."),
        ("FARMER-WISE UDHAR LEDGER", EMERALD, "Har kisaan ka alag khata. Ek click par WhatsApp par payment reminder aur bill receipt bhejein."),
        ("DIESEL & DRIVER EXPENSE AUDIT", CYAN, "Kitna diesel kis khet mein laga aur driver ne kitna kharch kiya, sab realtime cloud mein safe."),
        ("100% OFFLINE RURAL SUPPORT", EMERALD, "Khet mein internet nahi hai? Koi dikkat nahi. Internet aane par sara data automatically sync ho jata hai.")
    ]
    for idx, (f_h, col, f_d) in enumerate(feats):
        fy = 330 + idx * 310
        draw_glass_card(t_img, 80, fy, 920, 280, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw_pill_badge(t_draw, 110, fy + 22, f_h, get_font(FONT_MENLO, 19), accent_color=col)
        draw_safe_text(t_draw, 110, fy + 80, f_d, get_font(FONT_HELVETICA, 23), WHITE, max_width=860, line_spacing=6)
        
    draw_glass_card(t_img, 80, 1630, 920, 180, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 160))
    t_draw.text((w_reel // 2, 1685), "DM 'TRACTOR' FOR EARLY ACCESS & DEMO", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD, anchor='mm')
    t_draw.text((w_reel // 2, 1740), "Engineered by Cypher Matrix Technologies", font=get_font(FONT_HELVETICA, 22), fill=TEXT_MUTED, anchor='mm')
    
    t_img.convert('RGB').save(os.path.join(d9_dir, 'OnScreen_Telemetry_1080x1920.jpg'), quality=95)
    print("Day 09 generated.")

build_day09()

# ==============================================================================
# DAY 10: VEGGIEKING CASE STUDY (5 SLIDES, 1080x1350)
# ==============================================================================
d10_dir = os.path.join(WEEK2_DIR, 'Day_10_CaseStudy_VeggieKing_Retail')
os.makedirs(d10_dir, exist_ok=True)

def build_day10():
    w, h = w_port, h_port
    # Slide 1: Cover
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="01 / 05", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "RETAIL LOGISTICS & POS ENGINE", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 215, "How Cypher Matrix engineered\nVeggieKing's unified customer &\npartner delivery ecosystem.", font_hero, WHITE, max_width=960, line_spacing=10)
    
    # Left Card
    draw_glass_card(img, 60, 450, 520, 520, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((90, 480), "PROJECT SNAPSHOT:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    details = [
        ("Client", "VeggieKing (Retail Fresh Produce Ecosystem)"),
        ("Components", "Customer App + Partner POS + Delivery Engine"),
        ("Core Problem", "Real-time stock decay & delivery routing latency"),
        ("Architecture", "Flutter Multi-Platform + Node.js Microservices"),
        ("Outcome", "45% faster store checkout & 99.8% order accuracy")
    ]
    curr_y = 530
    for k, v in details:
        draw.text((90, curr_y), k.upper(), font=font_mono, fill=TEXT_MUTED)
        curr_y = draw_safe_text(draw, 90, curr_y + 24, v, font_body, WHITE, max_width=460, line_spacing=4) + 14
        
    # Right Side: Embed Veggieking Icon
    vk_path = os.path.join(REF_DIR, 'veggieking-customer-icon.png')
    if os.path.exists(vk_path):
        vk_img = Image.open(vk_path).convert('RGBA').resize((360, 360), Image.Resampling.LANCZOS)
        draw_glass_card(img, 620, 450, 400, 520, radius=24, bg=(12, 20, 22, 255), border=(0, 255, 136, 120))
        img.alpha_composite(vk_img, (640, 530))
        
    draw_glass_card(img, 60, 1000, 960, 175, radius=18, bg=(14, 20, 30, 250), border=(0, 255, 136, 120))
    draw.text((95, 1025), "THE E-COMMERCE LOGISTICS TAKEAWAY:", font=get_font(FONT_AVENIR, 22, index=2), fill=CYAN)
    lesson = "In grocery and retail logistics, seconds matter. A unified codebase across buyers, store counters, and drivers is the only way to prevent inventory mismatch."
    draw_safe_text(draw, 95, 1065, lesson, font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w, h, cta_text="Swipe to The Architecture ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(d10_dir, 'Slide_01_Cover.jpg'), quality=95)
    
    # Slides 2-5
    s_data = [
        ("Slide_02_The_Challenge.jpg", "02 / 05", "THE RETAIL FRESH PRODUCE CRISIS", [
            ("PERISHABLE INVENTORY DECAY", "Fresh produce inventory changes by the minute. If the customer app displays stock that a store already sold, cancellations skyrocket."),
            ("STORE DISPATCH BOTTLENECKS", "Store managers struggled with clunky manual computers while delivery drivers waited outside in traffic."),
            ("PAYMENT RECONCILIATION ERRORS", "Discrepancies between customer online payments, cash-on-delivery (COD), and merchant settlement led to accounting nightmares.")
        ]),
        ("Slide_03_Unified_Architecture.jpg", "03 / 05", "THE 3-TIER UNIFIED ARCHITECTURE", [
            ("TIER 1: CONSUMER MOBILE APP", "Ultra-fluid Flutter app with sub-second product search, dynamic price tiers, and instant UPI checkout."),
            ("TIER 2: MERCHANT STORE POS", "Offline-resilient tablet POS for fast barcode checkout and automatic real-time stock deduction."),
            ("TIER 3: DRIVER FLEET DISPATCH", "Optimized GPS route dispatch engine calculating real-time batch deliveries to minimize transit time.")
        ]),
        ("Slide_04_Production_Impact.jpg", "04 / 05", "MEASURABLE PRODUCTION OUTCOMES", [
            ("45% FASTER ORDER PROCESSING", "Order-to-pack turnaround dropped from 14 minutes down to under 7 minutes per customer order."),
            ("99.8% INVENTORY ACCURACY", "Real-time socket synchronization between store POS and mobile app eliminated duplicate stock sales."),
            ("ZERO RECONCILIATION GAPS", "Automated daily settlement dashboard gave franchise owners 100% financial visibility.")
        ]),
        ("Slide_05_CTA_Outro.jpg", "05 / 05", "SCALE YOUR RETAIL APP WITH CYPHER MATRIX", [
            ("BUILDING RETAIL, E-COMMERCE OR POS?", "From complex inventory microservices to cross-platform mobile apps, Cypher Matrix builds enterprise-grade software."),
            ("SCHEDULE AN ARCHITECTURAL AUDIT", "DM 'PROJECT' to discuss your digital transformation with our technical leads."),
            ("VISIT cyphermatrix.io", "Gandhinagar / Ahmedabad • International Engineering Services")
        ])
    ]
    for s_name, s_num, s_title, s_cards in s_data:
        s_img, s_draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 30), glow_pos=(540, 600, 450))
        add_header(s_img, s_draw, category="ENTERPRISE CASE STUDY", slide_str=s_num, accent=EMERALD)
        s_draw.text((60, 150), s_title, font=get_font(FONT_AVENIR, 42, index=2), fill=WHITE)
        s_draw.text((60, 215), "Production engineering standards applied at Cypher Matrix:", font=font_body, fill=TEXT_MUTED)
        
        for c_i, (c_h, c_desc) in enumerate(s_cards):
            cy = 280 + c_i * 280
            draw_glass_card(s_img, 60, cy, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 95, cy + 22, c_h, font_mono, accent_color=EMERALD if c_i==0 else CYAN)
            draw_safe_text(s_draw, 95, cy + 80, c_desc, font_body, WHITE, max_width=860, line_spacing=6)
            
        add_footer(s_draw, w, h, cta_text="Swipe to next ->" if s_num != "05 / 05" else "DM 'PROJECT' ->", accent=EMERALD)
        s_img.convert('RGB').save(os.path.join(d10_dir, s_name), quality=95)
    print("Day 10 generated.")

build_day10()

# ==============================================================================
# DAY 11: REVERSE-ENGINEERING DEFENSE (5 SLIDES, 1080x1350)
# ==============================================================================
d11_dir = os.path.join(WEEK2_DIR, 'Day_11_Mobile_Reverse_Engineering')
os.makedirs(d11_dir, exist_ok=True)

def build_day11():
    w, h = w_port, h_port
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="01 / 05", accent=CRIMSON)
    draw_pill_badge(draw, 60, 145, "OFFENSIVE BINARY AUDIT", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 215, "Can hackers decompile your mobile app\nand steal your proprietary algorithm?", font_hero, WHITE, max_width=960, line_spacing=10)
    
    # Terminal Box
    card_x, card_y, card_w, card_h = 60, 410, 960, 570
    draw_glass_card(img, card_x, card_y, card_w, card_h, radius=20, bg=(14, 18, 26, 245), border=(255, 51, 102, 120))
    
    t_bar_h = 55
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + t_bar_h], radius=20, fill=(20, 26, 38, 255))
    draw.rectangle([card_x, card_y + 20, card_x + card_w, card_y + t_bar_h], fill=(20, 26, 38, 255))
    draw.line([(card_x, card_y + t_bar_h), (card_x + card_w, card_y + t_bar_h)], fill=CARD_BORDER, width=1)
    draw.ellipse([card_x + 25, card_y + 20, card_x + 39, card_y + 34], fill=(255, 95, 87, 255))
    draw.ellipse([card_x + 49, card_y + 20, card_x + 63, card_y + 34], fill=(254, 187, 43, 255))
    draw.ellipse([card_x + 73, card_y + 20, card_x + 87, card_y + 34], fill=(39, 201, 63, 255))
    draw.text((card_x + 110, card_y + 18), "DECOMPILER INSPECTION: jadx-gui app_release.apk", font=font_mono, fill=TEXT_MUTED)
    draw.text((card_x + card_w - 240, card_y + 18), "EXPLOITABLE: YES", font=get_font(FONT_MENLO, 19), fill=CRIMSON)
    
    p1_x, panel_y, panel_w, panel_h = card_x + 25, card_y + t_bar_h + 20, 435, 330
    draw.rounded_rectangle([p1_x, panel_y, p1_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 12, 18, 255), outline=(255, 51, 102, 120))
    draw.text((p1_x + 20, panel_y + 20), "UNPROTECTED APK", font=get_font(FONT_AVENIR, 22, index=2), fill=CRIMSON)
    draw.text((p1_x + 20, panel_y + 55), "Decompiles in 30 seconds:", font=font_mono, fill=TEXT_MUTED)
    unprot = [
        "[✗] Source code extracted in Java",
        "[✗] Variable names & logic exposed",
        "[✗] API endpoint routes revealed",
        "[✗] In-app purchases easily bypassed"
    ]
    for i, u in enumerate(unprot):
        draw.text((p1_x + 20, panel_y + 95 + i * 40), u, font=font_mono, fill=(255, 120, 140, 255))
    draw.line([(p1_x + 20, panel_y + 275), (p1_x + panel_w - 20, panel_y + 275)], fill=CARD_BORDER, width=1)
    draw.text((p1_x + 20, panel_y + 290), "Risk: Clone Apps & IP Theft", font=font_mono, fill=CRIMSON)
    
    p2_x = card_x + 495
    draw.rounded_rectangle([p2_x, panel_y, p2_x + panel_w, panel_y + panel_h], radius=14, fill=(10, 20, 24, 255), outline=(0, 255, 136, 140))
    draw.text((p2_x + 20, panel_y + 20), "CYPHER MATRIX DEFENSE", font=get_font(FONT_AVENIR, 22, index=2), fill=EMERALD)
    draw.text((p2_x + 20, panel_y + 55), "Hardened binary protection:", font=font_mono, fill=TEXT_MUTED)
    prot = [
        "[✓] R8 / ProGuard symbol obfuscation",
        "[✓] Native ARM AOT machine code",
        "[✓] Anti-tamper & integrity checks",
        "[✓] Frida & Root/Jailbreak detection"
    ]
    for i, p in enumerate(prot):
        draw.text((p2_x + 20, panel_y + 95 + i * 40), p, font=font_mono, fill=(160, 255, 200, 255))
    draw.line([(p2_x + 20, panel_y + 275), (p2_x + panel_w - 20, panel_y + 275)], fill=CARD_BORDER, width=1)
    draw.text((p2_x + 20, panel_y + 290), "Result: Bank-Grade IP Protection", font=font_mono, fill=EMERALD)
    
    summary_y = panel_y + panel_h + 20
    draw.rounded_rectangle([card_x + 25, summary_y, card_x + card_w - 25, summary_y + 95], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((card_x + 45, summary_y + 18), "SECURITY REALITY:", font=font_mono, fill=EMERALD)
    draw_safe_text(draw, card_x + 45, summary_y + 48, "Anyone can download your APK from the Play Store and open it in JADX. If you don't obfuscate, you are giving away your backend blueprint.", font_body, WHITE, max_width=860, line_spacing=4)
    
    draw_glass_card(img, 60, 1010, 960, 170, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    callout = "Swipe through for the 5-slide guide: ProGuard configs, native symbol stripping, and runtime hooking countermeasures."
    draw_safe_text(draw, 95, 1035, callout, get_font(FONT_HELVETICA, 23), WHITE, max_width=890, line_spacing=6)
    draw.text((95, 1120), "[ Mobile Security Engineering Masterclass ]", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to Defense Stack ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(d11_dir, 'Slide_01_Cover.jpg'), quality=95)
    
    # Slides 2-5
    s_data = [
        ("Slide_02_How_Hackers_Decompile.jpg", "02 / 05", "THE ATTACK TOOLCHAIN: JADX & FRIDA", [
            ("APK EXTRACTION", "Attackers download the APK using public mirrors or ADB and unzip it to access AndroidManifest.xml and DEX bytecodes."),
            ("JADX-GUI DECOMPILATION", "In seconds, tools like JADX decompile Dalvik bytecodes back into readable Java classes—exposing logic and hidden routes."),
            ("RUNTIME HOOKING VIA FRIDA", "Attackers hook internal methods in memory at runtime to force authorization checks to return 'true'.")
        ]),
        ("Slide_03_Obfuscation_Config.jpg", "03 / 05", "OBFUSCATION & SYMBOL STRIPPING", [
            ("PROGUARD & R8 RULES", "Rename class, method, and field names to meaningless single letters (e.g. 'AuthService' becomes 'a.b.c')."),
            ("STRIP DEBUG METADATA", "Remove source file attributes and line number tables from production release binaries."),
            ("CONTROL FLOW FLATTENING", "Transform linear execution logic into complex state-machine loops that confound automated disassemblers.")
        ]),
        ("Slide_04_Root_Jailbreak_Defense.jpg", "04 / 05", "RUNTIME ENVIRONMENT ATTESTATION", [
            ("ROOT & JAILBREAK DETECTION", "Inspect device binaries for Magisk, Substrate, and Cydia hooks. Terminate sensitive sessions immediately."),
            ("EMULATOR VERIFICATION", "Detect whether the app is executing inside a headless analysis sandbox or virtual device."),
            ("PLAY INTEGRITY API INTEGRATION", "Verify cryptographically with Google Play that the app binary has not been tampered with or resigned.")
        ]),
        ("Slide_05_CTA_Outro.jpg", "05 / 05", "SECURE YOUR APPLICATION BINARY", [
            ("PRE-DEPLOYMENT VAPT AUDITS", "Cypher Matrix performs comprehensive mobile binary penetration testing before public app store submission."),
            ("SCHEDULE A CODE HARDENING REVIEW", "DM 'SECURITY' to receive our Mobile Anti-Tamper & Obfuscation Checklist."),
            ("VISIT cyphermatrix.io", "Gandhinagar / Ahmedabad • Enterprise Cybersecurity Center")
        ])
    ]
    for s_name, s_num, s_title, s_cards in s_data:
        s_img, s_draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 30), glow_pos=(540, 600, 450))
        add_header(s_img, s_draw, category="CYBERSECURITY MASTERCLASS", slide_str=s_num, accent=CRIMSON)
        s_draw.text((60, 150), s_title, font=get_font(FONT_AVENIR, 42, index=2), fill=WHITE)
        s_draw.text((60, 215), "Production engineering standards applied at Cypher Matrix:", font=font_body, fill=TEXT_MUTED)
        
        for c_i, (c_h, c_desc) in enumerate(s_cards):
            cy = 280 + c_i * 280
            draw_glass_card(s_img, 60, cy, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 95, cy + 22, c_h, font_mono, accent_color=CRIMSON if c_i==0 else CYAN)
            draw_safe_text(s_draw, 95, cy + 80, c_desc, font_body, WHITE, max_width=860, line_spacing=6)
            
        add_footer(s_draw, w, h, cta_text="Swipe to next ->" if s_num != "05 / 05" else "DM 'SECURITY' ->", accent=CRIMSON)
        s_img.convert('RGB').save(os.path.join(d11_dir, s_name), quality=95)
    print("Day 11 generated.")

build_day11()

# ==============================================================================
# DAY 12: ODOO FLUTTER OPEN SOURCE (INFOGRAPHIC, 1080x1350)
# ==============================================================================
d12_dir = os.path.join(WEEK2_DIR, 'Day_12_Odoo_Flutter_Library')
os.makedirs(d12_dir, exist_ok=True)

def build_day12():
    w, h = w_port, h_port
    img, draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 35), glow_pos=(540, 480, 500))
    add_header(img, draw, category="OPEN SOURCE & TECH AUTHORITY", slide_str="COMMUNITY", accent=CYAN)
    draw_pill_badge(draw, 60, 140, "DEVELOPER TOOLING CONTRIBUTION", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_sub = get_font(FONT_HELVETICA, 24)
    font_body = get_font(FONT_HELVETICA, 20)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 205, "Open Source Engineering: The Odoo\nMobile Client Library for Flutter.", font_hero, WHITE, max_width=960, line_spacing=8)
    draw_safe_text(draw, 60, 320, "Bridging enterprise ERP backends with modern mobile experiences.", font_sub, TEXT_MUTED, max_width=960)
    
    # 3 Key Value Cards
    cards = [
        ("XML-RPC & JSON-RPC CLIENT", CYAN, [
            "Seamless connection to any Odoo ERP instance.",
            "High-speed database schema introspection.",
            "Bi-directional ORM mapping in pure Dart."
        ]),
        ("ENTERPRISE SESSION HANDLING", EMERALD, [
            "Hardware-secured session token caching.",
            "Automatic re-authentication on 401 expiration.",
            "Role-based access permission validation."
        ]),
        ("OFFLINE SYNC RESILIENCE", CYAN, [
            "Caches ERP invoices, orders, and products locally.",
            "Enables field agents to operate without internet.",
            "Auto-syncs records once cellular network returns."
        ])
    ]
    card_w = 305
    for idx, (p_name, col, bullets) in enumerate(cards):
        px = 60 + idx * 328
        py = 390
        draw_glass_card(img, px, py, card_w, 440, radius=20, bg=(16, 22, 32, 245), border=(col[0], col[1], col[2], 140))
        draw.text((px + 20, py + 25), p_name, font=get_font(FONT_AVENIR, 24, index=2), fill=col)
        draw.line([(px + 20, py + 80), (px + card_w - 20, py + 80)], fill=CARD_BORDER, width=1)
        curr_y = py + 100
        for b in bullets:
            curr_y = draw_safe_text(draw, px + 20, curr_y, f"[+] {b}", font_body, TEXT_MUTED, max_width=card_w - 35, line_spacing=4) + 16
            
    # Bottom Code & Github Box
    draw_glass_card(img, 60, 855, 960, 310, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.text((95, 885), "WHY CYPHER MATRIX BUILDS OPEN-SOURCE TOOLING:", font=get_font(FONT_AVENIR, 24, index=2), fill=WHITE)
    draw.rounded_rectangle([95, 935, 985, 1130], radius=14, fill=(10, 16, 24, 255), outline=(0, 240, 255, 120))
    code_lines = [
        "// Connect your Flutter mobile app to Odoo in 3 lines of code:",
        "final client = OdooClient('https://erp.yourcompany.com');",
        "final session = await client.authenticate('production_db', 'admin', 'api_key');",
        "final partners = await client.searchRead('res.partner', domain: [], fields: ['name']);"
    ]
    for i, cl in enumerate(code_lines):
        draw.text((115, 955 + i * 36), cl, font=font_mono, fill=EMERALD if 'OdooClient' in cl or 'authenticate' in cl else TEXT_MUTED if '//' in cl else WHITE)
        
    add_footer(draw, w, h, cta_text="DM 'PROJECT' to integrate Odoo ->", accent=CYAN)
    img.convert('RGB').save(os.path.join(d12_dir, 'Creative_1080x1350.jpg'), quality=95)
    print("Day 12 generated.")

build_day12()

# ==============================================================================
# DAY 13: FLUTTER VS NATIVE DEBATE (4 STORIES, 1080x1920)
# ==============================================================================
d13_dir = os.path.join(WEEK2_DIR, 'Day_13_Flutter_vs_Native_Debate')
os.makedirs(d13_dir, exist_ok=True)

def build_day13():
    def add_story_hdr(im, dr, tag, s_num):
        if os.path.exists(LOGO_PATH):
            logo = Image.open(LOGO_PATH).convert('RGBA')
            logo.thumbnail((200, 70), Image.Resampling.LANCZOS)
            im.alpha_composite(logo, (60, 80))
        draw_pill_badge(dr, 290, 88, tag, get_font(FONT_MENLO, 20), accent_color=CYAN)
        bbox = dr.textbbox((0, 0), s_num, font=get_font(FONT_MENLO, 22))
        dr.text((w_reel - 60 - (bbox[2] - bbox[0]), 92), s_num, font=get_font(FONT_MENLO, 22), fill=TEXT_MUTED)

    # Story 1: Poll
    img, draw = create_base_canvas(w_reel, h_reel, glow_color=(0, 240, 255, 35), glow_pos=(540, 850, 500))
    add_story_hdr(img, draw, "WEEKEND TECH DEBATE", "01 / 04")
    draw_safe_text(draw, 60, 230, "FLUTTER VS NATIVE:\nWHAT WOULD YOU CHOOSE?", get_font(FONT_AVENIR, 50, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img, 60, 420, 960, 420, radius=24, bg=(18, 22, 32, 245), border=(0, 240, 255, 140))
    draw_safe_text(draw, 100, 470, "If you had a $100k budget to launch a cross-platform mobile app in 2027, which stack are you picking?", get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=880, line_spacing=12)
    draw.text((100, 740), "[ VOTE IN THE POLL BELOW ]", font=get_font(FONT_MENLO, 22), fill=CYAN)
    
    draw_glass_card(img, 120, 920, 840, 360, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw.text((w_reel // 2, 980), "PLACE INSTAGRAM POLL STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw.rounded_rectangle([180, 1030, 900, 1110], radius=16, fill=(24, 34, 48, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1070), "FLUTTER (SPEED & SINGLE CODE)", font=get_font(FONT_AVENIR, 24, index=2), fill=WHITE, anchor='mm')
    draw.rounded_rectangle([180, 1140, 900, 1220], radius=16, fill=(34, 20, 26, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1180), "SEPARATE NATIVE (SWIFT + KOTLIN)", font=get_font(FONT_AVENIR, 24, index=2), fill=TEXT_MUTED, anchor='mm')
    
    draw.text((w_reel // 2, 1500), "Tap next to see our production cost analysis ->", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    img.convert('RGB').save(os.path.join(d13_dir, 'Story_01_Poll.jpg'), quality=95)
    
    # Story 2: Cost Analysis
    img2, draw2 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img2, draw2, "FINANCIAL ANALYSIS", "02 / 04")
    draw_safe_text(draw2, 60, 230, "THE REAL-WORLD COST OF SEPARATE NATIVE TEAMS", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960)
    
    draw_glass_card(img2, 60, 380, 960, 530, radius=24, bg=(24, 16, 22, 245), border=(255, 51, 102, 140))
    draw.text((w_reel // 2, 460), "2.4X HIGHER ENGINEERING COST", font=get_font(FONT_AVENIR, 54, index=2), fill=CRIMSON, anchor='mm')
    draw_safe_text(draw2, 100, 530, "Building separate Swift and Kotlin codebases requires two engineering teams, two QA pipelines, and causes constant feature desynchronization.", get_font(FONT_HELVETICA, 26), WHITE, max_width=880, line_spacing=8)
    
    draw_glass_card(img2, 60, 960, 960, 520, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((100, 1005), "WHY 80% OF STARTUPS SWITCH TO FLUTTER:", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD)
    reasons = [
        "1. Single team ships iOS & Android simultaneously",
        "2. 60 FPS hardware rendering via Impeller engine",
        "3. Pixel-perfect identical UI across all screens",
        "4. Saved $60,000+ in first-year maintenance"
    ]
    curr_y = 1065
    for r in reasons:
        curr_y = draw_safe_text(draw2, 100, curr_y, r, get_font(FONT_HELVETICA, 26), WHITE, max_width=880) + 16
        
    draw2.text((w_reel // 2, 1600), "Tap next for when you SHOULD choose Native ->", font=get_font(FONT_HELVETICA, 26), fill=CYAN, anchor='mm')
    img2.convert('RGB').save(os.path.join(d13_dir, 'Story_02_Cost_Analysis.jpg'), quality=95)
    
    # Story 3: When to choose Native
    img3, draw3 = create_base_canvas(w_reel, h_reel, glow_color=(0, 240, 255, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img3, draw3, "HONEST CRITERIA", "03 / 04")
    draw_safe_text(draw3, 60, 230, "WHEN YOU SHOULD STILL BUILD NATIVE", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960)
    
    scenarios = [
        ("01. DEEP HARDWARE & BLUETOOTH LE PROTOCOLS", CYAN, "Custom proprietary medical sensors or firmware communication often benefit from pure native C/C++ bridges."),
        ("02. HEAVY AUGMENTED REALITY (ARKit / ARCore)", EMERALD, "If your core product is complex real-time 3D spatial camera tracking, native Apple APIs provide lowest overhead."),
        ("03. MASSIVE ENTERPRISE LEGACY REPOS", CYAN, "Companies with 200+ native engineers already maintaining a 10-year codebase rarely rewrite in cross-platform.")
    ]
    for idx, (title, col, desc) in enumerate(scenarios):
        cy = 380 + idx * 365
        draw_glass_card(img3, 60, cy, 960, 330, radius=20, bg=(16, 22, 32, 245), border=CARD_BORDER)
        draw_pill_badge(draw3, 95, cy + 22, title, get_font(FONT_MENLO, 19), accent_color=col)
        draw_safe_text(draw3, 95, cy + 85, desc, get_font(FONT_HELVETICA, 25), WHITE, max_width=870, line_spacing=6)
        
    draw3.text((w_reel // 2, 1580), "Tap next to ask our engineers which stack is right for you ->", font=get_font(FONT_HELVETICA, 26), fill=EMERALD, anchor='mm')
    img3.convert('RGB').save(os.path.join(d13_dir, 'Story_03_When_Native.jpg'), quality=95)
    
    # Story 4: Q&A Box
    img4, draw4 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 40), glow_pos=(540, 900, 500))
    add_story_hdr(img4, draw4, "ARCHITECTURE AUDIT", "04 / 04")
    draw_safe_text(draw4, 60, 230, "PLANNING YOUR 2027 APP?\nGET A FREE STACK AUDIT", get_font(FONT_AVENIR, 48, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img4, 100, 460, 880, 520, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw4.text((w_reel // 2, 530), "PLACE INSTAGRAM 'QUESTIONS' STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw4.text((w_reel // 2, 600), "Tell us your app idea & we'll tell you the best tech stack 👇", font=get_font(FONT_AVENIR, 28, index=2), fill=WHITE, anchor='mm')
    draw4.rounded_rectangle([160, 680, 920, 840], radius=18, fill=(24, 32, 46, 255), outline=CARD_BORDER)
    draw4.text((w_reel // 2, 760), "Type your app concept...", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img4, 60, 1040, 960, 360, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw4.text((100, 1085), "CYPHER MATRIX APP CONSULTATIONS:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    points = [
        "✓ Honest architectural analysis (Flutter vs Native)",
        "✓ Offline-first & cloud database scoping",
        "✓ Offensive security & compliance evaluation"
    ]
    curr_y = 1145
    for p in points:
        curr_y = draw_safe_text(draw4, 100, curr_y, p, get_font(FONT_HELVETICA, 24), WHITE, max_width=880) + 16
        
    draw4.text((w_reel // 2, 1580), "CYPHER MATRIX  |  cyphermatrix.io", font=get_font(FONT_MENLO, 22), fill=TEXT_MUTED, anchor='mm')
    img4.convert('RGB').save(os.path.join(d13_dir, 'Story_04_QA_Box.jpg'), quality=95)
    print("Day 13 generated.")

build_day13()

# ==============================================================================
# DAY 14: CLOUD BREACH ANATOMY (S3 & IAM) (5 SLIDES, 1080x1350)
# ==============================================================================
d14_dir = os.path.join(WEEK2_DIR, 'Day_14_Cloud_Breach_S3_IAM')
os.makedirs(d14_dir, exist_ok=True)

def build_day14():
    w, h = w_port, h_port
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 35), glow_pos=(850, 450, 400))
    add_header(img, draw, category="CLOUD SECURITY MASTERCLASS", slide_str="01 / 05", accent=CRIMSON)
    draw_pill_badge(draw, 60, 145, "AWS & CLOUD AUDIT", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 215, "The Anatomy of a Cloud Breach:\nHow an unauthenticated S3 bucket &\nwildcard IAM roles leak 10TB of data.", font_hero, WHITE, max_width=960, line_spacing=10)
    
    # Terminal Card
    card_x, card_y, card_w, card_h = 60, 420, 960, 560
    draw_glass_card(img, card_x, card_y, card_w, card_h, radius=20, bg=(14, 18, 26, 245), border=(255, 51, 102, 120))
    
    t_bar_h = 55
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + t_bar_h], radius=20, fill=(20, 26, 38, 255))
    draw.rectangle([card_x, card_y + 20, card_x + card_w, card_y + t_bar_h], fill=(20, 26, 38, 255))
    draw.line([(card_x, card_y + t_bar_h), (card_x + card_w, card_y + t_bar_h)], fill=CARD_BORDER, width=1)
    draw.ellipse([card_x + 25, card_y + 20, card_x + 39, card_y + 34], fill=(255, 95, 87, 255))
    draw.ellipse([card_x + 49, card_y + 20, card_x + 63, card_y + 34], fill=(254, 187, 43, 255))
    draw.ellipse([card_x + 73, card_y + 20, card_x + 87, card_y + 34], fill=(39, 201, 63, 255))
    draw.text((card_x + 110, card_y + 18), "AWS CLI EXPLOIT SIMULATOR: s3://prod-customer-backups", font=font_mono, fill=TEXT_MUTED)
    draw.text((card_x + card_w - 230, card_y + 18), "PUBLIC ACCESS: OPEN", font=get_font(FONT_MENLO, 19), fill=CRIMSON)
    
    p1_x, panel_y, panel_w, panel_h = card_x + 25, card_y + t_bar_h + 20, 435, 320
    draw.rounded_rectangle([p1_x, panel_y, p1_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 12, 18, 255), outline=(255, 51, 102, 120))
    draw.text((p1_x + 20, panel_y + 20), "1. S3 BUCKET EXPOSURE", font=get_font(FONT_AVENIR, 22, index=2), fill=CRIMSON)
    draw.text((p1_x + 20, panel_y + 55), "Misconfigured ACL Policy:", font=font_mono, fill=TEXT_MUTED)
    s3_checks = [
        "[✗] 'Block Public Access' DISABLED",
        "[✗] 'AllUsers' granted READ perms",
        "[✗] Server-side encryption missing",
        "[✗] Database dumps publicly listable"
    ]
    for i, sc in enumerate(s3_checks):
        draw.text((p1_x + 20, panel_y + 95 + i * 40), sc, font=font_mono, fill=(255, 120, 140, 255))
    draw.line([(p1_x + 20, panel_y + 265), (p1_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p1_x + 20, panel_y + 280), "Outcome: Anonymous Data Exfiltration", font=font_mono, fill=CRIMSON)
    
    p2_x = card_x + 495
    draw.rounded_rectangle([p2_x, panel_y, p2_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 14, 20, 255), outline=(255, 51, 102, 140))
    draw.text((p2_x + 20, panel_y + 20), "2. WILDCARD IAM ROLE LEAK", font=get_font(FONT_AVENIR, 22, index=2), fill=CRIMSON)
    draw.text((p2_x + 20, panel_y + 55), "Over-privileged Service Roles:", font=font_mono, fill=TEXT_MUTED)
    iam_checks = [
        "[✗] Policy: 'Action': 's3:*'",
        "[✗] Resource: 'Resource': '*'",
        "[✗] Leaked lambda role dumped",
        "[✗] Full AWS infrastructure hijacked"
    ]
    for i, ic in enumerate(iam_checks):
        draw.text((p2_x + 20, panel_y + 95 + i * 40), ic, font=font_mono, fill=(255, 120, 140, 255))
    draw.line([(p2_x + 20, panel_y + 265), (p2_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p2_x + 20, panel_y + 280), "Outcome: Full Cloud Account Takeover", font=font_mono, fill=CRIMSON)
    
    summary_y = panel_y + panel_h + 20
    draw.rounded_rectangle([card_x + 25, summary_y, card_x + card_w - 25, summary_y + 90], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((card_x + 45, summary_y + 18), "CLOUD SECURITY PRINCIPLE:", font=font_mono, fill=EMERALD)
    draw_safe_text(draw, card_x + 45, summary_y + 48, "Enforce Least Privilege. Never grant wildcard actions or public bucket ACLs without IAM boundary constraints.", font_body, WHITE, max_width=860, line_spacing=4)
    
    draw_glass_card(img, 60, 1015, 960, 165, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    callout = "Swipe through for the 5-slide guide: AWS IAM least-privilege policies, S3 SCP guardrails, and automated cloud misconfiguration auditing."
    draw_safe_text(draw, 95, 1040, callout, get_font(FONT_HELVETICA, 23), WHITE, max_width=890, line_spacing=6)
    draw.text((95, 1125), "[ Cloud Infrastructure Hardening Guide ]", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to Cloud Defense ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(d14_dir, 'Slide_01_Cover.jpg'), quality=95)
    
    # Slides 2-5
    s_data = [
        ("Slide_02_The_Breach_Chain.jpg", "02 / 05", "THE 4-STEP CLOUD INTRUSION CHAIN", [
            ("STEP 1: S3 BUCKET ENUMERATION", "Attackers scan for company bucket names using automated DNS tools. They find an open staging bucket with anonymous listing enabled."),
            ("STEP 2: CREDENTIAL EXTRACTION", "Inside an unencrypted backup folder, the attacker finds AWS access keys embedded in a `.env.backup` file."),
            ("STEP 3: PRIVILEGE ESCALATION VIA IAM", "The attacker runs `aws iam get-user-policy` and discovers a wildcard `*:*` administrator policy."),
            ("STEP 4: RANSOMWARE & DATA EXFILTRATION", "Attacker encrypts the production RDS database and exfiltrates 10TB of user data.")
        ]),
        ("Slide_03_Hardened_IAM_Policy.jpg", "03 / 05", "HARDENED IAM LEAST-PRIVILEGE POLICY", [
            ("RESTRICT OBJECT PATH SCOPE", "Explicitly limit resource ARN to `arn:aws:s3:::company-prod/uploads/${aws:userid}/*`."),
            ("ENFORCE SECURE TRANSPORT (HTTPS)", "Add bucket policy condition requiring `aws:SecureTransport: true` for all incoming requests."),
            ("DISABLE ANONYMOUS PRINCIPALS", "Enable AWS Account-level 'Block Public Access' across all existing and new S3 buckets.")
        ]),
        ("Slide_04_Cloud_Guardrails.jpg", "04 / 05", "AUTOMATED CLOUD SECURITY GUARDRAILS", [
            ("SERVICE CONTROL POLICIES (SCPs)", "Deploy AWS Organizations SCPs to prevent any engineer from disabling S3 encryption or public block."),
            ("AWS SECURITY HUB & GUARDDUTY", "Enable continuous machine learning threat detection for anomalous API calls and secret exfiltration."),
            ("CYPHER MATRIX CLOUD VAPT", "Our offensive security team tests your multi-cloud environment against lateral movement and IAM privilege escalation.")
        ]),
        ("Slide_05_CTA_Outro.jpg", "05 / 05", "AUDIT YOUR CLOUD INFRASTRUCTURE", [
            ("ARE YOUR AWS / GCP ASSETS SECURE?", "Don't wait for an S3 leak to discover cloud misconfigurations. Cypher Matrix provides comprehensive Cloud Security Posture Reviews."),
            ("SCHEDULE A CLOUD PENETRATION AUDIT", "DM 'SECURITY' to receive our AWS & Cloud Infrastructure VAPT Scoping Checklist."),
            ("VISIT cyphermatrix.io", "Gandhinagar / Ahmedabad • Enterprise Cloud Security Center")
        ])
    ]
    for s_name, s_num, s_title, s_cards in s_data:
        s_img, s_draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 30), glow_pos=(540, 600, 450))
        add_header(s_img, s_draw, category="CLOUD SECURITY MASTERCLASS", slide_str=s_num, accent=CRIMSON)
        s_draw.text((60, 150), s_title, font=get_font(FONT_AVENIR, 42, index=2), fill=WHITE)
        s_draw.text((60, 215), "Production engineering standards applied at Cypher Matrix:", font=font_body, fill=TEXT_MUTED)
        
        for c_i, (c_h, c_desc) in enumerate(s_cards):
            cy = 280 + c_i * 280
            draw_glass_card(s_img, 60, cy, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 95, cy + 22, c_h, font_mono, accent_color=CRIMSON if c_i==0 else CYAN)
            draw_safe_text(s_draw, 95, cy + 80, c_desc, font_body, WHITE, max_width=860, line_spacing=6)
            
        add_footer(s_draw, w, h, cta_text="Swipe to next ->" if s_num != "05 / 05" else "DM 'SECURITY' ->", accent=CRIMSON)
        s_img.convert('RGB').save(os.path.join(d14_dir, s_name), quality=95)
    print("Day 14 generated.")

build_day14()
print("Week 02 completely generated successfully!")
