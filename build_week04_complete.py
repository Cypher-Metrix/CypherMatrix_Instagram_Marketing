import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    ASSETS_DIR, LOGO_PATH, BILL_MITRA_LOGO_PATH, REF_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text, add_header, add_footer
)

BASE_DIR_USER = '/Users/cyphermatrix/scratch/CypherMatrix_Instagram_Marketing'
BASE_DIR_GEMINI = '/Users/cyphermatrix/.gemini/antigravity/scratch/CypherMatrix_Instagram_Marketing'

WEEK4_DIR_USER = os.path.join(BASE_DIR_USER, '04_Post_Creatives', 'Week_04')
WEEK4_DIR_GEMINI = os.path.join(BASE_DIR_GEMINI, '04_Post_Creatives', 'Week_04')
os.makedirs(WEEK4_DIR_USER, exist_ok=True)
os.makedirs(WEEK4_DIR_GEMINI, exist_ok=True)

w_port, h_port = 1080, 1350
w_sq, h_sq = 1080, 1080
w_reel, h_reel = 1080, 1920

def save_image_both(img, rel_folder, filename):
    for base in [WEEK4_DIR_USER, WEEK4_DIR_GEMINI]:
        folder = os.path.join(base, rel_folder)
        os.makedirs(folder, exist_ok=True)
        out_path = os.path.join(folder, filename)
        img.convert('RGB').save(out_path, quality=95)

# ==============================================================================
# DAY 22: STATE MANAGEMENT: RIVERPOD VS BLOC IN 2026 (5 Slides, 1080x1350)
# ==============================================================================
def build_day22():
    folder = 'Day_22_Flutter_StateManagement_Riverpod_Bloc'
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="FLUTTER ARCHITECTURE", slide_str="01 / 05", accent=CYAN)
    draw_pill_badge(draw, 60, 145, "STATE MANAGEMENT BENCHMARKS", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    draw_safe_text(draw, 60, 210, "FLUTTER STATE MANAGEMENT:\nRIVERPOD VS BLOC IN 2026", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "An honest, battle-tested architectural comparison from a team shipping production apps to millions of enterprise and retail users.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Comparison Terminal Card
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "PRODUCTION COMPARISON: RIVERPOD 3.0 VS BLOC 9.0", font=font_mono, fill=TEXT_MUTED)
    
    # Left Box: Riverpod
    draw.rounded_rectangle([90, 510, 520, 880], radius=14, fill=(12, 20, 28, 255), outline=(0, 240, 255, 120))
    draw.text((115, 535), "RIVERPOD (REMI ROUSSELET)", font=get_font(FONT_AVENIR, 19, index=2), fill=CYAN)
    points_rp = [
        "✓ Compile-time safety (no context required)",
        "✓ Elegant async data caching (`AsyncValue`)",
        "✓ Less boilerplate with code generation",
        "✓ Automatic state disposal & scoping",
        "⚠️ Steeper initial mental model for juniors",
        "BEST FOR: Rapid MVP, reactive apps, realtime"
    ]
    for idx, p in enumerate(points_rp):
        col = CYAN if '✓' in p else (255, 180, 120, 255) if '⚠️' in p else EMERALD
        draw_safe_text(draw, 115, 580 + idx * 48, p, font=get_font(FONT_HELVETICA, 17), fill=col, max_width=380, line_spacing=2)
        
    # Right Box: Bloc
    draw.rounded_rectangle([550, 510, 980, 880], radius=14, fill=(16, 20, 24, 255), outline=(0, 255, 136, 120))
    draw.text((575, 535), "BLOC (FELIX ANGELOV)", font=get_font(FONT_AVENIR, 19, index=2), fill=EMERALD)
    points_bl = [
        "✓ Strict event-driven state transitions",
        "✓ Highly predictable enterprise auditing",
        "✓ Exceptional testability & replayability",
        "✓ Easiest for large multi-team codebases",
        "⚠️ More boilerplate (Events, States, Blocs)",
        "BEST FOR: Enterprise banking, strict compliance"
    ]
    for idx, p in enumerate(points_bl):
        col = EMERALD if '✓' in p else (255, 180, 120, 255) if '⚠️' in p else CYAN
        draw_safe_text(draw, 575, 580 + idx * 48, p, font=get_font(FONT_HELVETICA, 17), fill=col, max_width=380, line_spacing=2)
        
    # Bottom key takeaway
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "There is no 'one best' framework. Your state architecture must reflect your team size, testing requirements, and event predictability needs.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect decision matrix ->", handle="@cyphermatrixpvtltd", accent=CYAN)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d22 = [
        ("02 / 05", "DECISION FACTOR 1: TEAM SCALE", "How Team Size Dictates State Architecture", [
            ("Small Teams & Fast Shipping (Choose Riverpod)", "Riverpod allows a single full-stack engineer to build complex asynchronous caching and UI reactivity with minimal ceremony. It drastically speeds up initial development velocity."),
            ("Large Distributed Engineering Orgs (Choose Bloc)", "Bloc enforces a strict, opinionated contract. Every state change requires an explicit Event and State class, making code reviews trivial and preventing junior devs from bypassing architecture."),
            ("Maintenance Over 3+ Years", "Bloc code written 4 years ago still looks identical to modern Bloc code. Riverpod's rapid evolution between v1, v2, and v3 has required code migration effort.")
        ], "DECISION CRITERIA: ENGINEERING RIGIDITY VS VELOCITY"),
        
        ("03 / 05", "DECISION FACTOR 2: ASYNC DATA HANDLING", "Handling Loading, Error, and Refresh States", [
            ("Riverpod's Killer Feature: AsyncValue", "Pattern matching with `.when(data: ..., loading: ..., error: ...)` makes handling network latency, pull-to-refresh, and automatic cached retries effortless."),
            ("Bloc's Granular Event Streams", "Bloc excels when user actions trigger complex side-effects (e.g., logging an analytics event, persisting to offline SQLite, and dispatching a push notification simultaneously)."),
            ("Optimistic State Mutations", "Both libraries handle optimistic updates well, but Riverpod's family providers allow cleaner granular widget rebuilding without repainting entire list trees.")
        ], "PERFORMANCE: 60 FPS IMPELERR RENDERING ON BOTH STACKS"),
        
        ("04 / 05", "CYPHER MATRIX STACK RECOMMENDATIONS", "What We Actually Use in Production", [
            ("Fintech & Banking Systems -> BLOC", "For apps like Bill Mitra where every financial transaction must be deterministically audited, logged, and replayed, Bloc's strict state machines are unmatched."),
            ("Realtime AI, Social & Logistics -> RIVERPOD", "For apps like GLAD AI or Green Line distribution with complex WebSocket streaming and multi-source reactivity, Riverpod provides cleaner decoupled dependencies."),
            ("Avoid Context-Dependent State", "Regardless of stack, we never rely on raw `Provider` or bloated singleton controllers that pollute the Flutter BuildContext.")
        ], "PRODUCTION STANDARD: ZERO STATE LEAKAGE | COMPREHENSIVE TESTS"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Engineering Scalable Flutter Architecture", [
            ("Clean Architecture Blueprint", "We engineer multi-tier Flutter codebases separated into Data, Domain, and Presentation layers for Fortune 500s and ambitious startups."),
            ("Offensive Security & Performance Profiling", "Zero jank, sub-100ms startup times, memory leak profiling, and hardened binary security built in."),
            ("Discuss Your Flutter Architecture", "Building a mission-critical mobile product? DM 'FLUTTER' to review your tech stack with our leads.")
        ], "CYPHER MATRIX TECHNOLOGIES | FLUTTER CENTER OF EXCELLENCE")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d22, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=CYAN)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=CYAN if s_idx < 5 else EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=CYAN if s_idx < 5 else EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'FLUTTER' to consult our team ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CYAN if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 22 generated.")

