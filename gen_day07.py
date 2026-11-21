import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

DAY7_DIR = os.path.join(WEEK1_DIR, 'Day_07_API_Security_IDOR')
os.makedirs(DAY7_DIR, exist_ok=True)

# Slide 1: Cover (Clean Terminal Interface: Zero cropped image tiles, zero meaningless pills)
def create_slide_1():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 35), glow_pos=(850, 450, 400))
    add_header(img, draw, category="API SECURITY MASTERCLASS", slide_str="01 / 05", accent=CRIMSON)
    
    draw_pill_badge(draw, 60, 145, "CRITICAL API VULNERABILITY (OWASP API1)", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_sub = get_font(FONT_HELVETICA, 23)
    font_mono = get_font(FONT_MENLO, 18)
    font_mono_bold = get_font(FONT_MENLO, 19)
    font_card_head = get_font(FONT_AVENIR, 22, index=2)
    
    title_text = "How 1 missing authorization check\nexposes 500,000 user profiles.\n(The IDOR Exploit)"
    draw_safe_text(draw, 60, 215, title_text, font_hero, WHITE, max_width=960, line_spacing=10)
    
    card_x, card_y, card_w, card_h = 60, 420, 960, 560
    draw_glass_card(img, card_x, card_y, card_w, card_h, radius=20, bg=(14, 18, 26, 245), border=(255, 51, 102, 120))
    
    # Terminal Title Bar
    t_bar_h = 55
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + t_bar_h], radius=20, fill=(20, 26, 38, 255))
    draw.rectangle([card_x, card_y + 20, card_x + card_w, card_y + t_bar_h], fill=(20, 26, 38, 255))
    draw.line([(card_x, card_y + t_bar_h), (card_x + card_w, card_y + t_bar_h)], fill=CARD_BORDER, width=1)
    
    draw.ellipse([card_x + 25, card_y + 20, card_x + 39, card_y + 34], fill=(255, 95, 87, 255))
    draw.ellipse([card_x + 49, card_y + 20, card_x + 63, card_y + 34], fill=(254, 187, 43, 255))
    draw.ellipse([card_x + 73, card_y + 20, card_x + 87, card_y + 34], fill=(39, 201, 63, 255))
    
    draw.text((card_x + 110, card_y + 18), "API GATEWAY LOG: /api/v1/invoices/{id}", font=font_mono, fill=TEXT_MUTED)
    draw.text((card_x + card_w - 240, card_y + 18), "IDOR EXPLOIT DETECTED", font=font_mono_bold, fill=CRIMSON)
    
    panel_y = card_y + t_bar_h + 20
    panel_h = 320
    panel_w = 435
    
    # Left Sub-Panel: Legitimate Request
    p1_x = card_x + 25
    draw.rounded_rectangle([p1_x, panel_y, p1_x + panel_w, panel_y + panel_h], radius=14, fill=(10, 16, 24, 255), outline=(40, 60, 85, 255))
    draw.text((p1_x + 20, panel_y + 20), "1. LEGITIMATE REQUEST", font=font_card_head, fill=CYAN)
    draw.text((p1_x + 20, panel_y + 55), "User #1042 requests own data:", font=font_mono, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([p1_x + 15, panel_y + 90, p1_x + panel_w - 15, panel_y + 240], radius=10, fill=(14, 20, 30, 255), outline=CARD_BORDER)
    draw.text((p1_x + 25, panel_y + 105), "GET /api/v1/invoices/1042", font=font_mono, fill=WHITE)
    draw.text((p1_x + 25, panel_y + 135), "Authorization: Bearer <user_1042>", font=font_mono, fill=CYAN)
    draw.text((p1_x + 25, panel_y + 175), "SERVER: 200 OK", font=font_mono_bold, fill=EMERALD)
    draw.text((p1_x + 25, panel_y + 205), "[Valid User 1042 Invoices Returned]", font=font_mono, fill=TEXT_MUTED)
    
    draw.line([(p1_x + 20, panel_y + 265), (p1_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p1_x + 20, panel_y + 280), "Outcome: Valid Authorized Call", font=font_mono, fill=CYAN)
    
    # Right Sub-Panel: IDOR Parameter Manipulation
    p2_x = card_x + 495
    draw.rounded_rectangle([p2_x, panel_y, p2_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 12, 18, 255), outline=(255, 51, 102, 140))
    draw.text((p2_x + 20, panel_y + 20), "2. TAMPERED PARAMETER (IDOR)", font=font_card_head, fill=CRIMSON)
    draw.text((p2_x + 20, panel_y + 55), "Attacker requests User #1043 data:", font=font_mono, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([p2_x + 15, panel_y + 90, p2_x + panel_w - 15, panel_y + 240], radius=10, fill=(30, 14, 20, 255), outline=(255, 51, 102, 80))
    draw.text((p2_x + 25, panel_y + 105), "GET /api/v1/invoices/1043", font=font_mono, fill=(255, 90, 90, 255))
    draw.text((p2_x + 25, panel_y + 135), "Authorization: Bearer <user_1042>", font=font_mono, fill=WHITE)
    draw.text((p2_x + 25, panel_y + 175), "SERVER: 200 OK", font=font_mono_bold, fill=CRIMSON)
    draw.text((p2_x + 25, panel_y + 205), "[CRITICAL LEAK: Leaks User 1043 Data!]", font=font_mono, fill=CRIMSON)
    
    draw.line([(p2_x + 20, panel_y + 265), (p2_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p2_x + 20, panel_y + 280), "Outcome: Broken Object Level Auth", font=font_mono_bold, fill=CRIMSON)
    
    # Bottom Summary Bar inside Card
    summary_y = panel_y + panel_h + 20
    draw.rounded_rectangle([card_x + 25, summary_y, card_x + card_w - 25, summary_y + 90], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((card_x + 45, summary_y + 18), "ATTACK REALITY:", font=font_mono_bold, fill=EMERALD)
    insight_text = "With a 10-line Python loop script, an attacker can dump 500,000 customer accounts in 10 minutes without triggering authentication alerts."
    draw_safe_text(draw, card_x + 45, summary_y + 48, insight_text, font_sub, WHITE, max_width=860, line_spacing=4)
    
    # Bottom Callout Box
    draw_glass_card(img, 60, 1015, 960, 165, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    callout = "Swipe through for the attack anatomy, vulnerable vs patched code, and the RBAC middleware you must deploy in your next sprint."
    draw_safe_text(draw, 95, 1040, callout, font_sub, WHITE, max_width=890, line_spacing=6)
    draw.text((95, 1125), "[ 5-Slide Developer Guide • Save For Your Team ]", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to The Exploit ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY7_DIR, 'Slide_01_Cover.jpg'), quality=95)
    print("Re-generated Day 7 Slide 1 (Clean Terminal, Zero Tiles/Pills)")

# Slide 2: The Attack Anatomy
def create_slide_2():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="API SECURITY MASTERCLASS", slide_str="02 / 05", accent=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "THE ANATOMY OF AN IDOR ATTACK", font=font_title, fill=WHITE)
    draw.text((60, 215), "How an attacker dumps your entire database using a 10-line script:", font=font_body, fill=TEXT_MUTED)
    
    draw_glass_card(img, 60, 275, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 300, "STEP 1: INSPECTING LEGITIMATE REQUEST", font_mono, accent_color=CYAN)
    draw.text((90, 355), "User logs in legitimately as User #1042 and downloads their invoice:", font=font_body, fill=TEXT_MUTED)
    draw.rounded_rectangle([90, 395, 1000, 485], radius=10, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 415), "GET /api/v1/invoices/1042 HTTP/1.1", font=font_mono, fill=WHITE)
    draw.text((115, 445), "Authorization: Bearer <valid_token_for_user_1042>", font=font_mono, fill=EMERALD)
    
    draw_glass_card(img, 60, 560, 960, 275, radius=18, bg=(24, 16, 22, 240), border=(255, 51, 102, 140))
    draw_pill_badge(draw, 90, 585, "STEP 2: PARAMETER TAMPERING (THE EXPLOIT)", font_mono, accent_color=CRIMSON)
    draw.text((90, 640), "Attacker simply changes the ID in the URL to User #1043:", font=font_body, fill=TEXT_MUTED)
    draw.rounded_rectangle([90, 680, 1000, 785], radius=10, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 700), "GET /api/v1/invoices/1043 HTTP/1.1  <-- CHANGED ID", font=font_mono, fill=(255, 90, 90, 255))
    draw.text((115, 728), "Authorization: Bearer <valid_token_for_user_1042>", font=font_mono, fill=WHITE)
    draw.text((115, 755), "SERVER STATUS: 200 OK (Leaks User 1043 Confidential Records!)", font=font_mono, fill=CRIMSON)
    
    draw_glass_card(img, 60, 865, 960, 280, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 890, "STEP 3: AUTOMATED MASS ENUMERATION", font_mono, accent_color=CYAN)
    draw.text((90, 945), "The attacker writes a basic loop script iterating IDs from 1 to 500,000:", font=font_body, fill=TEXT_MUTED)
    draw.rounded_rectangle([90, 985, 1000, 1100], radius=10, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 1005), "for id in range(1, 500000):", font=font_mono, fill=EMERALD)
    draw.text((150, 1035), "data = requests.get(f'/api/v1/invoices/{id}', headers=auth)", font=font_mono, fill=WHITE)
    draw.text((150, 1065), "save_to_leak_database(data)  # 500k records dumped in 10 mins", font=font_mono, fill=(255, 90, 90, 255))
    
    add_footer(draw, w, h, cta_text="Swipe to Code Fix ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY7_DIR, 'Slide_02_Attack_Anatomy.jpg'), quality=95)
    print("Re-generated Day 7 Slide 2 (Bounds Guaranteed)")

# Slide 3: Code Comparison
def create_slide_3():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="API SECURITY MASTERCLASS", slide_str="03 / 05", accent=EMERALD)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "VULNERABLE VS HARDENED CODE", font=font_title, fill=WHITE)
    draw.text((60, 215), "How to implement strict object-level authorization in your backend:", font=font_body, fill=TEXT_MUTED)
    
    draw_glass_card(img, 60, 270, 960, 420, radius=20, bg=(24, 16, 22, 240), border=(255, 51, 102, 140))
    draw_pill_badge(draw, 90, 295, "FLAWED: CHECKS AUTHENTICATION ONLY", font_mono, accent_color=CRIMSON)
    draw.text((90, 350), "Server verifies who the user is, but never checks if they own the object:", font=font_body, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([90, 395, 1000, 655], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    flawed_code = [
        "// Insecure Controller Route",
        "app.get('/api/v1/invoices/:id', requireAuth, async (req, res) => {",
        "  // VULNERABLE: Direct database query using client parameter",
        "  const invoice = await db.invoices.findById(req.params.id);",
        "  if (!invoice) return res.status(404).json({ error: 'Not found' });",
        "  res.json(invoice); // Returns data to anyone with a valid JWT!",
        "});"
    ]
    for idx, cl in enumerate(flawed_code):
        col = CRIMSON if 'VULNERABLE' in cl or 'Returns data' in cl else TEXT_MUTED if '//' in cl else WHITE
        draw.text((115, 415 + idx * 32), cl, font=font_mono, fill=col)
        
    draw_glass_card(img, 60, 720, 960, 470, radius=20, bg=(14, 24, 20, 240), border=(0, 255, 136, 140))
    draw_pill_badge(draw, 90, 745, "HARDENED: CRYPTOGRAPHIC TENANT BOUNDARY & RBAC", font_mono, accent_color=EMERALD)
    draw.text((90, 800), "Server strictly binds the object query to the authenticated tenant context:", font=font_body, fill=TEXT_MUTED)
    
    draw.rounded_rectangle([90, 845, 1000, 1150], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    hardened_code = [
        "// Secure Controller Route",
        "app.get('/api/v1/invoices/:id', requireAuth, async (req, res) => {",
        "  // HARDENED: Query binds BOTH object ID and authenticated orgId",
        "  const invoice = await db.invoices.findOne({",
        "    id: req.params.id,",
        "    organizationId: req.user.orgId // Cryptographically verified",
        "  });",
        "  if (!invoice) return res.status(403).json({ error: 'Access Denied' });",
        "  res.json(invoice);",
        "});"
    ]
    for idx, cl in enumerate(hardened_code):
        col = EMERALD if 'HARDENED' in cl or 'Cryptographically' in cl else TEXT_MUTED if '//' in cl else WHITE
        draw.text((115, 865 + idx * 30), cl, font=font_mono, fill=col)
        
    add_footer(draw, w, h, cta_text="Swipe to Scanners vs VAPT ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY7_DIR, 'Slide_03_Code_Comparison.jpg'), quality=95)
    print("Re-generated Day 7 Slide 3 (Bounds Guaranteed)")

# Slide 4: Why Scanners Miss IDOR
def create_slide_4():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="API SECURITY MASTERCLASS", slide_str="04 / 05", accent=CYAN)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "WHY AUTOMATED SCANNERS MISS IDOR", font=font_title, fill=WHITE)
    draw.text((60, 215), "Why passing automated CI/CD security tools does not guarantee safety:", font=font_body, fill=TEXT_MUTED)
    
    reasons = [
        ("01. SCANNERS LACK BUSINESS LOGIC CONTEXT", CRIMSON, [
            "Automated tools fuzz for SQLi, XSS, and header errors.",
            "They cannot distinguish whether User A is authorized to view Invoice B.",
            "To the scanner, a '200 OK' response looks like successful operation."
        ]),
        ("02. MULTI-TENANT ISOLATION REQUIRES DUAL TOKENS", CYAN, [
            "Detecting IDOR requires logging in with two separate tenant credentials",
            "and attempting cross-tenant object manipulation (Privilege Escalation).",
            "Generic scanners test endpoints in isolation with a single token."
        ]),
        ("03. OFFENSIVE HUMAN PENETRATION TESTING (VAPT) IS ESSENTIAL", EMERALD, [
            "Offensive security engineers map out data models and role hierarchies.",
            "We systematically test horizontal & vertical authorization boundaries.",
            "Uncovers logic leaks before malicious actors script mass database dumps."
        ])
    ]
    
    for idx, (title, col, bullets) in enumerate(reasons):
        cy = 280 + idx * 280
        draw_glass_card(img, 60, cy, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw_pill_badge(draw, 95, cy + 22, title, font_mono, accent_color=col)
        curr_y = cy + 75
        for b in bullets:
            curr_y = draw_safe_text(draw, 95, curr_y, f"[+] {b}", font_body, WHITE, max_width=860, line_spacing=4) + 8
                
    add_footer(draw, w, h, cta_text="Swipe to Secure Your APIs ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY7_DIR, 'Slide_04_Scanners_vs_VAPT.jpg'), quality=95)
    print("Re-generated Day 7 Slide 4 (Bounds Guaranteed)")

# Slide 5: Outro & API VAPT CTA
def create_slide_5():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(540, 600, 500))
    add_header(img, draw, category="API SECURITY MASTERCLASS", slide_str="05 / 05", accent=EMERALD)
    
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 260), Image.Resampling.LANCZOS)
        lw, lh = logo.size
        img.alpha_composite(logo, (w // 2 - lw // 2, 200))
        
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_sub = get_font(FONT_HELVETICA, 26)
    font_mono = get_font(FONT_MENLO, 20)
    
    draw.text((w // 2, 480), "HARDEN YOUR API INFRASTRUCTURE", font=font_hero, fill=WHITE, anchor='mm')
    draw.text((w // 2, 540), "REST • GraphQL • Microservices • Mobile Gateways", font=font_sub, fill=CYAN, anchor='mm')
    
    draw_glass_card(img, 100, 630, 880, 420, radius=24, bg=(16, 22, 34, 250), border=(0, 255, 136, 180))
    draw.text((w // 2, 690), "SCHEDULE AN API PENETRATION AUDIT", font=get_font(FONT_AVENIR, 30, index=2), fill=EMERALD, anchor='mm')
    
    pitch = (
        "Our offensive cybersecurity team will systematically audit your\n"
        "API endpoints, role-based access controls, and cloud gateways—\n"
        "identifying IDOR and business logic bugs before attackers exploit them."
    )
    for i, l in enumerate(pitch.split('\n')):
        draw.text((w // 2, 750 + i * 36), l, font=font_sub, fill=WHITE, anchor='mm')
        
    btn_w, btn_h = 740, 80
    bx = (w - btn_w) // 2
    by = 910
    draw.rounded_rectangle([bx, by, bx + btn_w, by + btn_h], radius=16, fill=EMERALD)
    draw.text((w // 2, by + btn_h // 2), "DM 'SECURITY' FOR AN API VAPT SCOPING AUDIT", font=get_font(FONT_AVENIR, 23, index=2), fill=(8, 10, 15, 255), anchor='mm')
    
    draw.text((w // 2, 1140), "CYPHER MATRIX TECHNOLOGIES  |  cyphermatrix.io", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    draw.text((w // 2, 1180), "Gandhinagar / Ahmedabad • Enterprise Cybersecurity Center", font=font_mono, fill=CYAN, anchor='mm')
    
    add_footer(draw, w, h, cta_text="Share with a Backend Lead ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY7_DIR, 'Slide_05_CTA_Outro.jpg'), quality=95)
    print("Re-generated Day 7 Slide 5 (Bounds Guaranteed)")

create_slide_1()
create_slide_2()
create_slide_3()
create_slide_4()
create_slide_5()
