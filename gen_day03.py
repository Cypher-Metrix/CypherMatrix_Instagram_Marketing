import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, BILL_MITRA_LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_footer
)

DAY3_DIR = os.path.join(WEEK1_DIR, 'Day_03_BillMitra_CounterCheckout')
os.makedirs(DAY3_DIR, exist_ok=True)

def add_day3_header(img, draw, slide_str="01 / 05"):
    w, h = 1080, 1080
    if os.path.exists(BILL_MITRA_LOGO_PATH):
        bm_logo = Image.open(BILL_MITRA_LOGO_PATH).convert('RGBA')
        bm_logo.thumbnail((180, 60), Image.Resampling.LANCZOS)
        img.alpha_composite(bm_logo, (50, 40))
        
    draw_pill_badge(draw, 240, 45, "SMART GST BILLING & POS", get_font(FONT_MENLO, 18), accent_color=EMERALD)
    
    font_slide = get_font(FONT_MENLO, 20)
    bbox = draw.textbbox((0, 0), slide_str, font=font_slide)
    draw.text((w - 50 - (bbox[2] - bbox[0]), 50), slide_str, font=font_slide, fill=TEXT_MUTED)
    draw.line([(50, 105), (w - 50, 105)], fill=SLATE_LINE, width=1)

# Slide 1: Cover
def create_slide_1():
    w, h = 1080, 1080
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(800, 500, 450))
    add_day3_header(img, draw, "01 / 05")
    
    font_hero = get_font(FONT_AVENIR, 42, index=2)
    font_sub = get_font(FONT_HELVETICA, 24)
    font_body = get_font(FONT_HELVETICA, 21)
    font_mono = get_font(FONT_MENLO, 19)
    
    draw_pill_badge(draw, 50, 135, "RETAIL CHECKOUT BLUEPRINT", font_mono, accent_color=CYAN)
    
    draw_safe_text(draw, 50, 200, "A 5-minute counter queue\nwill lose you customers.", font_hero, WHITE, max_width=540, line_spacing=8)
    draw_safe_text(draw, 50, 320, "How Bill Mitra creates & prints GST invoices\nin under 4 seconds flat. ⚡", font_sub, EMERALD, max_width=540, line_spacing=6)
    
    features = [
        "1-Tap Barcode Product Lookup",
        "Auto GST & Tax Surcharge Calculation",
        "Instant Bluetooth Thermal Receipt Print",
        "Real-Time Inventory & Cloud Backup"
    ]
    for idx, f in enumerate(features):
        fy = 430 + idx * 64
        draw.rounded_rectangle([50, fy, 560, fy + 52], radius=10, fill=(16, 22, 32, 240), outline=CARD_BORDER)
        draw.text((70, fy + 14), f"[✓] {f}", font=font_body, fill=WHITE)
        
    draw.text((50, 715), "No expensive computers or bulky hardware needed.", font=font_body, fill=TEXT_MUTED)
    draw.text((50, 750), "Turn any Android smartphone into an enterprise POS.", font=font_mono, fill=CYAN)
    
    dash_path = os.path.join(REF_DIR, 'bill-mitra-dashboard.png')
    if os.path.exists(dash_path):
        dash_img = Image.open(dash_path).convert('RGBA')
        dash_img = dash_img.resize((370, 780), Image.Resampling.LANCZOS)
        draw_glass_card(img, 620, 140, 410, 820, radius=30, bg=(12, 16, 24, 255), border=(0, 255, 136, 120))
        img.alpha_composite(dash_img, (640, 160))
        
    add_footer(draw, w, h, cta_text="Swipe to inspect demo ->", handle="Cypher Matrix Product", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY3_DIR, 'Slide_01_Cover.jpg'), quality=95)
    print("Re-generated Day 3 Slide 1 (Bounds Guaranteed)")