# ==============================================================================
# DAY 23: HOW BILL MITRA SIMPLIFIES INVENTORY & STOCK (5 Slides, 1080x1080 Square)
# ==============================================================================
def build_day23():
    folder = 'Day_23_BillMitra_Inventory_Stock'
    w, h = w_sq, h_sq
    font_hero = get_font(FONT_AVENIR, 42, index=2)
    font_body = get_font(FONT_HELVETICA, 21)
    font_mono = get_font(FONT_MENLO, 18)
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(800, 300, 400))
    if os.path.exists(BILL_MITRA_LOGO_PATH):
        bm_logo = Image.open(BILL_MITRA_LOGO_PATH).convert('RGBA')
        bm_logo.thumbnail((180, 60), Image.Resampling.LANCZOS)
        img.alpha_composite(bm_logo, (60, 45))
    draw_pill_badge(draw, 260, 48, "PRODUCT SPOTLIGHT", get_font(FONT_MENLO, 18), accent_color=EMERALD)
    draw.text((w - 140, 52), "01 / 05", font=get_font(FONT_MENLO, 20), fill=TEXT_MUTED)
    draw.line([(50, 105), (w - 50, 105)], fill=SLATE_LINE, width=1)
    
    draw_safe_text(draw, 60, 135, "STOP LOSING PROFIT:\nSMART INVENTORY IN BILL MITRA", font_hero, WHITE, max_width=960, line_spacing=8)
    draw_safe_text(draw, 60, 245, "How retail store owners and wholesalers automate stock counting, low-balance alerts, and batch expiry tracking from their phone.", font_body, TEXT_MUTED, max_width=960)
    
    # Feature Showcase Card
    draw_glass_card(img, 60, 320, 960, 610, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    
    # Left Box: The Manual Inventory Nightmare
    draw.rounded_rectangle([90, 350, 510, 830], radius=16, fill=(20, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 375), "MANUAL STOCK LOSSES", font=get_font(FONT_AVENIR, 20, index=2), fill=CRIMSON)
    points_bad = [
        "❌ Items run out during peak sales",
        "❌ Over-ordering slow-moving dead stock",
        "❌ Expired FMCG products dumped in trash",
        "❌ Staff theft & unaccounted shrinkage",
        "❌ Hours spent doing manual ledger tally",
        "❌ Loss of customer trust & repeat orders"
    ]
    for idx, p in enumerate(points_bad):
        draw_safe_text(draw, 115, 430 + idx * 62, p, font=get_font(FONT_HELVETICA, 18), fill=(255, 180, 190, 255), max_width=380, line_spacing=4)
    draw.text((115, 850), "Average Retail Loss: 4-7% Revenue", font=font_mono, fill=CRIMSON)
    
    # Right Box: Bill Mitra Automation
    draw.rounded_rectangle([550, 350, 970, 830], radius=16, fill=(10, 24, 18, 255), outline=(0, 255, 136, 140))
    draw.text((575, 375), "BILL MITRA AUTOMATION", font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
    points_bm = [
        "✅ Stock auto-deducts on every bill scan",
        "✅ Real-time Low-Stock WhatsApp alerts",
        "✅ Batch number & expiration tracking",
        "✅ Fast barcode cataloging with camera",
        "✅ Profit-margin analysis per item category",
        "✅ 1-Click Purchase Order to suppliers"
    ]
    for idx, p in enumerate(points_bm):
        draw_safe_text(draw, 575, 430 + idx * 62, p, font=get_font(FONT_HELVETICA, 18), fill=(180, 255, 210, 255), max_width=380, line_spacing=4)
    draw.text((575, 850), "Stock Accuracy: 99.8% Cloud Audited", font=font_mono, fill=EMERALD)
    
    draw.line([(50, h - 80), (w - 50, h - 80)], fill=SLATE_LINE, width=1)
    draw.text((50, h - 55), "BILL MITRA  |  Google Play Store", font=font_mono, fill=TEXT_MUTED)
    draw.text((w - 380, h - 55), "Swipe to inspect stock features ->", font=get_font(FONT_AVENIR, 18, index=2), fill=EMERALD)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d23 = [
        ("02 / 05", "AUTO-DEDUCTION ENGINE", "Real-Time Stock Depletion with Every Bill", [
            ("Zero Discrepancy Checkout", "The millisecond your cashier scans a barcode or taps an item on the Bill Mitra app, the local inventory database deducts quantity in real-time."),
            ("Multi-Counter Stock Synchronization", "Operating multiple billing counters in one supermarket? Stock numbers update across all staff devices simultaneously via local mesh & cloud sync.")
        ], "ENGINE: ATOMIC INVENTORY MUTATION TRANSACTIONS"),
        
        ("03 / 05", "SMART LOW-STOCK ALERTS", "Never Hear 'Sorry Sir, Out of Stock' Again", [
            ("Custom Reorder Thresholds", "Set minimum threshold levels for each item. When milk packets drop below 10 or rice sacks drop below 5, your phone notifies you immediately."),
            ("Automated Vendor Purchase Orders", "Generate professional WhatsApp PDF purchase orders to your wholesale suppliers with one tap, including item codes, quantities, and GST.")
        ], "NOTIFICATION: INSTANT SMARTPHONE PUSH & WHATSAPP TELEMETRY"),
        
        ("04 / 05", "BATCH & EXPIRY CONTROLS", "Eliminate Dead Stock and Expired Waste", [
            ("First-In, First-Out (FIFO) Enforcement", "Bill Mitra guides staff to sell older inventory batches first, preventing perishable goods from sitting forgotten in the back warehouse."),
            ("30-Day Expiry Warning Dashboard", "Get a proactive weekly report of items expiring within 30 days so you can run discount promotions or return them to vendors for credit.")
        ], "COMPLIANCE: FSSAI & DRUG CONTROLLER BATCH REGULATION READY"),
        
        ("05 / 05", "START IN 60 SECONDS", "Download Bill Mitra Free on Google Play", [
            ("Excel / CSV Bulk Item Import", "Have 2,000 items in an old spreadsheet? Upload your CSV file and start billing with full inventory in 2 minutes flat."),
            ("Built for Modern Indian Retail", "Supermarkets, pharmacies, apparel stores, and electrical shops—trusted by thousands of thriving business owners.")
        ], "FREE ON GOOGLE PLAY STORE | SEARCH 'BILL MITRA'")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d23, 2):
        s_img, s_draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 35), glow_pos=(800, 300, 400))
        if os.path.exists(BILL_MITRA_LOGO_PATH):
            bm_logo = Image.open(BILL_MITRA_LOGO_PATH).convert('RGBA')
            bm_logo.thumbnail((180, 60), Image.Resampling.LANCZOS)
            s_img.alpha_composite(bm_logo, (60, 45))
        draw_pill_badge(s_draw, 260, 48, s_badge, get_font(FONT_MENLO, 18), accent_color=EMERALD)
        s_draw.text((w - 140, 52), s_num, font=get_font(FONT_MENLO, 20), fill=TEXT_MUTED)
        s_draw.line([(50, 105), (w - 50, 105)], fill=SLATE_LINE, width=1)
        
        draw_safe_text(s_draw, 60, 140, s_title, font_hero, WHITE, max_width=960, line_spacing=8)
        
        y_pos = 250
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 290, radius=20, bg=(16, 22, 32, 245), border=CARD_BORDER)
            draw_pill_badge(s_draw, 95, y_pos + 25, c_title, get_font(FONT_MENLO, 20), accent_color=EMERALD)
            draw_safe_text(s_draw, 95, y_pos + 85, c_desc, font_body, WHITE, max_width=890, line_spacing=6)
            y_pos += 320
            
        draw.line([(50, h - 80), (w - 50, h - 80)], fill=SLATE_LINE, width=1)
        s_draw.text((50, h - 55), f"[ {footer_txt} ]", font=font_mono, fill=CYAN if s_idx < 5 else EMERALD)
        s_cta = "Swipe for features ->" if s_idx < 5 else "Download on Google Play ->"
        s_draw.text((w - 380, h - 55), s_cta, font=get_font(FONT_AVENIR, 18, index=2), fill=EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 23 generated.")

# ==============================================================================
# DAY 24: CASE STUDY: PATNAGAR GROUP ORGANIC MARKETPLACE (5 Slides, 1080x1350)
# ==============================================================================
def build_day24():
    folder = 'Day_24_CaseStudy_Patnagar_Organic'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="AGRITECH CASE STUDY", slide_str="01 / 05", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "FARM-TO-CONSUMER E-COMMERCE", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "CASE STUDY: PATNAGAR GROUP\nORGANIC AGRI MARKETPLACE", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "How Cypher Matrix designed and launched a direct-from-farm organic agricultural marketplace connecting rural producers to urban consumers.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Project Snapshot Terminal
    draw_glass_card(img, 60, 450, 960, 560, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.text((95, 480), "PROJECT SNAPSHOT & TECHNICAL HIGHLIGHTS:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    
    metrics = [
        ("CLIENT PARTNER", "Patnagar Group — Organic Agricultural Producers"),
        ("CHALLENGE", "Eliminating predatory middlemen; Building farmer-to-consumer trust"),
        ("DELIVERABLES", "High-conversion web portal, order routing engine, and logistics tracking"),
        ("INTEGRATIONS", "Razorpay payment gateway, automated SMS dispatch, and warehouse sync"),
        ("VERIFIED OUTCOME", "4.2x increase in direct farmer margins • 48-hour farm-to-table delivery")
    ]
    curr_y = 535
    for k, v in metrics:
        draw.text((95, curr_y), k, font=font_mono, fill=EMERALD)
        curr_y = draw_safe_text(draw, 95, curr_y + 28, v, font_body, WHITE, max_width=890) + 20
        
    # Bottom key takeaway
    draw_glass_card(img, 60, 1050, 960, 190, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((95, 1080), "THE AGRITECH E-COMMERCE TAKEAWAY:", font=get_font(FONT_AVENIR, 22, index=2), fill=CYAN)
    draw_safe_text(draw, 95, 1125, "Building for rural agriculture requires frictionless payment gateways, robust low-bandwidth web optimization, and transparent traceability.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect architecture ->", handle="@cyphermatrixpvtltd", accent=EMERALD)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d24 = [
        ("02 / 05", "THE CHALLENGE", "The Exploitative Agricultural Supply Chain", [
            ("70% Margin Lost to Middlemen", "Traditional mandi brokers and wholesalers took up to 70% of product value, leaving organic farmers underpaid while urban consumers paid inflated prices."),
            ("Zero Product Traceability", "Consumers had no proof whether 'organic' labels were authentic, creating massive skepticism in the premium food market."),
            ("Complex Perishable Logistics", "Fresh organic produce requires strict 24-to-48 hour fulfillment windows to avoid spoilage without chemical preservatives.")
        ], "PROBLEM: UNVERIFIED CLAIMS AND CRIPPLING WHOLESALER MONOPOLIES"),
        
        ("03 / 05", "CYPHER MATRIX ARCHITECTURE", "Direct-from-Farm Digital Infrastructure", [
            ("Traceable Farm Provenance Engine", "Engineered batch-level QR code tracking. Consumers scan the packaging to see the exact farmer, harvest date, and soil certification."),
            ("High-Performance E-Commerce Web Stack", "Lightweight, responsive web application achieving 98+ Google Lighthouse performance scores—ensuring instant checkout even on 3G connections."),
            ("Automated Delivery Scheduling", "Integrated automated dispatch notifications and cold-chain logistics routing to deliver farm-fresh goods within 48 hours.")
        ], "STACK: MODERN NEXT.JS + TAILWIND + HIGH-THROUGHPUT SQL BACKEND"),
        
        ("04 / 05", "BUSINESS IMPACT & RESULTS", "Empowering Farmers While Scaling Revenue", [
            ("4.2x Higher Revenue Retention", "Farmers earned over 4x higher per-kilogram payouts compared to traditional wholesale APMC mandis."),
            ("94% Customer Repeat Rate", "Transparent farm origin and pristine product freshness created intense brand loyalty among health-conscious urban households."),
            ("Zero Payment Reconcile Failures", "Automated instant payout splits routed earnings directly to rural bank accounts with zero manual accounting errors.")
        ], "IMPACT: SUSTAINABLE FAIR-TRADE AGRITECH AT REGIONAL SCALE"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Build Your Digital Marketplace with Cypher Matrix", [
            ("Custom E-Commerce & Marketplace Engines", "We engineer custom multi-vendor platforms, logistics routing systems, and payment splitting architectures."),
            ("Hardened Security & PCI-DSS Compliance", "Every transaction, tokenized card, and webhook is audited against financial fraud and tampering."),
            ("Consult with Our Product Engineering Team", "Ready to disrupt an industry with custom digital products? DM 'AGRITECH' to explore your project.")
        ], "CYPHER MATRIX TECHNOLOGIES | SECURE. BUILD. SCALE.")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d24, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=EMERALD)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'AGRITECH' to discuss your platform ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 24 generated.")

# ==============================================================================
# DAY 25: SQL INJECTION IN MODERN WEB APPS: YES, IT STILL EXISTS (5 Slides, 1080x1350)
# ==============================================================================
def build_day25():
    folder = 'Day_25_Modern_SQL_Injection'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(255, 51, 102, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="CYBERSECURITY EXPLOIT BREAKDOWN", slide_str="01 / 05", accent=CRIMSON)
    draw_pill_badge(draw, 60, 145, "THE VULNERABILITY THAT WON'T DIE", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "SQL INJECTION IN 2026:\nYES, IT STILL BREACHES PRODUCTION", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "Developers think modern ORMs completely eliminate SQL injection. Here is how advanced attackers bypass ORM filters, raw query escapes, and second-order injections.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Exploit Terminal Container
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "EXPLOIT SIMULATOR: ORM RAW CLAUSE INJECTION", font=font_mono, fill=TEXT_MUTED)
    
    # Code snippet comparison
    draw.rounded_rectangle([90, 510, 990, 670], radius=14, fill=(24, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 530), "VULNERABLE PRODUCTION PATTERN (RAW CLAUSE CONCATENATION):", font=font_mono, fill=CRIMSON)
    vulnerable_sql = [
        "// Developer bypassed ORM for 'performance optimization':",
        "const query = `SELECT * FROM users WHERE organization_id = ${orgId} ORDER BY ${req.body.sortField}`;",
        "// Attacker passes: sortField = 'created_at; DROP TABLE audit_logs;--'"
    ]
    for idx, c in enumerate(vulnerable_sql):
        draw.text((115, 570 + idx * 34), c, font=font_mono, fill=(255, 180, 190, 255))
        
    draw.rounded_rectangle([90, 690, 990, 850], radius=14, fill=(10, 24, 18, 255), outline=(0, 255, 136, 120))
    draw.text((115, 710), "CYPHER MATRIX DEFENSE (STRICT PARAMETERIZATION & ALLOWLIST):", font=font_mono, fill=EMERALD)
    hardened_sql = [
        "// Enforce strict column allowlist + parameterized AST builders:",
        "const ALLOWED_SORT = ['created_at', 'company_name', 'annual_revenue'];",
        "if (!ALLOWED_SORT.includes(req.body.sortField)) throw new SecurityException('Invalid Sort Field');"
    ]
    for idx, c in enumerate(hardened_sql):
        draw.text((115, 750 + idx * 34), c, font=font_mono, fill=(180, 255, 210, 255))
        
    draw.rounded_rectangle([90, 870, 990, 1010], radius=14, fill=(18, 24, 34, 255), outline=CARD_BORDER)
    draw.text((115, 895), "3 WAYS SQLi STILL BREACHES ORMs IN 2026:", font=get_font(FONT_AVENIR, 20, index=2), fill=CYAN)
    draw.text((115, 935), "1. Dynamic `ORDER BY` / `GROUP BY` injection  •  2. Second-order stored injection", font=font_mono, fill=WHITE)
    draw.text((115, 965), "3. JSON column operators (`->>`, `jsonb_extract_path`) lacking escaping", font=font_mono, fill=WHITE)
    
    # Bottom key takeaway
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "Using Prisma, TypeORM, or Sequelize does NOT make you immune to SQL injection. Whenever a developer writes raw SQL or dynamic sort clauses, attack surfaces reopen.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect injection vectors ->", handle="@cyphermatrixpvtltd", accent=CRIMSON)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d25 = [
        ("02 / 05", "VECTOR 1: ORDER BY & GROUP BY", "The Blind Spot of Parameterized Queries", [
            ("Why Prepared Statements Can't Parameterize Identifiers", "Standard SQL drivers only parameterize literal VALUES (`WHERE id = ?`). You cannot parameterize column names or sort directions in standard SQL syntax."),
            ("How Developers Cut Corners", "Developers concatenate user input directly into string templates (`ORDER BY ${sort}`), assuming input validation was handled by API middleware."),
            ("The Exploit Payload", "Attackers inject conditional blind SQL statements: `(CASE WHEN (SELECT SUBSTRING(secret_key,1,1) FROM config)='A' THEN id ELSE name END)` to dump database secrets byte-by-byte.")
        ], "VULNERABILITY: UNESCAPED DYNAMIC SQL IDENTIFIERS"),
        
        ("03 / 05", "VECTOR 2: SECOND-ORDER INJECTION", "When Safe Inputs Turn Malicious Later", [
            ("The Trojan Horse Input", "An attacker inputs a crafted payload into their account profile name: `admin'--`. The initial `INSERT` query is parameterized, so it saves safely without error."),
            ("The Fatal Backend Job", "Hours later, a nightly background cron job or admin report aggregates user names using raw string concatenation: `SELECT * FROM users WHERE name = '${user.name}'`."),
            ("Database Execution", "The single quote breaks out of the nightly query, granting unauthorized administrative privileges or dumping entire multi-tenant records.")
        ], "ATTACK MECHANISM: DELAYED ASYNCHRONOUS EXPLOITATION"),
        
        ("04 / 05", "VECTOR 3: JSONB OPERATORS", "Postgres & MySQL JSON Path Injections", [
            ("Modern NoSQL-in-SQL Complexity", "Modern web apps store nested configurations inside Postgres `JSONB` columns, using operators like `->>` or `json_extract()`."),
            ("Unescaped JSON Key Extraction", "Dynamically querying nested JSON paths based on frontend user filters often bypasses ORM sanitizers entirely."),
            ("Remote Data Exfiltration", "Attackers manipulate JSON extraction operators to pivot across sibling keys containing private tokens and hashed passwords.")
        ], "THREAT: HIGH-SEVERITY CLOUD DATABASE EXTRADITION"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Hardened Application Development & VAPT", [
            ("Comprehensive Web & API Security Audits", "Our offensive security researchers systematically test every raw query, JSON handler, and database abstraction in your codebase."),
            ("Secure Software Engineering", "We design bulletproof database access layers with strict allowlists, AST validation, and defense-in-depth principles."),
            ("Schedule Your Web VAPT Audit", "Protect your users and enterprise reputation before attackers exploit hidden database vulnerabilities.")
        ], "CYPHER MATRIX TECHNOLOGIES | OFFENSIVE SECURITY & DEVELOPMENT")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d25, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(255, 51, 102, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=CRIMSON if s_idx < 5 else EMERALD)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=CRIMSON if s_idx < 5 else EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=CRIMSON if s_idx < 5 else EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'VAPT' to test your database defenses ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CRIMSON if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 25 generated.")

# ==============================================================================
# DAY 26: BEHIND THE SPRINTS: CYPHER MATRIX GANDHINAGAR HUB (1 Creative, 1080x1350)
# ==============================================================================
def build_day26():
    folder = 'Day_26_Behind_The_Sprints_Hub'
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 40), glow_pos=(850, 450, 450))
    add_header(img, draw, category="COMPANY CULTURE & ETHOS", slide_str="CULTURE", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "INSIDE THE ENGINEERING LAB", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "BEHIND THE SPRINTS:\nINSIDE CYPHER MATRIX HUB", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "From Gandhinagar to global enterprise clients: How our dual-focus software development and offensive cybersecurity teams build digital products that scale.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # 4 Pillar Engineering Culture Cards
    pillars = [
        ("01. OFFENSIVE-FIRST ARCHITECTURE", EMERALD, "We don't build software and hand it to a third-party security auditor 6 months later. Our certified cybersecurity specialists review architecture from day zero."),
        ("02. ZERO TOLERANCE FOR RE-WRITES", CYAN, "We write clean, strictly-typed Flutter, Dart, Node.js, and Python code designed to survive 5+ years of rapid feature additions without accumulating fatal technical debt."),
        ("03. OWNERSHIP OF OUR OWN PRODUCTS", EMERALD, "We aren't just an outsourcing agency. We build and operate proprietary consumer products like Bill Mitra and Tractor Hisab—giving us real operator empathy."),
        ("04. TRANSPARENT INTERNATIONAL PARTNERSHIP", CYAN, "Zero offshore smoke and mirrors. International founders get direct Slack access to lead engineers, daily async video demos, and complete IP repository ownership.")
    ]
    curr_y = 440
    for p_t, col, p_d in pillars:
        draw_glass_card(img, 60, curr_y, 960, 165, radius=18, bg=(14, 18, 26, 245), border=CARD_BORDER)
        draw_pill_badge(draw, 90, curr_y + 18, p_t, get_font(FONT_MENLO, 18), accent_color=col)
        draw_safe_text(draw, 90, curr_y + 65, p_d, font_body, WHITE, max_width=890, line_spacing=6)
        curr_y += 185
        
    # Bottom Hub Stats Card
    draw_glass_card(img, 60, 1180, 960, 90, radius=16, bg=(16, 22, 32, 255), border=CARD_BORDER)
    draw.text((95, 1215), "CYPHER MATRIX TECHNOLOGIES  •  GANDHINAGAR, GUJARAT, INDIA  •  cyphermatrix.io", font=font_mono, fill=EMERALD)
    
    add_footer(draw, w_port, h_port, cta_text="DM 'BUILD' to start your sprint ->", handle="@cyphermatrixpvtltd", accent=EMERALD)
    save_image_both(img, folder, 'Creative_1080x1350.jpg')
    print("Day 26 generated.")

# ==============================================================================
# DAY 27: DEVSECOPS QUIZ: SECURITY SHIFT-LEFT (4 Stories, 1080x1920)
# ==============================================================================
def build_day27():
    folder = 'Day_27_DevSecOps_Quiz'
    d_dir = folder
    
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
    add_story_hdr(img, draw, "DEVSECOPS TRIVIA", "01 / 04")
    draw_safe_text(draw, 60, 230, "WHEN SHOULD CYBERSECURITY AUDITS BEGIN?", get_font(FONT_AVENIR, 48, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img, 60, 420, 960, 420, radius=24, bg=(18, 22, 32, 245), border=(0, 240, 255, 140))
    draw_safe_text(draw, 100, 470, "At what stage in the software development lifecycle should security testing happen?", get_font(FONT_AVENIR, 36, index=2), WHITE, max_width=880, line_spacing=12)
    draw.text((100, 740), "[ VOTE IN THE POLL BELOW ]", font=get_font(FONT_MENLO, 22), fill=CYAN)
    
    draw_glass_card(img, 120, 920, 840, 360, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw.text((w_reel // 2, 980), "PLACE INSTAGRAM POLL STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw.rounded_rectangle([180, 1030, 900, 1110], radius=16, fill=(24, 34, 48, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1070), "RIGHT BEFORE APP STORE LAUNCH", font=get_font(FONT_AVENIR, 24, index=2), fill=TEXT_MUTED, anchor='mm')
    draw.rounded_rectangle([180, 1140, 900, 1220], radius=16, fill=(10, 34, 20, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1180), "FROM SPRINT ZERO & CI/CD PIPELINES", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD, anchor='mm')
    
    draw.text((w_reel // 2, 1500), "Tap next to see why 'pre-launch' testing costs 30x more ->", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    save_image_both(img, d_dir, 'Story_01_Poll.jpg')
    
    # Story 2: Shift-Left Cost Reality
    img2, draw2 = create_base_canvas(w_reel, h_reel, glow_color=(255, 51, 102, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img2, draw2, "THE SHIFT-LEFT LAW", "02 / 04")
    draw_safe_text(draw2, 60, 230, "THE EXPONENTIAL COST OF DELAYED SECURITY", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960)
    
    draw_glass_card(img2, 60, 380, 960, 530, radius=24, bg=(24, 16, 22, 245), border=(255, 51, 102, 140))
    draw.text((w_reel // 2, 450), "30X HIGHER REMEDIATION COST", font=get_font(FONT_AVENIR, 50, index=2), fill=CRIMSON, anchor='mm')
    draw_safe_text(draw2, 100, 520, "Fixing an architectural flaw during Sprint Planning costs $200 in developer time. Fixing that same flaw after production deployment costs $6,000+ in emergency hotfixes, database downtime, and customer churn.", get_font(FONT_HELVETICA, 26), WHITE, max_width=880, line_spacing=8)
    
    draw_glass_card(img2, 60, 960, 960, 520, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((100, 1005), "WHY CYPHER MATRIX PRACTICES SHIFT-LEFT:", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD)
    reasons = [
        "1. Automated SAST scans on every GitHub pull request",
        "2. Secret scanning to prevent API key commits",
        "3. Container & cloud infrastructure as code (IaC) linting",
        "4. Continuous VAPT before release cut-offs"
    ]
    curr_y = 1065
    for r in reasons:
        curr_y = draw_safe_text(draw2, 100, curr_y, r, get_font(FONT_HELVETICA, 26), WHITE, max_width=880) + 16
        
    draw2.text((w_reel // 2, 1600), "Tap next to see our 4-stage pipeline ->", font=get_font(FONT_HELVETICA, 26), fill=CYAN, anchor='mm')
    save_image_both(img2, d_dir, 'Story_02_Cost_Reality.jpg')
    
    # Story 3: 4-Stage DevSecOps Pipeline
    img3, draw3 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img3, draw3, "PIPELINE BLUEPRINT", "03 / 04")
    draw_safe_text(draw3, 60, 230, "CYPHER MATRIX DEVSECOPS FLOW", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960)
    
    stages = [
        ("STAGE 1: COMMIT TIME (PRE-COMMIT)", CYAN, "TruffleHog & GitGuardian prevent developers from accidentally pushing AWS tokens, Stripe keys, or private SSH certificates."),
        ("STAGE 2: BUILD TIME (CI RUNNER)", EMERALD, "SonarQube & Semgrep analyze code semantics for SQLi, XSS, and insecure crypto before pull requests can merge."),
        ("STAGE 3: DEPLOY TIME (CD PIPELINE)", CYAN, "Trivy scans Docker container images for OS vulnerabilities, and Checkov validates Terraform AWS IAM security."),
        ("STAGE 4: RUNTIME (PRODUCTION VAPT)", CRIMSON, "Human offensive penetration testing actively probes live staging environments for complex business logic flaws.")
    ]
    for idx, (title, col, desc) in enumerate(stages):
        cy = 380 + idx * 280
        draw_glass_card(img3, 60, cy, 960, 250, radius=20, bg=(16, 22, 32, 245), border=CARD_BORDER)
        draw_pill_badge(draw3, 95, cy + 20, title, get_font(FONT_MENLO, 18), accent_color=col)
        draw_safe_text(draw3, 95, cy + 75, desc, get_font(FONT_HELVETICA, 23), WHITE, max_width=870, line_spacing=6)
        
    draw3.text((w_reel // 2, 1600), "Tap next to consult on your DevSecOps pipeline ->", font=get_font(FONT_HELVETICA, 26), fill=EMERALD, anchor='mm')
    save_image_both(img3, d_dir, 'Story_03_Pipeline.jpg')
    
    # Story 4: Q&A Box
    img4, draw4 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 40), glow_pos=(540, 900, 500))
    add_story_hdr(img4, draw4, "DEVSECOPS AUDIT", "04 / 04")
    draw_safe_text(draw4, 60, 230, "WANT TO AUTOMATE YOUR\nSECURITY PIPELINE?", get_font(FONT_AVENIR, 48, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img4, 100, 460, 880, 520, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw4.text((w_reel // 2, 530), "PLACE INSTAGRAM 'QUESTIONS' STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw4.text((w_reel // 2, 600), "Ask us how to embed automated security into GitHub Actions 👇", font=get_font(FONT_AVENIR, 26, index=2), fill=WHITE, anchor='mm')
    draw4.rounded_rectangle([160, 680, 920, 840], radius=18, fill=(24, 32, 46, 255), outline=CARD_BORDER)
    draw4.text((w_reel // 2, 760), "Type your CI/CD question...", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img4, 60, 1040, 960, 360, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw4.text((100, 1085), "CYPHER MATRIX DEVSECOPS SERVICES:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    points = [
        "✓ Automated GitHub Actions security workflow design",
        "✓ Cloud infrastructure (AWS/GCP) compliance audits",
        "✓ Ongoing vulnerability scanning & developer triage"
    ]
    curr_y = 1145
    for p in points:
        curr_y = draw_safe_text(draw4, 100, curr_y, p, get_font(FONT_HELVETICA, 24), WHITE, max_width=880) + 16
        
    draw4.text((w_reel // 2, 1580), "CYPHER MATRIX  |  cyphermatrix.io", font=get_font(FONT_MENLO, 22), fill=TEXT_MUTED, anchor='mm')
    save_image_both(img4, d_dir, 'Story_04_QA_Box.jpg')
    print("Day 27 generated.")

# ==============================================================================
# DAY 28: 10-POINT PRE-LAUNCH APPLICATION SECURITY CHECKLIST (5 Slides, 1080x1350)
# ==============================================================================
def build_day28():
    folder = 'Day_28_PreLaunch_Security_Checklist'
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="APPLICATION SECURITY CHECKLIST", slide_str="01 / 05", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "THE 10-POINT HARDENING CHECKLIST", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    draw_safe_text(draw, 60, 210, "THE 10-POINT PRE-LAUNCH\nAPPLICATION SECURITY CHECKLIST", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "Before deploying your mobile app or web platform to production users, verify your engineering team has cleared these 10 non-negotiable security controls.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Visual Checklist Preview Card
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "CYPHER MATRIX GO-LIVE SECURITY GATE: 10 AUDIT CHECKS", font=font_mono, fill=TEXT_MUTED)
    
    checks = [
        ("01. TLS 1.3 & Certificate Pinning (SPKI)", "Prevents MitM proxy attacks on mobile networks"),
        ("02. Broken Object-Level Authorization (BOLA)", "Strict owner validation on every REST/GraphQL API call"),
        ("03. SQL / NoSQL Query Parameterization", "Zero string concatenation in database lookups or sorts"),
        ("04. Code Obfuscation & R8/ProGuard Rules", "Symbols stripped to prevent 30-second reverse-engineering"),
        ("05. Client-Side Encryption of Local DB", "Encrypted SQLite/Drift databases with Android Keystore/iOS Keychain")
    ]
    curr_y = 515
    for c_t, c_d in checks:
        draw.rounded_rectangle([85, curr_y, 995, curr_y + 88], radius=12, fill=(18, 24, 34, 255), outline=CARD_BORDER)
        draw.text((110, curr_y + 14), c_t, font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
        draw.text((110, curr_y + 50), c_d, font=font_mono, fill=TEXT_MUTED)
        curr_y += 98
        
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "Deploying an app without these 10 controls is leaving your front door unlocked. Swipe through for the complete technical breakdown.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect all 10 controls ->", handle="@cyphermatrixpvtltd", accent=EMERALD)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d28 = [
        ("02 / 05", "CONTROLS 01 - 03: API & TRANSPORT", "Locking Down Data in Motion", [
            ("01. Enforce SPKI Certificate Pinning", "Pin subject public key hashes on mobile clients to render Burp Suite and Charles Proxy tools useless against your HTTPS APIs."),
            ("02. Database-Level Ownership Checks", "Never trust user tokens alone. Every query must enforce `WHERE organization_id = session.org_id` to block IDOR attacks."),
            ("03. Strict Input & Sorting Allowlisting", "Never permit client-supplied strings to dictate database sort fields or table names without regex allowlists.")
        ], "DOMAIN: API GATEWAY & DATABASE PROTECTION"),
        
        ("03 / 05", "CONTROLS 04 - 06: CLIENT-SIDE BINARY", "Hardening the Mobile Binary", [
            ("04. Aggressive ProGuard / DexGuard Obfuscation", "Strip method names, inline sensitive strings, and scramble control flows to frustrate decompilers like JADX."),
            ("05. Keystore-Backed Storage Encryption", "Never store JWTs or cached PII in plain SharedPreferences or UserDefaults. Always use EncryptedSharedPreferences and Keychain."),
            ("06. Runtime Jailbreak & Root Detection", "Detect compromised OS environments, Magisk hide modules, and active Frida debugging agents at startup.")
        ], "DOMAIN: MOBILE CLIENT BINARY HARDENING"),
        
        ("04 / 05", "CONTROLS 07 - 10: CLOUD & INFRA", "Securing Cloud Workloads", [
            ("07. S3 / Cloud Storage Public Access Block", "Enable account-wide 'Block Public Access' and audit bucket ACLs with AWS Config or GCP Security Command Center."),
            ("08. Zero-Wildcard IAM Permissions", "Eliminate `*:*` administrative roles from ECS, Lambda, or Kubernetes pod service accounts."),
            ("09. Production Secret Manager Integration", "Zero API keys committed to Git. Inject credentials via AWS Secrets Manager or HashiCorp Vault at runtime."),
            ("10. Independent Manual VAPT Certification", "Conduct a professional penetration test with verified attestation before accepting live customer funds.")
        ], "DOMAIN: CLOUD INFRASTRUCTURE & DEVSECOPS"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Get Your Free Pre-Launch Security Audit", [
            ("Cypher Matrix Pre-Launch Review", "We perform end-to-end security audits, penetration testing, and code quality assessments for growing startups and enterprises."),
            ("Attestation for Enterprise Clients", "Receive a verified Security Audit Report that satisfies institutional investors, enterprise procurement, and regulators."),
            ("Schedule Your Assessment", "Launching in the next 60 days? DM 'CHECKLIST' to book a confidential scoping call.")
        ], "CYPHER MATRIX TECHNOLOGIES | SECURE. BUILD. SCALE.")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d28, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=EMERALD)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'CHECKLIST' to audit your app ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 28 generated.")

# ==============================================================================
# DAY 29: WHY MICROSERVICES AREN'T ALWAYS THE ANSWER (5 Slides, 1080x1350)
# ==============================================================================
def build_day29():
    folder = 'Day_29_Microservices_vs_ModularMonolith'
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="BACKEND SYSTEM DESIGN", slide_str="01 / 05", accent=CYAN)
    draw_pill_badge(draw, 60, 145, "THE ARCHITECTURE DEBATE", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    draw_safe_text(draw, 60, 210, "WHY MICROSERVICES ARE KILLING\nEARLY-STAGE STARTUP VELOCITY", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "How early-stage engineering teams waste $100k+ building distributed microservice complexity before finding product-market fit, and why a Modular Monolith wins.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Architectural Comparison Card
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "STARTUP INFRASTRUCTURE: PREMATURE MICROSERVICES VS MODULAR MONOLITH", font=font_mono, fill=TEXT_MUTED)
    
    # Left Box: Premature Microservices
    draw.rounded_rectangle([90, 510, 520, 880], radius=14, fill=(24, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 535), "PREMATURE MICROSERVICES", font=get_font(FONT_AVENIR, 19, index=2), fill=CRIMSON)
    points_ms = [
        "❌ 12 Kubernetes services for 500 users",
        "❌ Network latency on internal RPC calls",
        "❌ Two-phase commit database nightmares",
        "❌ Distributed tracing hell (Jaeger/Datadog)",
        "❌ $4,000/mo cloud bills on Day 1",
        "❌ Simple schema changes require 4 PRs"
    ]
    for idx, p in enumerate(points_ms):
        draw_safe_text(draw, 115, 580 + idx * 48, p, font=get_font(FONT_HELVETICA, 17), fill=(255, 180, 190, 255), max_width=380, line_spacing=2)
    draw.text((115, 890), "Result: 70% Time Spent on DevOps", font=font_mono, fill=CRIMSON)
    
    # Right Box: Modular Monolith
    draw.rounded_rectangle([550, 510, 980, 880], radius=14, fill=(10, 24, 18, 255), outline=(0, 255, 136, 120))
    draw.text((575, 535), "MODULAR MONOLITH (WINNER)", font=get_font(FONT_AVENIR, 19, index=2), fill=EMERALD)
    points_mm = [
        "✅ Clean bounded contexts in one repo",
        "✅ In-memory function calls (0ms latency)",
        "✅ Single ACID transaction consistency",
        "✅ Trivial local development & Docker setup",
        "✅ $50/mo cloud bill on single cluster",
        "✅ Can extract services later when needed"
    ]
    for idx, p in enumerate(points_mm):
        draw_safe_text(draw, 575, 580 + idx * 48, p, font=get_font(FONT_HELVETICA, 17), fill=(180, 255, 210, 255), max_width=380, line_spacing=2)
    draw.text((575, 890), "Result: 95% Time Spent on Product", font=font_mono, fill=EMERALD)
    
    # Bottom key takeaway
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "You are not Google or Netflix. Designing distributed systems before having paying customers is premature optimization that kills startup survival.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect architecture ->", handle="@cyphermatrixpvtltd", accent=CYAN)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d29 = [
        ("02 / 05", "THE DISTRIBUTED COMPLEXITY TRAP", "Where Microservices Secretly Bleed Cash", [
            ("Network Boundary Latency & Failures", "When a single user request cascades across 6 microservices over HTTP/gRPC, any packet drop, timeout, or circuit-breaker trip fails the user transaction."),
            ("Distributed Data Consistency (Saga Pattern)", "Without single-database ACID guarantees, maintaining order status, inventory depletion, and payment capture requires complex asynchronous compensating transactions."),
            ("DevOps Overhead for Small Teams", "A team of 4 engineers spends more time managing Helm charts, service meshes (Istio), and Docker clusters than writing revenue-generating features.")
        ], "COST FACTOR: 3X ENGINEERING OVERHEAD FOR INFRASTRUCTURE"),
        
        ("03 / 05", "THE MODULAR MONOLITH SOLUTION", "Clean Separation Without Network Penalties", [
            ("Domain-Driven Bounded Contexts", "Organize code into strict decoupled modules: `AuthModule`, `BillingModule`, `CatalogModule`. Modules communicate via strict public interfaces, not private internals."),
            ("Single Database with Logical Schemas", "Benefit from atomic foreign keys, instant database migrations, and zero distributed transaction locks."),
            ("Instant Future Decomposition", "Because modules have zero circular dependencies, extracting high-throughput services into standalone microservices later takes days—not months.")
        ], "ADVANTAGE: MAXIMUM VELOCITY WITH CLEAN ARCHITECTURE"),
        
        ("04 / 05", "WHEN SHOULD YOU ACTUALLY DECOMPOSE?", "The True Signals for Microservice Migration", [
            ("1. Independent Deployment Velocity", "When 30+ engineers are blocking each other on continuous deployment merges for unrelated business domains."),
            ("2. Asymmetric Resource Requirements", "When one specific component (like real-time video transcoding or ML vector inference) requires heavy GPU clusters while the REST API needs lightweight CPUs."),
            ("3. Strict Regulatory Data Isolation", "When payment compliance (PCI-DSS) or health data (HIPAA) mandates that credit card data live on an isolated physical network.")
        ], "TIMING: DECOMPOSE WHEN CONSTRAINTS DEMAND IT, NEVER BY DEFAULT"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Pragmatic Product Architecture at Cypher Matrix", [
            ("Built for Scalable Real-World Growth", "We design pragmatic backend architectures that optimize for developer speed, low infrastructure bills, and seamless future scale."),
            ("Zero DevOps Vanity Metrics", "We focus on code that works reliably, passes offensive security audits, and delivers business ROI."),
            ("Architect Your Product with Us", "Planning a new SaaS or mobile backend? DM 'ARCHITECTURE' to review your system design with our leads.")
        ], "CYPHER MATRIX TECHNOLOGIES | SECURE. BUILD. SCALE.")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d29, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=CYAN)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=CYAN if s_idx < 5 else EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=CYAN if s_idx < 5 else EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'ARCHITECTURE' to scope your backend ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CYAN if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 29 generated.")

# ==============================================================================
# DAY 30: TRACTOR HISAB: SEASON FINANCIAL AUDIT (Reel Cover + Telemetry, 1080x1920)
# ==============================================================================
def build_day30():
    folder = 'Day_30_TractorHisab_Season_Audit'
    
    # Reel Cover
    img, draw = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 40), glow_pos=(540, 960, 550))
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((260, 80), Image.Resampling.LANCZOS)
        img.alpha_composite(logo, (w_reel // 2 - logo.size[0] // 2, 140))
        
    draw_pill_badge(draw, (w_reel - 380) // 2, 260, "AGRITECH PRODUCT REEL", get_font(FONT_MENLO, 20), accent_color=EMERALD)
    draw.text((w_reel // 2, 380), "TRACTOR HISAB", font=get_font(FONT_AVENIR, 64, index=2), fill=EMERALD, anchor='mm')
    draw.text((w_reel // 2, 455), "Season khatam, par kisaano ki udhari kitni baaki hai?", font=get_font(FONT_AVENIR, 28, index=2), fill=WHITE, anchor='mm')
    draw.text((w_reel // 2, 510), "Ek click mein dekhein poore season ka profit aur udhari:", font=get_font(FONT_HELVETICA, 24), fill=TEXT_MUTED, anchor='mm')
    
    # 3 Summary Audit Cards
    draw_glass_card(img, 80, 580, 920, 980, radius=24, bg=(16, 22, 32, 245), border=(0, 255, 136, 120))
    draw.text((120, 625), "SEASON FINANCIAL REPORT CARD:", font=get_font(FONT_MENLO, 20), fill=CYAN)
    
    audits = [
        ("01. Kisaan-wise Total Udhari Report", "Season ke ant mein kis kisaan par kitne rupaye baaki hain, ek click par PDF banakar WhatsApp par payment reminder bhejein."),
        ("02. Diesel kharch vs Total Jotai Munafa", "Pata karein kis khet mein kitna diesel laga aur kitni kamai hui. Pura fuel telemetry hisab saaf aur transparent."),
        ("03. Driver Advance aur Bata hisab", "Driver ka advance cash, daily bata aur salary hisab clear—koi bahas ya hisab mein gadbadi nahi.")
    ]
    for idx, (m_head, m_desc) in enumerate(audits):
        my = 675 + idx * 280
        draw.rounded_rectangle([120, my, 960, my + 250], radius=16, fill=(10, 14, 22, 255), outline=CARD_BORDER)
        draw_pill_badge(draw, 145, my + 20, m_head, get_font(FONT_MENLO, 18), accent_color=EMERALD)
        draw_safe_text(draw, 145, my + 75, m_desc, get_font(FONT_HELVETICA, 22), WHITE, max_width=770, line_spacing=6)
        
    draw_glass_card(img, 80, 1600, 920, 175, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 160))
    draw.text((w_reel // 2, 1650), "TRACTOR HISAB: KISAANO AUR TRACTOR MALIKON KA SAATHI", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD, anchor='mm')
    draw.text((w_reel // 2, 1705), "Watch this 45-second Reel to audit your tractor season accounts.", font=get_font(FONT_HELVETICA, 24), fill=WHITE, anchor='mm')
    draw.text((w_reel // 2, 1840), "CYPHER MATRIX PRODUCT  |  @cyphermatrixpvtltd", font=get_font(FONT_MENLO, 20), fill=TEXT_MUTED, anchor='mm')
    save_image_both(img, folder, 'Reel_Cover_1080x1920.jpg')
    
    # Telemetry Feature Card
    t_img, t_draw = create_base_canvas(w_reel, h_reel, glow_color=(0, 240, 255, 35), glow_pos=(540, 1000, 500))
    draw_pill_badge(t_draw, 80, 120, "TRACTOR HISAB TELEMETRY", get_font(FONT_MENLO, 22), accent_color=EMERALD)
    t_draw.text((80, 200), "COMPLETE SEASON TELEMETRY", font=get_font(FONT_AVENIR, 48, index=2), fill=WHITE)
    t_draw.text((80, 265), "Engineered for clarity, speed & rural offline performance:", font=get_font(FONT_HELVETICA, 24), fill=TEXT_MUTED)
    
    feats = [
        ("AUTOMATED WHATSAPP RECEIPTS", CYAN, "Kisaan ko turant khet par hi WhatsApp bill bhejein. Transparency se payment jaldi aati hai."),
        ("MULTI-TRACTOR FLEET SUPPORT", EMERALD, "Ek se zyada tractor hain? Ek hi app mein sabhi tractors aur drivers ka hisab alag-alag manage karein."),
        ("OFFLINE RURAL CLOUD SYNC", CYAN, "Bina internet ke bhi khet mein entries karein. Internet aate hi automatic secure cloud backup."),
        ("SAFE FROM PHONE DAMAGE", EMERALD, "Phone khone ya kharab hone par bhi naye phone mein login karte hi sara purana hisab turant wapas.")
    ]
    for idx, (f_h, col, f_d) in enumerate(feats):
        fy = 330 + idx * 310
        draw_glass_card(t_img, 80, fy, 920, 280, radius=20, bg=(18, 24, 34, 240), border=CARD_BORDER)
        draw_pill_badge(t_draw, 110, fy + 22, f_h, get_font(FONT_MENLO, 19), accent_color=col)
        draw_safe_text(t_draw, 110, fy + 80, f_d, get_font(FONT_HELVETICA, 23), WHITE, max_width=860, line_spacing=6)
        
    draw_glass_card(t_img, 80, 1630, 920, 180, radius=20, bg=(14, 20, 28, 250), border=(0, 255, 136, 160))
    t_draw.text((w_reel // 2, 1685), "DM 'TRACTOR' FOR PRODUCT ACCESS & DEMO", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD, anchor='mm')
    t_draw.text((w_reel // 2, 1740), "Engineered by Cypher Matrix Technologies", font=get_font(FONT_HELVETICA, 22), fill=TEXT_MUTED, anchor='mm')
    save_image_both(t_img, folder, 'OnScreen_Telemetry_1080x1920.jpg')
    print("Day 30 generated.")

if __name__ == '__main__':
    build_day22()
    build_day23()
    build_day24()
    build_day25()
    build_day26()
    build_day27()
    build_day28()
    build_day29()
    build_day30()
    print("Week 04 completely generated successfully!")
