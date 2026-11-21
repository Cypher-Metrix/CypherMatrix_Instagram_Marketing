import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

DAY1_DIR = os.path.join(WEEK1_DIR, 'Day_01_OWASP_Mobile_Top10')
os.makedirs(DAY1_DIR, exist_ok=True)

# Slide 1: Cover (Completely Clean & Purpose-Driven: No random image tiles, no meaningless pills)
def create_slide_1():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 30), glow_pos=(850, 450, 450))
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="01 / 07", accent=CRIMSON)
    
    draw_pill_badge(draw, 60, 145, "OFFENSIVE SECURITY AUDIT", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 48, index=2)
    title_text = "Your mobile app passed QA testing.\nHere is why an ethical hacker can still dump your database in 40 seconds."
    draw_safe_text(draw, 60, 215, title_text, font_title, WHITE, max_width=960, line_spacing=12)
    
    # Clean Full-Width Terminal Card (No weird image bars, no floating meaningless pills)
    card_x, card_y, card_w, card_h = 60, 420, 960, 560
    draw_glass_card(img, card_x, card_y, card_w, card_h, radius=20, bg=(14, 18, 26, 245), border=(255, 51, 102, 120))
    
    # Terminal Title Bar
    t_bar_h = 55
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + t_bar_h], radius=20, fill=(20, 26, 38, 255))
    draw.rectangle([card_x, card_y + 20, card_x + card_w, card_y + t_bar_h], fill=(20, 26, 38, 255))
    draw.line([(card_x, card_y + t_bar_h), (card_x + card_w, card_y + t_bar_h)], fill=CARD_BORDER, width=1)
    
    # 3 Window dots
    draw.ellipse([card_x + 25, card_y + 20, card_x + 39, card_y + 34], fill=(255, 95, 87, 255))
    draw.ellipse([card_x + 49, card_y + 20, card_x + 63, card_y + 34], fill=(254, 187, 43, 255))
    draw.ellipse([card_x + 73, card_y + 20, card_x + 87, card_y + 34], fill=(39, 201, 63, 255))
    
    font_mono = get_font(FONT_MENLO, 18)
    font_mono_bold = get_font(FONT_MENLO, 19)
    font_card_head = get_font(FONT_AVENIR, 22, index=2)
    font_body = get_font(FONT_HELVETICA, 21)
    
    draw.text((card_x + 110, card_y + 18), "AUDIT LOG: MOBILE_STAGING_v2.4_RELEASE.apk", font=font_mono, fill=TEXT_MUTED)
    draw.text((card_x + card_w - 240, card_y + 18), "STATUS: 82% FAILED", font=font_mono_bold, fill=CRIMSON)
    
    # Left Sub-Panel: Functional QA
    panel_y = card_y + t_bar_h + 20
    panel_h = 320
    panel_w = 435
    
    # QA Box
    p1_x = card_x + 25
    draw.rounded_rectangle([p1_x, panel_y, p1_x + panel_w, panel_y + panel_h], radius=14, fill=(10, 16, 24, 255), outline=(40, 60, 85, 255))
    draw.text((p1_x + 20, panel_y + 20), "1. FUNCTIONAL QA RESULTS", font=font_card_head, fill=CYAN)
    draw.text((p1_x + 20, panel_y + 55), "Tests what the code DOES:", font=font_mono, fill=TEXT_MUTED)
    
    qa_checks = [
        "[✓] User Login & Registration: PASS",
        "[✓] In-App Payment Checkout: PASS",
        "[✓] UI Layout & Rendering: PASS (60 FPS)",
        "[✓] API Data Loading: PASS"
    ]
    for i, qc in enumerate(qa_checks):
        draw.text((p1_x + 20, panel_y + 95 + i * 40), qc, font=font_mono, fill=(180, 220, 255, 255))
        
    draw.line([(p1_x + 20, panel_y + 265), (p1_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p1_x + 20, panel_y + 280), "Outcome: Functional & Bug-Free.", font=font_mono, fill=CYAN)
    
    # Right Sub-Panel: Offensive VAPT
    p2_x = card_x + 495
    draw.rounded_rectangle([p2_x, panel_y, p2_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 12, 18, 255), outline=(255, 51, 102, 140))
    draw.text((p2_x + 20, panel_y + 20), "2. OFFENSIVE VAPT RESULTS", font=font_card_head, fill=CRIMSON)
    draw.text((p2_x + 20, panel_y + 55), "Tests what the code PERMITS:", font=font_mono, fill=TEXT_MUTED)
    
    vapt_checks = [
        "[✗] APK Decompiled: API Key Leaked",
        "[✗] TLS Pinning: Bypass via Burp Suite",
        "[✗] SQLite DB: Unencrypted Tokens",
        "[✗] Biometrics: Frida Hook Bypass"
    ]
    for i, vc in enumerate(vapt_checks):
        draw.text((p2_x + 20, panel_y + 95 + i * 40), vc, font=font_mono, fill=(255, 120, 140, 255))
        
    draw.line([(p2_x + 20, panel_y + 265), (p2_x + panel_w - 20, panel_y + 265)], fill=CARD_BORDER, width=1)
    draw.text((p2_x + 20, panel_y + 280), "Outcome: CRITICAL EXPOSURE (40 Secs)", font=font_mono_bold, fill=CRIMSON)
    
    # Bottom Audit Summary Bar inside Card
    summary_y = panel_y + panel_h + 20
    draw.rounded_rectangle([card_x + 25, summary_y, card_x + card_w - 25, summary_y + 90], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((card_x + 45, summary_y + 18), "OFFENSIVE SECURITY INSIGHT:", font=font_mono_bold, fill=EMERALD)
    insight_text = "Attackers don't need zero-days. They exploit exposed secrets, unpinned TLS, and missing authorization."
    draw_safe_text(draw, card_x + 45, summary_y + 48, insight_text, font_body, WHITE, max_width=860, line_spacing=4)
    
    # Bottom Callout Box
    draw_glass_card(img, 60, 1015, 960, 165, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    font_callout = get_font(FONT_HELVETICA, 23)
    callout_text = (
        "Swipe through this 7-slide teardown for the critical vulnerabilities "
        "found in early-stage startups and how our VAPT team patches them before production."
    )
    draw_safe_text(draw, 95, 1040, callout_text, font_callout, WHITE, max_width=890, line_spacing=6)
    draw.text((95, 1125), "[ 16-Minute Read Condensed Into 60 Seconds ]", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to inspect ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_01_Cover.jpg'), quality=95)
    print("Re-generated Day 1 Slide 1 (Tiles & Pills Completely Removed)")

# Slide 2: QA vs Security
def create_slide_2():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="02 / 07", accent=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 44, index=2)
    font_card_title = get_font(FONT_AVENIR, 28, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 19)
    
    draw.text((60, 150), "QA TESTING vs OFFENSIVE SECURITY", font=font_title, fill=WHITE)
    draw.text((60, 215), "Why high test coverage does NOT mean secure code:", font=font_body, fill=TEXT_MUTED)
    
    # Left Card: QA
    draw_glass_card(img, 60, 280, 465, 540, radius=20, bg=(18, 24, 34, 240), border=(45, 60, 85, 255))
    draw_pill_badge(draw, 85, 305, "FUNCTIONAL QA", font_mono, accent_color=CYAN)
    draw.text((85, 370), "What It Validates:", font=font_card_title, fill=WHITE)
    qa_points = [
        "- Can user click login button?",
        "- Does checkout process charge card?",
        "- Are UI screens rendering smooth?",
        "- Is API payload received correctly?",
        "- Do error toasts show on failed inputs?"
    ]
    curr_y = 430
    for pt in qa_points:
        curr_y = draw_safe_text(draw, 85, curr_y, pt, font_body, TEXT_MUTED, max_width=415, line_spacing=6) + 6
    draw.text((85, 760), "Verdict: Validates expected behavior.", font=font_mono, fill=CYAN)
    
    # Right Card: VAPT
    draw_glass_card(img, 555, 280, 465, 540, radius=20, bg=(24, 16, 24, 240), border=(255, 51, 102, 140))
    draw_pill_badge(draw, 580, 305, "OFFENSIVE VAPT", font_mono, accent_color=CRIMSON)
    draw.text((580, 370), "What Attackers Exploit:", font=font_card_title, fill=WHITE)
    vapt_points = [
        "- Can token be replayed across users?",
        "- Are private API keys in client APK?",
        "- Can TLS cert pinning be bypassed?",
        "- Is SQLite database encrypted at rest?",
        "- Does server authorize object ID?"
    ]
    curr_y2 = 430
    for pt in vapt_points:
        curr_y2 = draw_safe_text(draw, 580, curr_y2, pt, font_body, TEXT_MUTED, max_width=415, line_spacing=6) + 6
    draw.text((580, 760), "Verdict: Discovers malicious exploits.", font=font_mono, fill=CRIMSON)
    
    # Stat Banner
    draw_glass_card(img, 60, 850, 960, 330, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 120))
    draw.text((95, 885), "THE HARD REALITY FROM 100+ AUDITS:", font=font_card_title, fill=EMERALD)
    stat_desc = (
        "In 9 out of 10 startup applications we audit, attackers do not need zero-days. "
        "They exploit hardcoded secret keys, unpinned endpoints, and broken authorization. "
        "Swipe to inspect the OWASP Mobile Top 10 vulnerabilities and fixes."
    )
    draw_safe_text(draw, 95, 940, stat_desc, font_body, WHITE, max_width=890, line_spacing=10)
    
    add_footer(draw, w, h, cta_text="Swipe to M1 & M2 ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_02_QA_vs_Security.jpg'), quality=95)
    print("Re-generated Day 1 Slide 2")

# Slide 3: M1 & M2
def create_slide_3():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="03 / 07", accent=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_card_title = get_font(FONT_AVENIR, 26, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "M1: CREDENTIAL LEAKS & M2: SUPPLY CHAIN", font=font_title, fill=WHITE)
    draw.text((60, 215), "The two most prevalent vulnerabilities in mobile applications today.", font=font_body, fill=TEXT_MUTED)
    
    # Card 1: M1
    draw_glass_card(img, 60, 270, 960, 420, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 295, "OWASP M1: IMPROPER CREDENTIAL USAGE", font_mono, accent_color=CRIMSON)
    draw.text((90, 350), "The Exploit: Hardcoded Secrets in APK / IPA", font=font_card_title, fill=WHITE)
    m1_exploit = "Decompiling your app with JADX-GUI reveals AWS keys, Stripe secret keys, and Firebase master admin tokens stored in strings.xml or .env files."
    draw_safe_text(draw, 90, 395, m1_exploit, font_body, TEXT_MUTED, max_width=880, line_spacing=6)
    
    # Code snippet block
    draw.rounded_rectangle([90, 480, 1000, 650], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 500), "// VULNERABLE: Hardcoded API Secret in App", font=font_mono, fill=(255, 90, 90, 255))
    draw.text((115, 532), "const STRIPE_KEY = 'sk_live_51M78...'  // Extracted in 5 secs", font=font_mono, fill=(220, 220, 220, 255))
    draw.text((115, 574), "// PATCHED: Ephemeral Tokens via Backend Gateway", font=font_mono, fill=EMERALD)
    draw.text((115, 606), "final sessionToken = await authGateway.requestEphemeralToken();", font=font_mono, fill=WHITE)
    
    # Card 2: M2
    draw_glass_card(img, 60, 720, 960, 470, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 745, "OWASP M2: INADEQUATE SUPPLY CHAIN SECURITY", font_mono, accent_color=CRIMSON)
    draw.text((90, 800), "The Exploit: Poisoned Third-Party Packages", font=font_card_title, fill=WHITE)
    m2_exploit = "An unvetted open-source pub.dev or npm package silently injects analytics spyware, capturing clipboard data and keystrokes on checkout screens."
    draw_safe_text(draw, 90, 845, m2_exploit, font_body, TEXT_MUTED, max_width=880, line_spacing=6)
    
    draw.rounded_rectangle([90, 935, 1000, 1140], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 955), "CYPHER MATRIX SUPPLY CHAIN REMEDIATION:", font=font_mono, fill=EMERALD)
    draw.text((115, 995), "1. Lock dependency hash checksums in pubspec.lock", font=font_body, fill=WHITE)
    draw.text((115, 1035), "2. Automated SCA vulnerability scanning in CI/CD pipeline", font=font_body, fill=WHITE)
    draw.text((115, 1075), "3. Strip unused dynamic reflection symbols from release builds", font=font_body, fill=WHITE)
    
    add_footer(draw, w, h, cta_text="Swipe to M3 & M4 ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_03_M1_M2_Vulnerabilities.jpg'), quality=95)
    print("Re-generated Day 1 Slide 3")

# Slide 4: M3 & M4
def create_slide_4():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="04 / 07", accent=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_card_title = get_font(FONT_AVENIR, 26, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "M3: AUTHENTICATION & M4: VALIDATION", font=font_title, fill=WHITE)
    draw.text((60, 215), "How attackers hijack user accounts without needing passwords.", font=font_body, fill=TEXT_MUTED)
    
    # Card M3
    draw_glass_card(img, 60, 270, 960, 430, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 295, "OWASP M3: INSECURE AUTHENTICATION / AUTHORIZATION", font_mono, accent_color=CRIMSON)
    draw.text((90, 350), "The Exploit: Client-Side Biometric Bypass", font=font_card_title, fill=WHITE)
    m3_text = "If your biometric lock only returns a local boolean (true/false) in Flutter, attackers hook Frida to force return true—bypassing FaceID entirely."
    draw_safe_text(draw, 90, 395, m3_text, font_body, TEXT_MUTED, max_width=880, line_spacing=6)
    
    draw.rounded_rectangle([90, 480, 1000, 660], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 500), "// FLAWED: Client-only biometric check", font=font_mono, fill=(255, 90, 90, 255))
    draw.text((115, 532), "if (await localAuth.authenticate()) { navigateToWallet(); }", font=font_mono, fill=(200, 200, 200, 255))
    draw.text((115, 574), "// HARDENED: Cryptographic KeyStore / Secure Enclave Signature", font=font_mono, fill=EMERALD)
    draw.text((115, 606), "final signature = await SecureEnclave.signChallenge(nonce);", font=font_mono, fill=WHITE)
    draw.text((115, 636), "await server.verifySignature(signature, userId);", font=font_mono, fill=CYAN)
    
    # Card M4
    draw_glass_card(img, 60, 730, 960, 460, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 755, "OWASP M4: INSUFFICIENT INPUT / OUTPUT VALIDATION", font_mono, accent_color=CRIMSON)
    draw.text((90, 810), "The Exploit: Deep Link Hijacking & SQLi in Local DB", font=font_card_title, fill=WHITE)
    m4_text = "Unsanitized custom URI schemes allow malicious websites to trigger internal intents, stealing cached session cookies from SQLite storage."
    draw_safe_text(draw, 90, 855, m4_text, font_body, TEXT_MUTED, max_width=880, line_spacing=6)
    
    draw.rounded_rectangle([90, 940, 1000, 1145], radius=12, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    draw.text((115, 965), "DEFENSE CHECKLIST FOR LEAD ENGINEERS:", font=font_mono, fill=EMERALD)
    draw.text((115, 1005), "- Strict input validation regex on deep link payloads", font=font_body, fill=WHITE)
    draw.text((115, 1045), "- Parameterized SQL queries with SQLCipher encryption at rest", font=font_body, fill=WHITE)
    draw.text((115, 1085), "- Disable Android exported activities unless explicitly required", font=font_body, fill=WHITE)
    
    add_footer(draw, w, h, cta_text="Swipe to M5 & TLS Pinning ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_04_M3_M4_Vulnerabilities.jpg'), quality=95)
    print("Re-generated Day 1 Slide 4")

# Slide 5: M5
def create_slide_5():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="05 / 07", accent=CRIMSON)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_card_title = get_font(FONT_AVENIR, 26, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "M5: INSECURE COMMUNICATION & TLS PINNING", font=font_title, fill=WHITE)
    draw.text((60, 215), "Why HTTPS alone does NOT protect your mobile app from proxy snooping.", font=font_body, fill=TEXT_MUTED)
    
    draw_glass_card(img, 60, 270, 960, 920, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
    draw_pill_badge(draw, 90, 295, "OWASP M5: MAN-IN-THE-MIDDLE (MitM) THREAT", font_mono, accent_color=CRIMSON)
    draw.text((90, 350), "How Hackers Intercept Your Traffic with Burp Suite", font=font_card_title, fill=WHITE)
    
    mitm_text = (
        "An attacker installs a custom CA certificate on a rooted or jailbroken device. "
        "Because the app trusts the device root store, all outgoing financial transactions, "
        "bearer tokens, and personal data are decrypted in clear text."
    )
    draw_safe_text(draw, 90, 395, mitm_text, font_body, TEXT_MUTED, max_width=880, line_spacing=6)
    
    # Interception flow
    draw.rounded_rectangle([90, 490, 1000, 670], radius=14, fill=(10, 14, 22, 255), outline=(255, 51, 102, 100))
    draw.text((115, 515), "[Mobile App] ---> (Intercepted by Attacker Proxy) ---> [Your API Server]", font=font_mono, fill=(255, 90, 90, 255))
    draw.text((115, 555), "Payload: Authorization: Bearer eyJhbGciOi... [DUMPED]", font=font_mono, fill=(200, 200, 200, 255))
    draw.text((115, 605), "SOLUTION: Strict Certificate Pinning (Pin SHA-256 Public Key)", font=font_mono, fill=EMERALD)
    
    draw.text((90, 705), "PRODUCTION FLUTTER / DART SSL PINNING FIX:", font=font_card_title, fill=EMERALD)
    draw.rounded_rectangle([90, 755, 1000, 1140], radius=14, fill=(10, 12, 18, 255), outline=CARD_BORDER)
    code_lines = [
        "// Enforce SHA-256 Public Key Pinning",
        "final dio = Dio();",
        "(dio.httpClientAdapter as IOHttpClientAdapter).createHttpClient = () {",
        "  final client = HttpClient();",
        "  client.badCertificateCallback = (cert, host, port) {",
        "    final expectedHash = 'sha256/k20YWfoAyYv16v6xSm5jUx71T8=...';",
        "    return cert.sha256Digest == expectedHash; // Block rogue CAs",
        "  };",
        "  return client;",
        "};"
    ]
    for i, cl in enumerate(code_lines):
        color = EMERALD if 'sha256' in cl or 'return cert' in cl else TEXT_MUTED if '//' in cl else WHITE
        draw.text((115, 780 + i * 35), cl, font=font_mono, fill=color)
        
    add_footer(draw, w, h, cta_text="Swipe to VAPT Blueprint ->", accent=CRIMSON)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_05_TLS_Pinning_MitM.jpg'), quality=95)
    print("Re-generated Day 1 Slide 5")

# Slide 6: VAPT Checklist
def create_slide_6():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h)
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="06 / 07", accent=EMERALD)
    
    font_title = get_font(FONT_AVENIR, 42, index=2)
    font_card_title = get_font(FONT_AVENIR, 26, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((60, 150), "THE CYPHER MATRIX PRE-LAUNCH VAPT AUDIT", font=font_title, fill=WHITE)
    draw.text((60, 215), "Our 3-tier offensive security testing blueprint before app store release.", font=font_body, fill=TEXT_MUTED)
    
    steps = [
        ("STAGE 1: STATIC ANALYSIS (SAST)", CRIMSON, [
            "Decompile APK & IPA to audit hardcoded secrets & obfuscation",
            "Audit third-party dependencies for known CVEs",
            "Review manifest permissions and exported app components"
        ]),
        ("STAGE 2: DYNAMIC RUNTIME PENTESTING (DAST)", CYAN, [
            "Bypass biometric checks using Frida runtime hooking",
            "Test local database encryption against physical extraction",
            "Verify jailbreak & root detection resilience"
        ]),
        ("STAGE 3: NETWORK & API HARDENING", EMERALD, [
            "Proxy interception via Burp Suite & verify TLS certificate pinning",
            "Object-level authorization (IDOR) testing across all endpoints",
            "Rate limiting and brute-force defenses on auth routes"
        ])
    ]
    
    for idx, (title, color, items) in enumerate(steps):
        top_y = 270 + idx * 300
        draw_glass_card(img, 60, top_y, 960, 270, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw_pill_badge(draw, 90, top_y + 25, title, font_mono, accent_color=color)
        for i, item in enumerate(items):
            draw_safe_text(draw, 90, top_y + 85 + i * 50, f"[+] {item}", font_body, WHITE, max_width=880)
            
    add_footer(draw, w, h, cta_text="Swipe to Get Scoping Checklist ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_06_VAPT_Audit_Pipeline.jpg'), quality=95)
    print("Re-generated Day 1 Slide 6")

# Slide 7: Outro & CTA
def create_slide_7():
    w, h = 1080, 1350
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(540, 600, 500))
    add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="07 / 07", accent=EMERALD)
    
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 260), Image.Resampling.LANCZOS)
        lw, lh = logo.size
        img.alpha_composite(logo, (w // 2 - lw // 2, 200))
        
    font_headline = get_font(FONT_AVENIR, 48, index=2)
    font_sub = get_font(FONT_HELVETICA, 26)
    font_mono = get_font(FONT_MENLO, 20)
    
    draw.text((w // 2, 490), "SECURE. BUILD. SCALE.", font=font_headline, fill=WHITE, anchor='mm')
    draw.text((w // 2, 550), "Don't wait for a data breach to audit your application.", font=font_sub, fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img, 100, 640, 880, 420, radius=24, bg=(18, 24, 36, 250), border=(0, 255, 136, 180))
    draw.text((w // 2, 700), "READY TO HARDEN YOUR MOBILE APP?", font=get_font(FONT_AVENIR, 32, index=2), fill=EMERALD, anchor='mm')
    
    pitch = (
        "Our offensive security engineers will perform a targeted VAPT audit\n"
        "on your staging build and deliver an executive CVE remediation report\n"
        "within 5 business days."
    )
    for i, l in enumerate(pitch.split('\n')):
        draw.text((w // 2, 760 + i * 36), l, font=font_sub, fill=WHITE, anchor='mm')
        
    btn_w, btn_h = 760, 80
    bx = (w - btn_w) // 2
    by = 920
    draw.rounded_rectangle([bx, by, bx + btn_w, by + btn_h], radius=16, fill=EMERALD)
    draw.text((w // 2, by + btn_h // 2), "DM 'SECURITY' FOR VAPT SCOPING CHECKLIST", font=get_font(FONT_AVENIR, 24, index=2), fill=(8, 10, 15, 255), anchor='mm')
    
    draw.text((w // 2, 1140), "CYPHER MATRIX TECHNOLOGIES  |  cyphermatrix.io", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    draw.text((w // 2, 1180), "Gandhinagar / Ahmedabad • International Client Services", font=font_mono, fill=CYAN, anchor='mm')
    
    add_footer(draw, w, h, cta_text="Share with your CTO ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY1_DIR, 'Slide_07_CTA_Outro.jpg'), quality=95)
    print("Re-generated Day 1 Slide 7")

create_slide_1()
create_slide_2()
create_slide_3()
create_slide_4()
create_slide_5()
create_slide_6()
create_slide_7()