# Slide 2: The Rush Hour Bottleneck
def create_slide_2():
    w, h = 1080, 1080
    img, draw = create_base_canvas(w, h)
    add_day3_header(img, draw, "02 / 05")
    
    font_title = get_font(FONT_AVENIR, 36, index=2)
    font_card_title = get_font(FONT_AVENIR, 24, index=2)
    font_body = get_font(FONT_HELVETICA, 19)
    font_mono = get_font(FONT_MENLO, 17)
    
    draw.text((50, 135), "THE RUSH-HOUR BOTTLENECK IN RETAIL SHOPS", font=font_title, fill=WHITE)
    draw.text((50, 190), "Dukaan par grahakon ki bheed ke waqt purana tareeqa fail kyun hota hai:", font=font_body, fill=TEXT_MUTED)
    
    # Card 1: Traditional Way
    draw_glass_card(img, 50, 245, 470, 560, radius=20, bg=(24, 16, 22, 240), border=(255, 51, 102, 120))
    draw_pill_badge(draw, 75, 270, "PURANA TAREEQA (DESKTOP / PAPER)", font_mono, accent_color=CRIMSON)
    old_pts = [
        "❌ Computer boot hone mein 10 min lagte hain",
        "❌ Bijli cut hote hi billing ruk jaati hai",
        "❌ Har item ka naam manual type karna padta hai",
        "❌ GST calculation calculate karne mein galti",
        "❌ Grahak lambi line dekh kar doosri dukaan chala jata hai",
        "❌ Maheene ke end mein udhari ka hisab gayab"
    ]
    curr_y = 330
    for pt in old_pts:
        curr_y = draw_safe_text(draw, 75, curr_y, pt, font_body, WHITE, max_width=420, line_spacing=4) + 12
    draw.text((75, 765), "Average Billing Time: 3 to 5 Minutes", font=font_mono, fill=CRIMSON)
    
    # Card 2: Bill Mitra Way
    draw_glass_card(img, 560, 245, 470, 560, radius=20, bg=(14, 24, 22, 240), border=(0, 255, 136, 140))
    draw_pill_badge(draw, 585, 270, "BILL MITRA SMART POS", font_mono, accent_color=EMERALD)
    new_pts = [
        "✅ Mobile app se instant 4-second mein billing",
        "✅ Battery backup—bijli cut hone par bhi chalega",
        "✅ Phone camera se direct barcode scanner",
        "✅ Exact CGST + SGST automatic calculate",
        "✅ Bluetooth thermal printer se turant receipt",
        "✅ Cloud backup se ek-ek rupaye ka hisab safe"
    ]
    curr_y2 = 330
    for pt in new_pts:
        curr_y2 = draw_safe_text(draw, 585, curr_y2, pt, font_body, WHITE, max_width=420, line_spacing=4) + 12
    draw.text((585, 765), "Average Billing Time: 4 Seconds", font=font_mono, fill=EMERALD)
    
    # Bottom callout
    draw_glass_card(img, 50, 830, 980, 130, radius=16, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((80, 860), "FAST BILLING = MORE HAPPY CUSTOMERS = HIGHER DAILY REVENUE", font=get_font(FONT_AVENIR, 22, index=2), fill=CYAN)
    draw.text((80, 900), "Swipe to see the 4-second invoicing flow in action.", font=font_body, fill=TEXT_MUTED)
    
    add_footer(draw, w, h, cta_text="Swipe to Invoicing Flow ->", handle="Cypher Matrix Product", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY3_DIR, 'Slide_02_RushHour_Problem.jpg'), quality=95)
    print("Re-generated Day 3 Slide 2 (Bounds Guaranteed)")

