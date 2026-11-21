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

# ==============================================================================
# DAY 08: OFFLINE-FIRST ARCHITECTURE (5 SLIDES, 1080x1350)
# ==============================================================================
d8_dir = os.path.join(WEEK2_DIR, 'Day_08_Offline_First_Architecture')
os.makedirs(d8_dir, exist_ok=True)

def build_day08():
    w, h = 1080, 1350
    # Slide 1: Cover
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="SOFTWARE ARCHITECTURE", slide_str="01 / 05", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "MOBILE RESILIENCE BLUEPRINT", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    font_card_head = get_font(FONT_AVENIR, 22, index=2)
    
    title_text = "Why building an 'online-only' mobile app\nwill fail your users in real-world environments."
    draw_safe_text(draw, 60, 215, title_text, font_hero, WHITE, max_width=960, line_spacing=10)
    
    # Terminal Card
    card_x, card_y, card_w, card_h = 60, 410, 960, 570
    draw_glass_card(img, card_x, card_y, card_w, card_h, radius=20, bg=(14, 18, 26, 245), border=(0, 255, 136, 120))
    
    t_bar_h = 55
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + t_bar_h], radius=20, fill=(20, 26, 38, 255))
    draw.rectangle([card_x, card_y + 20, card_x + card_w, card_y + t_bar_h], fill=(20, 26, 38, 255))
    draw.line([(card_x, card_y + t_bar_h), (card_x + card_w, card_y + t_bar_h)], fill=CARD_BORDER, width=1)
    draw.ellipse([card_x + 25, card_y + 20, card_x + 39, card_y + 34], fill=(255, 95, 87, 255))
    draw.ellipse([card_x + 49, card_y + 20, card_x + 63, card_y + 34], fill=(254, 187, 43, 255))
    draw.ellipse([card_x + 73, card_y + 20, card_x + 87, card_y + 34], fill=(39, 201, 63, 255))
    draw.text((card_x + 110, card_y + 18), "ARCHITECTURE SIMULATOR: NETWORK_DROP_TEST", font=font_mono, fill=TEXT_MUTED)
    draw.text((card_x + card_w - 230, card_y + 18), "RESILIENCE: 100%", font=get_font(FONT_MENLO, 19), fill=EMERALD)
    
    # Left: Fragile Web Wrapper
    p1_x, panel_y, panel_w, panel_h = card_x + 25, card_y + t_bar_h + 20, 435, 330
    draw.rounded_rectangle([p1_x, panel_y, p1_x + panel_w, panel_y + panel_h], radius=14, fill=(22, 12, 18, 255), outline=(255, 51, 102, 120))
    draw.text((p1_x + 20, panel_y + 20), "FRAGILE APP (ONLINE ONLY)", font=font_card_head, fill=CRIMSON)
    draw.text((p1_x + 20, panel_y + 55), "When 5G/4G drops to 0 bars:", font=font_mono, fill=TEXT_MUTED)
    fragile = [
        "[✗] Infinite spinning loader screens",
        "[✗] Socket timeout exceptions thrown",
        "[✗] Unsaved cart / delivery data lost",
        "[✗] User forced to restart the app"
    ]
    for i, f in enumerate(fragile):
        draw.text((p1_x + 20, panel_y + 95 + i * 40), f, font=font_mono, fill=(255, 120, 140, 255))
    draw.line([(p1_x + 20, panel_y + 275), (p1_x + panel_w - 20, panel_y + 275)], fill=CARD_BORDER, width=1)
    draw.text((p1_x + 20, panel_y + 290), "Result: Churn & App Store 1-Star", font=font_mono, fill=CRIMSON)
    
    # Right: Offline-First Engine
    p2_x = card_x + 495
    draw.rounded_rectangle([p2_x, panel_y, p2_x + panel_w, panel_y + panel_h], radius=14, fill=(10, 20, 24, 255), outline=(0, 255, 136, 140))
    draw.text((p2_x + 20, panel_y + 20), "OFFLINE-FIRST ENGINE", font=font_card_head, fill=EMERALD)
    draw.text((p2_x + 20, panel_y + 55), "With local replica & auto-sync:", font=font_mono, fill=TEXT_MUTED)
    resilient = [
        "[✓] 0ms UI latency (Optimistic UI)",
        "[✓] Local SQLite encrypted write",
        "[✓] Background auto-sync daemon",
        "[✓] Zero lost customer transactions"
    ]
    for i, r in enumerate(resilient):
        draw.text((p2_x + 20, panel_y + 95 + i * 40), r, font=font_mono, fill=(160, 255, 200, 255))
    draw.line([(p2_x + 20, panel_y + 275), (p2_x + panel_w - 20, panel_y + 275)], fill=CARD_BORDER, width=1)
    draw.text((p2_x + 20, panel_y + 290), "Result: 100% Field Reliability", font=font_mono, fill=EMERALD)
    
    # Bottom insight
    summary_y = panel_y + panel_h + 20
    draw.rounded_rectangle([card_x + 25, summary_y, card_x + card_w - 25, summary_y + 95], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((card_x + 45, summary_y + 18), "ENGINEERING PRINCIPLE:", font=font_mono, fill=CYAN)
    draw_safe_text(draw, card_x + 45, summary_y + 48, "Your local database should be the single source of truth for the UI. The network is merely an asynchronous sync mechanism.", font_body, WHITE, max_width=860, line_spacing=4)
    
    # Bottom Callout Box
    draw_glass_card(img, 60, 1010, 960, 170, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
    callout = "Swipe through for the 5-slide blueprint: SQLite event sourcing, background sync queues, and CRDT conflict resolution."
    draw_safe_text(draw, 95, 1035, callout, get_font(FONT_HELVETICA, 23), WHITE, max_width=890, line_spacing=6)
    draw.text((95, 1120), "[ Battle-Tested in Logistics & Retail Deployments ]", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w, h, cta_text="Swipe to Architecture ->", accent=EMERALD)
    img.convert('RGB').save(os.path.join(d8_dir, 'Slide_01_Cover.jpg'), quality=95)
    
    # Slides 2 to 5 for Day 08
    slides_d8 = [
        ("Slide_02_Local_Replica.jpg", "02 / 05", "LOCAL STORAGE: SQLITE & DRIFT", [
            ("1. ZERO LATENCY LOCAL WRITES", "When the driver or customer taps 'Submit Order', the app writes directly to the on-device SQLite database via Drift. Zero network delay."),
            ("2. OPTIMISTIC UI UPDATES", "The UI updates instantly to confirm the action. The user never waits for server round-trips."),
            ("3. ENCRYPTION AT REST", "All sensitive local records are encrypted using SQLCipher with hardware KeyStore/KeyChain keys.")
        ]),
        ("Slide_03_Sync_Queue.jpg", "03 / 05", "BACKGROUND QUEUE: EVENT SOURCING", [
            ("1. APPEND-ONLY MUTATION LOG", "Every update is recorded as an immutable event with cryptographic nonce and local timestamp."),
            ("2. WORKMANAGER DAEMON", "A battery-efficient background worker monitors network state. When 4G re-connects, it pushes queued events."),
            ("3. EXPONENTIAL BACKOFF RETRY", "If the server returns 503 or dropped connection, the queue retries gracefully without data loss.")
        ]),
        ("Slide_04_CRDT_Resolution.jpg", "04 / 05", "CONFLICT-FREE REPLICATION (CRDTs)", [
            ("1. THE MULTI-DEVICE CHALLENGE", "When 2 drivers update the same inventory batch offline, naive 'last write wins' overwrites data."),
            ("2. STATE-BASED CRDT RESOLUTION", "Using deterministic CRDT merge rules, both offline updates are merged seamlessly on the server."),
            ("3. 100% AUDIT RECONCILIATION", "Guarantees that no stock counts or customer ledger balances are corrupted.")
        ]),
        ("Slide_05_CTA_Outro.jpg", "05 / 05", "BUILD ROBUST MOBILE SYSTEMS", [
            ("NEED ARCHITECTURE THAT DOESN'T CRASH?", "Whether building for warehouse retail, remote logistics, or global SaaS—Cypher Matrix engineers resilient offline-first systems."),
            ("TALK TO OUR LEAD ARCHITECTS", "DM 'PROJECT' to schedule a scoping session for your mobile architecture."),
            ("VISIT cyphermatrix.io", "Gandhinagar / Ahmedabad • International Engineering Services")
        ])
    ]
    
    for s_name, s_num, s_title, s_cards in slides_d8:
        s_img, s_draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 30), glow_pos=(540, 600, 450))
        add_header(s_img, s_draw, category="SOFTWARE ARCHITECTURE", slide_str=s_num, accent=CYAN)
        s_draw.text((60, 150), s_title, font=get_font(FONT_AVENIR, 42, index=2), fill=WHITE)
        s_draw.text((60, 215), "Production engineering standards applied at Cypher Matrix:", font=font_body, fill=TEXT_MUTED)
        
        for c_i, (c_h, c_desc) in enumerate(s_cards):
            cy = 280 + c_i * 280
            draw_glass_card(s_img, 60, cy, 960, 255, radius=18, bg=(18, 24, 34, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 95, cy + 22, c_h, font_mono, accent_color=EMERALD if c_i==0 else CYAN)
            draw_safe_text(s_draw, 95, cy + 80, c_desc, font_body, WHITE, max_width=860, line_spacing=6)
            
        add_footer(s_draw, w, h, cta_text="Swipe to next ->" if s_num != "05 / 05" else "DM 'PROJECT' ->", accent=EMERALD)
        s_img.convert('RGB').save(os.path.join(d8_dir, s_name), quality=95)
        
    print("Day 08 generated successfully.")

build_day08()