# Slide 3: 4-Second Invoicing Flow
def create_slide_3():
    w, h = 1080, 1080
    img, draw = create_base_canvas(w, h)
    add_day3_header(img, draw, "03 / 05")
    
    font_title = get_font(FONT_AVENIR, 36, index=2)
    font_body = get_font(FONT_HELVETICA, 20)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((50, 135), "STEP-BY-STEP: 4-SECOND INVOICE CREATION", font=font_title, fill=WHITE)
    draw.text((50, 190), "Designed for zero technical training—anyone can bill effortlessly.", font=font_body, fill=TEXT_MUTED)
    
    steps = [
        ("1. SCAN OR SELECT ITEM", "Scan barcode with phone camera or 1-tap quick item search."),
        ("2. AUTO GST & DISCOUNT", "HSN code, tax slab, and wholesale discount applied automatically."),
        ("3. CHOOSE PAYMENT MODE", "Cash, UPI QR, or Udhar / Credit Ledger recorded in one tap."),
        ("4. PRINT & SHARE RECEIPT", "Prints 2-inch / 3-inch thermal bill and sends PDF on WhatsApp.")
    ]
    for idx, (head, desc) in enumerate(steps):
        sy = 250 + idx * 140
        draw_glass_card(img, 50, sy, 550, 120, radius=14, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw.text((75, sy + 18), head, font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
        draw_safe_text(draw, 75, sy + 54, desc, font_body, TEXT_MUTED, max_width=500, line_spacing=4)
        
    inv_path = os.path.join(REF_DIR, 'bill-mitra-create-invoice.png')
    if os.path.exists(inv_path):
        inv_img = Image.open(inv_path).convert('RGBA')
        inv_img = inv_img.resize((370, 780), Image.Resampling.LANCZOS)
        draw_glass_card(img, 640, 140, 390, 810, radius=24, bg=(12, 16, 24, 255), border=(0, 255, 136, 120))
        img.alpha_composite(inv_img, (650, 155))
        
    draw.text((50, 835), "[ 100% Offline Capability: Bills sync to cloud automatically ]", font=font_mono, fill=CYAN)
    
    add_footer(draw, w, h, cta_text="Swipe to Thermal Printing ->", handle="Cypher Matrix Product", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY3_DIR, 'Slide_03_Invoicing_Flow.jpg'), quality=95)
    print("Re-generated Day 3 Slide 3 (Bounds Guaranteed)")

# Slide 4: Bluetooth Thermal Printer
def create_slide_4():
    w, h = 1080, 1080
    img, draw = create_base_canvas(w, h)
    add_day3_header(img, draw, "04 / 05")
    
    font_title = get_font(FONT_AVENIR, 36, index=2)
    font_body = get_font(FONT_HELVETICA, 20)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw.text((50, 135), "BLUETOOTH THERMAL PRINTER INTEGRATION", font=font_title, fill=WHITE)
    draw.text((50, 190), "Wireless, portable, and zero expensive ink cartridge replacements.", font=font_body, fill=TEXT_MUTED)
    
    showcase_path = os.path.join(REF_DIR, 'bill-mitra-showcase.jpg')
    if os.path.exists(showcase_path):
        sc_img = Image.open(showcase_path).convert('RGBA')
        sc_img = sc_img.resize((500, 340), Image.Resampling.LANCZOS)
        draw_glass_card(img, 50, 245, 520, 360, radius=18, bg=(12, 16, 24, 255), border=CARD_BORDER)
        img.alpha_composite(sc_img, (60, 255))
        
    draw_glass_card(img, 600, 245, 430, 360, radius=18, bg=(18, 24, 34, 240), border=(0, 255, 136, 120))
    draw.text((625, 275), "HARDWARE COMPATIBILITY:", font=get_font(FONT_AVENIR, 22, index=2), fill=EMERALD)
    compat = [
        "- Any 58mm / 80mm Bluetooth printer",
        "- ESC/POS standard support",
        "- Pocket portable battery printers",
        "- USB & Wi-Fi receipt printers",
        "- Print Shop Name, GSTIN & Terms"
    ]
    for i, c in enumerate(compat):
        draw.text((625, 325 + i * 44), c, font=font_body, fill=WHITE)
        
    benefits = [
        ("ZERO INK COST", "Thermal paper uses heat—no ink cartridges to replace ever."),
        ("WHATSAPP PDF", "Optionally send digital bill on customer WhatsApp to save paper."),
        ("REAL-TIME STOCK", "Every invoice automatically reduces current store inventory.")
    ]
    for i, (b_title, b_desc) in enumerate(benefits):
        bx = 50 + i * 335
        draw_glass_card(img, bx, 640, 315, 280, radius=16, bg=(16, 22, 32, 240), border=CARD_BORDER)
        draw_pill_badge(draw, bx + 20, 665, b_title, font_mono, accent_color=CYAN)
        draw_safe_text(draw, bx + 20, 725, b_desc, font_body, TEXT_MUTED, max_width=275, line_spacing=6)
        
    add_footer(draw, w, h, cta_text="Swipe to Download ->", handle="Cypher Matrix Product", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY3_DIR, 'Slide_04_Thermal_Printing.jpg'), quality=95)
    print("Re-generated Day 3 Slide 4 (Bounds Guaranteed)")

# Slide 5: Outro & Download CTA
def create_slide_5():
    w, h = 1080, 1080
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 45), glow_pos=(540, 500, 480))
    add_day3_header(img, draw, "05 / 05")
    
    if os.path.exists(BILL_MITRA_LOGO_PATH):
        bm_logo = Image.open(BILL_MITRA_LOGO_PATH).convert('RGBA')
        bm_logo.thumbnail((240, 240), Image.Resampling.LANCZOS)
        img.alpha_composite(bm_logo, (w // 2 - bm_logo.size[0] // 2, 160))
        
    font_hero = get_font(FONT_AVENIR, 40, index=2)
    font_sub = get_font(FONT_HELVETICA, 24)
    font_mono = get_font(FONT_MENLO, 19)
    
    draw.text((w // 2, 440), "UPGRADE YOUR SHOP TO BILL MITRA TODAY", font=font_hero, fill=WHITE, anchor='mm')
    draw.text((w // 2, 495), "India's smartest mobile billing, inventory, and GST app.", font=font_sub, fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img, 100, 550, 880, 350, radius=20, bg=(16, 22, 34, 250), border=(0, 255, 136, 160))
    draw.text((w // 2, 595), "AVAILABLE ON GOOGLE PLAY STORE", font=get_font(FONT_AVENIR, 24, index=2), fill=CYAN, anchor='mm')
    
    pitch = [
        "✓ Free download with instant 2-minute store setup",
        "✓ Works for Kirana, Wholesale, Electronics, Garments & Hardware",
        "✓ Multi-device sync & full business financial reports"
    ]
    for i, p in enumerate(pitch):
        draw.text((w // 2, 650 + i * 40), p, font=font_sub, fill=WHITE, anchor='mm')
        
    btn_w, btn_h = 720, 75
    bx = (w - btn_w) // 2
    by = 785
    draw.rounded_rectangle([bx, by, bx + btn_w, by + btn_h], radius=16, fill=EMERALD)
    draw.text((w // 2, by + btn_h // 2), "DM 'MITRA' FOR FREE ONBOARDING DEMO", font=get_font(FONT_AVENIR, 23, index=2), fill=(8, 10, 15, 255), anchor='mm')
    
    draw.text((w // 2, 940), "Engineered by Cypher Matrix Technologies Private Limited", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    
    add_footer(draw, w, h, cta_text="Share with a Dukandaar ->", handle="Cypher Matrix Product", accent=EMERALD)
    img.convert('RGB').save(os.path.join(DAY3_DIR, 'Slide_05_Download_CTA.jpg'), quality=95)
    print("Re-generated Day 3 Slide 5 (Bounds Guaranteed)")

create_slide_1()
create_slide_2()
create_slide_3()
create_slide_4()
create_slide_5()
