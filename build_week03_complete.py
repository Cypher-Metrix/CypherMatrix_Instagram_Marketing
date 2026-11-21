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

WEEK3_DIR_USER = os.path.join(BASE_DIR_USER, '04_Post_Creatives', 'Week_03')
WEEK3_DIR_GEMINI = os.path.join(BASE_DIR_GEMINI, '04_Post_Creatives', 'Week_03')
os.makedirs(WEEK3_DIR_USER, exist_ok=True)
os.makedirs(WEEK3_DIR_GEMINI, exist_ok=True)

w_port, h_port = 1080, 1350
w_sq, h_sq = 1080, 1080
w_reel, h_reel = 1080, 1920

def save_image_both(img, rel_folder, filename):
    for base in [WEEK3_DIR_USER, WEEK3_DIR_GEMINI]:
        folder = os.path.join(base, rel_folder)
        os.makedirs(folder, exist_ok=True)
        out_path = os.path.join(folder, filename)
        img.convert('RGB').save(out_path, quality=95)

# ==============================================================================
# DAY 15: VOICE AI INTEGRATION IN MOBILE APPS (5 Slides, 1080x1350)
# ==============================================================================
def build_day15():
    folder = 'Day_15_Voice_AI_Mobile_Apps'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="MOBILE AI ENGINEERING", slide_str="01 / 05", accent=CYAN)
    draw_pill_badge(draw, 60, 145, "LOW-LATENCY STREAMING ARCHITECTURE", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    font_hero = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "VOICE AI IN MOBILE APPS:\nTHE REALTIME WEBSOCKET BLUEPRINT", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "Why standard REST APIs fail for voice assistants, and how we engineer sub-350ms conversational latency in Flutter & Native.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Terminal comparison card
    draw_glass_card(img, 60, 450, 960, 620, radius=20, bg=(12, 16, 24, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "LATENCY BENCHMARK: REST PIPELINE VS REALTIME WEBSOCKET", font=font_mono, fill=TEXT_MUTED)
    
    # Left column: The Broken REST Way
    draw.rounded_rectangle([90, 510, 520, 880], radius=14, fill=(20, 14, 18, 255), outline=(255, 51, 102, 100))
    draw.text((110, 530), "LEGACY REST PIPELINE", font=get_font(FONT_AVENIR, 20, index=2), fill=CRIMSON)
    draw.text((110, 565), "End-to-End Latency: ~2,800ms", font=font_mono, fill=CRIMSON)
    steps_rest = [
        "1. App records full audio clip (WAV/M4A)",
        "2. Upload complete clip to REST server",
        "3. Whisper ASR transcribes to text",
        "4. LLM processes text & returns completion",
        "5. TTS engine synthesizes MP3 file",
        "6. App downloads & plays whole audio"
    ]
    for idx, s in enumerate(steps_rest):
        draw_safe_text(draw, 110, 610 + idx * 42, s, font=get_font(FONT_HELVETICA, 17), fill=(255, 180, 190, 255), max_width=390, line_spacing=2)
    draw.text((110, 890), "User Experience: Awkward 3s pauses", font=font_mono, fill=CRIMSON)
    
    # Right column: The Cypher Matrix Way
    draw.rounded_rectangle([550, 510, 980, 880], radius=14, fill=(10, 22, 18, 255), outline=(0, 255, 136, 120))
    draw.text((570, 530), "CYPHER MATRIX REALTIME", font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
    draw.text((570, 565), "End-to-End Latency: ~320ms", font=font_mono, fill=EMERALD)
    steps_cm = [
        "1. Stream raw PCM16/Opus 24kHz audio",
        "2. Bi-directional persistent WebSocket",
        "3. Server Voice Activity Detection (VAD)",
        "4. Token-by-token audio streaming back",
        "5. Sub-millisecond client audio buffer",
        "6. Instant interruption on user speech"
    ]
    for idx, s in enumerate(steps_cm):
        draw_safe_text(draw, 570, 610 + idx * 42, s, font=get_font(FONT_HELVETICA, 17), fill=(180, 255, 210, 255), max_width=390, line_spacing=2)
    draw.text((570, 890), "User Experience: True human flow", font=font_mono, fill=EMERALD)
    
    # Bottom key metrics banner
    draw.rounded_rectangle([90, 940, 980, 1045], radius=12, fill=(16, 22, 32, 255), outline=CARD_BORDER)
    draw.text((115, 960), "PRODUCTION BENCHMARK AT CYPHER MATRIX:", font=get_font(FONT_AVENIR, 20, index=2), fill=WHITE)
    draw.text((115, 995), "320ms voice response  •  Full client interruption support  •  Sub-15kbps bandwidth", font=font_mono, fill=CYAN)
    
    # Highlight pill
    draw_glass_card(img, 60, 1100, 960, 140, radius=16, bg=(14, 20, 30, 240), border=CARD_BORDER)
    draw_safe_text(draw, 90, 1130, "Inside this masterclass: Audio streaming mechanics, client-side VAD, echo cancellation, and native Flutter bridge architecture.", font_body, WHITE, max_width=900, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect architecture ->", handle="@cyphermatrixpvtltd", accent=CYAN)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d15 = [
        ("02 / 05", "AUDIO STREAMING & CODEC SELECTION", "Why Opus 24kHz is the Gold Standard for Mobile Voice AI", [
            ("PCM16 vs Opus Compression", "Sending uncompressed PCM16 audio consumes ~384 kbps of upload bandwidth—causing packet drops on mobile LTE. We transcode to Opus 24kHz (16-32 kbps), preserving pristine human speech clarity at 92% bandwidth savings."),
            ("Bi-Directional WebSocket Framing", "Standard HTTP/2 cannot stream duplex low-latency binary chunks with sub-10ms framing. A persistent WebSocket channel multiplexes user audio in, model audio out, and JSON function call telemetry."),
            ("Dynamic Bitrate Adaptation", "Our mobile client monitors packet round-trip time (RTT). If cell coverage degrades, audio frame size adapts dynamically between 20ms and 60ms without dropping the conversational session.")
        ], "AUDIO PROTOCOL: RFC 6716 OPUS | 24,000 HZ SAMPLE RATE"),
        
        ("03 / 05", "HANDLING THE HARDEST MOBILE PROBLEM", "Acoustic Echo Cancellation (AEC) & Barge-In", [
            ("The Feedback Loop Disaster", "When the AI voice speaks through the phone speaker, the device microphone picks it up and loops it back into the WebSocket—causing the AI to interrupt itself. Standard mobile audio APIs fail here."),
            ("Hardware-Accelerated AEC", "We route mobile audio through native hardware AEC pipelines (`VoiceProcessingIO` on iOS and `VOICE_COMMUNICATION` audio mode on Android AudioManager) to cancel speaker bleed before it hits the socket."),
            ("Server-Side VAD & Instant Barge-In", "When the user interrupts mid-sentence, the server detects human voice activity (VAD) within 80ms, halts the current audio generation pipeline, and clears the client playback buffer instantly.")
        ], "HARDWARE PIPELINES: iOS VoiceProcessingIO | Android VOICE_COMMUNICATION"),
        
        ("04 / 05", "LOCAL TOOL CALLING & DEVICE INTEGRATION", "Connecting Realtime Voice to Native App Actions", [
            ("Client-Side Function Calling", "Voice AI isn't just a chatbot—it controls the app. The LLM emits structured JSON tool calls over the WebSocket: `create_invoice()`, `navigate_to_cart()`, or `initiate_vapt_scan()`."),
            ("Zero-Latency Optimistic UI Execution", "While the voice assistant acknowledges the action verbally ('Adding 5 items to your invoice'), the mobile client executes the local state mutation immediately."),
            ("Session State Recovery", "If the user drives through a cellular dead zone, our offline event queue buffers microphone audio and synchronizes speech context seamlessly upon reconnection.")
        ], "AGENT PROTOCOL: STRUCTURED JSON SCHEMA | BIDIRECTIONAL TOOL CALLING"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Ready to Build Voice-First Mobile AI Applications?", [
            ("Production Reference Architecture", "We build enterprise-grade voice AI interfaces into Flutter, iOS, and Android applications—optimized for sub-350ms conversational latency and rock-solid edge stability."),
            ("End-to-End Encryption & Privacy", "Audio streams are encrypted with TLS 1.3. Zero audio retention policies ensure complete user privacy and regulatory compliance."),
            ("Consult with Our Senior Engineers", "Whether you're building hands-free logistics apps, smart retail assistants, or enterprise AI workflows—we engineer the entire stack.")
        ], "CYPHER MATRIX TECHNOLOGIES | GANDHINAGAR & GLOBAL")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d15, 2):
        s_img, s_draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 30), glow_pos=(800, 300, 450))
        add_header(s_img, s_draw, category=s_badge, slide_str=s_num, accent=CYAN)
        draw_safe_text(s_draw, 60, 150, s_title, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=960, line_spacing=8)
        
        y_pos = 260
        for c_title, c_desc in cards:
            draw_glass_card(s_img, 60, y_pos, 960, 230, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
            draw_pill_badge(s_draw, 90, y_pos + 20, c_title, get_font(FONT_MENLO, 18), accent_color=CYAN if s_idx < 5 else EMERALD)
            draw_safe_text(s_draw, 90, y_pos + 70, c_desc, font_body, WHITE, max_width=900, line_spacing=6)
            y_pos += 260
            
        # Terminal note at bottom
        draw.rounded_rectangle([60, 1080, 1020, 1170], radius=14, fill=(12, 16, 24, 255), outline=CARD_BORDER)
        s_draw.text((90, 1115), f"[ {footer_txt} ]", font=font_mono, fill=CYAN if s_idx < 5 else EMERALD)
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'VOICE' to consult our team ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CYAN if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 15 generated.")

# ==============================================================================
# DAY 16: BILL MITRA VS TRADITIONAL DESKTOP BILLING (5 Slides, 1080x1080 Square)
# ==============================================================================
def build_day16():
    folder = 'Day_16_BillMitra_vs_Desktop_Billing'
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
    draw_pill_badge(draw, 260, 48, "PRODUCT TEARDOWN", get_font(FONT_MENLO, 18), accent_color=EMERALD)
    draw.text((w - 140, 52), "01 / 05", font=get_font(FONT_MENLO, 20), fill=TEXT_MUTED)
    draw.line([(50, 105), (w - 50, 105)], fill=SLATE_LINE, width=1)
    
    draw_safe_text(draw, 60, 135, "BILL MITRA VS 10-YEAR-OLD\nDESKTOP BILLING SOFTWARE", font_hero, WHITE, max_width=960, line_spacing=8)
    draw_safe_text(draw, 60, 245, "Why modern retail and wholesale businesses are abandoning heavy desktop PCs for cloud-synced mobile POS engines.", font_body, TEXT_MUTED, max_width=960)
    
    # Comparison Container
    draw_glass_card(img, 60, 320, 960, 610, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    
    # Legacy Desktop Box
    draw.rounded_rectangle([90, 350, 510, 830], radius=16, fill=(20, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 375), "TRADITIONAL DESKTOP PC", font=get_font(FONT_AVENIR, 20, index=2), fill=CRIMSON)
    points_legacy = [
        "❌ Stuck behind counter desk",
        "❌ Requires expensive heavy PC ($500+)",
        "❌ Vulnerable to hard drive crash",
        "❌ Thermal printer cable mess",
        "❌ Manual pen-drive Tally backup",
        "❌ No real-time stock alert on phone"
    ]
    for idx, p in enumerate(points_legacy):
        draw_safe_text(draw, 115, 430 + idx * 62, p, font=get_font(FONT_HELVETICA, 18), fill=(255, 180, 190, 255), max_width=380, line_spacing=4)
    draw.text((115, 850), "Cost: High | Flexibility: Zero", font=font_mono, fill=CRIMSON)
    
    # Bill Mitra Box
    draw.rounded_rectangle([550, 350, 970, 830], radius=16, fill=(10, 24, 18, 255), outline=(0, 255, 136, 140))
    draw.text((575, 375), "BILL MITRA (SMART POS)", font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
    points_bm = [
        "✅ Bill anywhere from your Android phone",
        "✅ Works on existing $100 smartphones",
        "✅ 100% Automatic encrypted cloud sync",
        "✅ Instant wireless Bluetooth thermal print",
        "✅ 1-Click WhatsApp PDF invoice dispatch",
        "✅ Live inventory alerts in your pocket"
    ]
    for idx, p in enumerate(points_bm):
        draw_safe_text(draw, 575, 430 + idx * 62, p, font=get_font(FONT_HELVETICA, 18), fill=(180, 255, 210, 255), max_width=380, line_spacing=4)
    draw.text((575, 850), "Cost: $0 Free Start | Flexibility: 100%", font=font_mono, fill=EMERALD)
    
    # Footer banner
    draw.line([(50, h - 80), (w - 50, h - 80)], fill=SLATE_LINE, width=1)
    draw.text((50, h - 55), "BILL MITRA  |  Google Play Store", font=font_mono, fill=TEXT_MUTED)
    draw.text((w - 380, h - 55), "Swipe for full feature matrix ->", font=get_font(FONT_AVENIR, 18, index=2), fill=EMERALD)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5
    slides_d16 = [
        ("02 / 05", "HARDWARE FREEDOM", "Ditch the Bulky $600 Desktop Setup", [
            ("Run on Any Android Smartphone", "You don't need a heavy computer desk or dedicated operator. Download Bill Mitra on any Android phone and turn it into a high-speed barcode checkout terminal in under 60 seconds."),
            ("Wireless Bluetooth Thermal Printing", "Connect directly to portable 2-inch or 3-inch ESC/POS thermal printers via Bluetooth. Print instant receipts on the go or hand paperless invoices over WhatsApp.")
        ], "HARDWARE REQUIREMENT: ANDROID PHONE + BLUETOOTH THERMAL PRINTER"),
        
        ("03 / 05", "SPEED & PRODUCTIVITY", "The 4-Second Rush Hour Checkout Flow", [
            ("Instant Barcode Scanning", "Use your phone camera or connect a handheld wireless barcode scanner. Add items, calculate GST, apply discounts, and print bills in 4 seconds flat."),
            ("Eliminate Long Counter Queues", "During peak festival rush or weekend spikes, your staff can walk the floor with phones and bill customers right in the aisle—cutting checkout bottlenecks by 70%.")
        ], "CHECKOUT BENCHMARK: SUB-4 SECOND INVOICE GENERATION"),
        
        ("04 / 05", "AUTOMATIC CLOUD & OFFLINE-FIRST", "Never Lose a Single Rupee of Accounts Data", [
            ("100% Offline Resilience", "Power outage? Internet disconnected? Bill Mitra keeps billing offline without missing a beat. All records sync automatically the second connectivity returns."),
            ("Multi-Device Owner Telemetry", "Check your store's total daily sales, cash in drawer, and low stock warnings live from home on your personal phone—even when you're away from the shop.")
        ], "DATA SECURITY: 256-BIT ENCRYPTION | AUTOMATIC REALTIME BACKUP"),
        
        ("05 / 05", "GET STARTED FREE", "Experience the Future of Smart Retail Billing", [
            ("Zero Hardware Lock-In", "Start with the Free plan on your phone today. No complex installation, no IT engineer visits, and no yearly server maintenance contracts."),
            ("Trusted by Growing Businesses", "From supermarkets and apparel boutiques to wholesale distributors—Bill Mitra is engineered for speed, simplicity, and scale.")
        ], "AVAILABLE ON GOOGLE PLAY STORE | SEARCH 'BILL MITRA'")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d16, 2):
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
        s_cta = "Swipe to compare ->" if s_idx < 5 else "Download on Google Play ->"
        s_draw.text((w - 380, h - 55), s_cta, font=get_font(FONT_AVENIR, 18, index=2), fill=EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 16 generated.")

# ==============================================================================
# DAY 17: CASE STUDY: GLAD AI & WORKSPACE SUITE (5 Slides, 1080x1350)
# ==============================================================================
def build_day17():
    folder = 'Day_17_CaseStudy_GladAI_Workspace'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 240, 255, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="ENTERPRISE CASE STUDY", slide_str="01 / 05", accent=CYAN)
    draw_pill_badge(draw, 60, 145, "ENTERPRISE WORKSPACE & AI SUITE", get_font(FONT_MENLO, 19), accent_color=CYAN)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "CASE STUDY: GLAD AI\nENTERPRISE COLLABORATION SUITE", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "How Cypher Matrix engineered a unified workspace combining generative AI copilots, document intelligence, and real-time team insights.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Project Snapshot Terminal
    draw_glass_card(img, 60, 450, 960, 540, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.text((95, 480), "SYSTEM ARCHITECTURE METRICS:", font=get_font(FONT_AVENIR, 24, index=2), fill=CYAN)
    
    metrics = [
        ("CLIENT DEPLOYMENT", "Glad AI Technologies — Global Remote Enterprise"),
        ("CORE CHALLENGE", "Fragmented chat, disconnected docs, and manual invoice reconciliation"),
        ("ENGINEERING SOLUTION", "Full-stack Flutter + Node microservices + Embedded LLM Vector Engine"),
        ("DATA PRIVACY", "Zero data retention on third-party AI APIs; Private VPC isolation"),
        ("IMPACT AT SCALE", "3.8x faster document search • 60% reduction in status meetings")
    ]
    curr_y = 535
    for k, v in metrics:
        draw.text((95, curr_y), k, font=font_mono, fill=CYAN)
        curr_y = draw_safe_text(draw, 95, curr_y + 28, v, font_body, WHITE, max_width=890) + 20
        
    # Embed actual Glad AI asset preview if exists
    glad_ref = os.path.join(REF_DIR, 'glad-ai-illustration.png')
    if os.path.exists(glad_ref):
        try:
            g_img = Image.open(glad_ref).convert('RGBA')
            g_img.thumbnail((400, 220), Image.Resampling.LANCZOS)
            img.alpha_composite(g_img, (580, 740))
        except:
            pass
            
    # Bottom key takeaway
    draw_glass_card(img, 60, 1030, 960, 210, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((95, 1060), "THE ENTERPRISE AI TAKEAWAY:", font=get_font(FONT_AVENIR, 22, index=2), fill=EMERALD)
    draw_safe_text(draw, 95, 1105, "Generic chatbots don't move enterprise productivity. AI must be deeply integrated into the daily file systems, invoicing pipelines, and team permission graphs.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect architecture ->", handle="@cyphermatrixpvtltd", accent=CYAN)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d17 = [
        ("02 / 05", "THE CLIENT CHALLENGE", "Siloed Knowledge & Exploding Tool Sprawl", [
            ("The 5-Tab Chaos", "Enterprise teams used Slack for chat, Google Docs for specs, Notion for wikis, and QuickBooks for billing—spending 2.5 hours daily searching for context across tabs."),
            ("Lack of Document Intelligence", "New hires and project managers struggled to locate previous client contracts, technical specifications, and historical invoice approvals buried across nested cloud folders."),
            ("Sensitive Data Leak Risks", "Employees pasted sensitive company financial data into consumer AI chat apps without enterprise audit logging or data residency controls.")
        ], "CHALLENGE: 40% LOSS IN EXECUTIVE PRODUCTIVITY DUE TO TOOL FRAGMENTATION"),
        
        ("03 / 05", "THE CYPHER MATRIX SOLUTION", "Unified Workspace + Private Context Engine", [
            ("Single Multiplatform Workspace", "Engineered a high-performance Flutter desktop & mobile application backed by scalable microservices—unifying real-time messaging, tasks, and document management."),
            ("Private Vector Search & RAG Pipeline", "Implemented local vector embeddings with Milvus and Postgres pgvector. When team members ask questions, Glad AI retrieves answers strictly from verified company documents."),
            ("Role-Based Access Control (RBAC)", "Fine-grained permissions ensure AI answers never expose restricted payroll or executive data to unauthorized department members.")
        ], "ARCHITECTURE: FLUTTER MULTIPLATFORM + PGVECTOR + SECURE ENTERPRISE RBAC"),
        
        ("04 / 05", "PRODUCTION IMPACT & METRICS", "Measurable Operational ROI in 90 Days", [
            ("3.8x Faster Document Retrieval", "Semantic natural-language query engine cut document lookup time from 18 minutes to under 5 seconds."),
            ("60% Fewer Status Meetings", "Automated daily project summarization kept international team leads aligned asynchronously across 6 time zones."),
            ("Bank-Grade Security Compliance", "Passed comprehensive penetration testing with SOC 2 readiness—ensuring zero data leakage across multi-tenant enterprise organizations.")
        ], "RESULTS: 380% RETRIEVAL EFFICIENCY | SOC 2 READINESS VERIFIED"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Build Custom AI Solutions for Your Enterprise", [
            ("Custom LLM & Agent Workflows", "We design, build, and deploy production-ready AI workspaces, customer service copilots, and intelligent workflow engines tailored to your proprietary data."),
            ("Offensive Security Hardening", "Every AI interface we engineer undergoes rigorous LLM prompt injection and API security testing before launch."),
            ("Schedule a Strategic Architecture Call", "Discuss your custom enterprise software roadmap with our engineering team.")
        ], "CYPHER MATRIX TECHNOLOGIES | B2B SOFTWARE & SECURITY")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d17, 2):
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
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'GLAD' to consult our team ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CYAN if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 17 generated.")

# ==============================================================================
# DAY 18: WHAT HAPPENS DURING A PROFESSIONAL VAPT AUDIT? (5 Slides, 1080x1350)
# ==============================================================================
def build_day18():
    folder = 'Day_18_Inside_VAPT_Audit'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(255, 51, 102, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="CYBERSECURITY CONSULTING", slide_str="01 / 05", accent=CRIMSON)
    draw_pill_badge(draw, 60, 145, "OFFENSIVE SECURITY DEMYSTIFIED", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "WHAT ACTUALLY HAPPENS\nDURING A CYPHER MATRIX VAPT AUDIT?", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "A transparent step-by-step breakdown of how ethical offensive security experts simulate real-world attacks to protect your company's data.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Audit Pipeline Visual Container
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "CYPHER MATRIX 5-PHASE VAPT METHODOLOGY", font=font_mono, fill=TEXT_MUTED)
    
    phases = [
        ("PHASE 01: RECONNAISSANCE & SCOPING", "Attack surface discovery, subdomains, shadow APIs, and threat modeling."),
        ("PHASE 02: AUTOMATED VULNERABILITY SCANNING", "High-coverage vulnerability baselining using Burp Suite Professional, Nuclei & custom scripts."),
        ("PHASE 03: MANUAL OFFENSIVE EXPLOITATION", "The critical differentiator: business logic flaws, IDOR, privilege escalation, and token forgery."),
        ("PHASE 04: ACTIONABLE REPORTING & CVSS SCORING", "Detailed PoC videos, CVSS 3.1 severity scores, and exact code-level remediation steps."),
        ("PHASE 05: VERIFICATION & RETESTING", "Retesting all patched endpoints to issue a verified Security Attestation Certificate.")
    ]
    curr_y = 515
    for p_h, p_d in phases:
        draw.rounded_rectangle([85, curr_y, 995, curr_y + 88], radius=12, fill=(18, 24, 34, 255), outline=CARD_BORDER)
        draw_pill_badge(draw, 105, curr_y + 12, p_h, get_font(FONT_MENLO, 17), accent_color=CRIMSON if '03' in p_h else CYAN if '01' in p_h or '02' in p_h else EMERALD)
        draw_safe_text(draw, 105, curr_y + 48, p_d, get_font(FONT_HELVETICA, 18), WHITE, max_width=860)
        curr_y += 98
        
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "A real penetration test is NOT just running an automated scanner and generating an unhelpful 200-page PDF. It is manual adversarial thinking.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect methodology ->", handle="@cyphermatrixpvtltd", accent=CRIMSON)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d18 = [
        ("02 / 05", "PHASE 1 & 2: RECONNAISSANCE", "Mapping Every Inch of Your Digital Attack Surface", [
            ("Passive & Active Intelligence Gathering", "Before touching your systems, we map every publicly accessible asset—forgotten staging subdomains, exposed S3 buckets, GitHub secret leaks, and unversioned v1 API endpoints."),
            ("Threat Modeling the Business Architecture", "We analyze how user roles interact with payments, database records, and third-party integrations to pinpoint high-value target areas."),
            ("Targeted Automated Baseline", "Running calibrated security scanners to eliminate low-hanging fruit (known CVEs, outdated libraries, TLS configuration weaknesses) without disrupting production traffic.")
        ], "STANDARDS: OWASP ASVS 4.0 | NIST SP 800-115 | SANS TOP 25"),
        
        ("03 / 05", "PHASE 3: MANUAL OFFENSIVE EXPLOITATION", "Where 80% of Critical Vulnerabilities Are Found", [
            ("Broken Object-Level Authorization (BOLA/IDOR)", "Testing if User A can view or edit User B's invoices or sensitive documents simply by modifying a record ID in the API payload."),
            ("Business Logic Abuse", "Manipulating cart quantities, bypassing coupon limits, skipping payment validation webhooks, or racing concurrent requests to duplicate balances."),
            ("Account Takeover & JWT Flaws", "Exploiting weak cryptographic signatures, unvalidated redirect URIs, or token replay vulnerabilities in OAuth2 and authentication flows.")
        ], "OFFENSIVE RIGOR: CERTIFIED OSCP / CEH SECURITY RESEARCHERS"),
        
        ("04 / 05", "PHASE 4 & 5: REPORTING & RETESTING", "Developer-Ready Fixes, Not Academic Theory", [
            ("Reproducible Proof-of-Concepts (PoCs)", "Every vulnerability includes exact `curl` commands, HTTP request/response dumps, and video walkthroughs so your developers can recreate it in 2 minutes."),
            ("Line-by-Line Code Remediation", "We don't just say 'fix your auth'—we provide specific code snippets in Node.js, Python, Flutter, or Java demonstrating the secure implementation."),
            ("Compliant Retesting & Attestation", "Once your team patches the issues, we conduct a full retest and issue a verified VAPT Security Certificate for your enterprise clients and investors.")
        ], "COMPLIANCE: ISO 27001 | SOC 2 | GDPR | RBI CYBERSECURITY COMPLIANT"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Don't Wait for a Breach to Test Your Defenses", [
            ("Mobile App VAPT (iOS & Android)", "Static binary decompilation analysis, dynamic hooking with Frida, local SQLite storage encryption, and certificate pinning verification."),
            ("Web & Cloud Infrastructure VAPT", "REST/GraphQL API testing, AWS/GCP cloud IAM configuration reviews, and SaaS multi-tenant isolation audits."),
            ("Book a Confidential Scoping Call", "Secure your application before hostile actors find your vulnerabilities.")
        ], "CYPHER MATRIX TECHNOLOGIES | OFFENSIVE CYBERSECURITY")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d18, 2):
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
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'VAPT' to scope your security ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CRIMSON if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 18 generated.")

# ==============================================================================
# DAY 19: THE TRUE COST OF CHEAP OFFSHORE CODE (5 Slides, 1080x1350)
# ==============================================================================
def build_day19():
    folder = 'Day_19_Cost_of_Cheap_Code'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(255, 51, 102, 35), glow_pos=(850, 450, 450))
    add_header(img, draw, category="B2B FOUNDER ADVISORY", slide_str="01 / 05", accent=CRIMSON)
    draw_pill_badge(draw, 60, 145, "THE $25/HR DEVELOPER TRAP", get_font(FONT_MENLO, 19), accent_color=CRIMSON)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "THE TRUE FINANCIAL COST\nOF CHEAP OFFSHORE CODE", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "Why low upfront hourly rates secretly cost startup founders 4x more in technical debt, security breaches, and complete code rewrites.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Financial Comparison Card
    draw_glass_card(img, 60, 450, 960, 580, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.text((95, 480), "YEAR 1 COST BREAKDOWN: CHEAP DEV VS ENGINEERING STUDIO", font=font_mono, fill=CYAN)
    
    # Left column: The "Cheap" Option
    draw.rounded_rectangle([90, 520, 520, 880], radius=14, fill=(24, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 545), "THE $25/HR FREELANCER", font=get_font(FONT_AVENIR, 20, index=2), fill=CRIMSON)
    draw.text((115, 580), "Initial Estimate: $12,000", font=font_mono, fill=CRIMSON)
    costs_cheap = [
        ("Months 1-3: Delayed Deliveries", "+$6,000"),
        ("Month 4: Spaghetti Code Bugfixes", "+$8,500"),
        ("Month 6: Security Vulnerability Leak", "+$25,000"),
        ("Month 8: Complete System Crash", "+$15,000"),
        ("Month 10: Complete Code Rewrite", "+$35,000")
    ]
    for idx, (lbl, cost) in enumerate(costs_cheap):
        draw.text((115, 625 + idx * 45), lbl, font=get_font(FONT_HELVETICA, 16), fill=(255, 180, 190, 255))
        draw.text((430, 625 + idx * 45), cost, font=font_mono, fill=CRIMSON)
    draw.line([(115, 840), (490, 840)], fill=(255, 51, 102, 100), width=1)
    draw.text((115, 850), "ACTUAL YEAR 1 COST: $101,500", font=get_font(FONT_AVENIR, 18, index=2), fill=CRIMSON)
    
    # Right column: The Cypher Matrix Engineering Option
    draw.rounded_rectangle([550, 520, 980, 880], radius=14, fill=(10, 24, 18, 255), outline=(0, 255, 136, 120))
    draw.text((575, 545), "CYPHER MATRIX STUDIO", font=get_font(FONT_AVENIR, 20, index=2), fill=EMERALD)
    draw.text((575, 580), "Initial Scope: $38,000", font=font_mono, fill=EMERALD)
    costs_cm = [
        ("Months 1-3: On-Time Sprint Milestones", "$0 Delay"),
        ("Month 4: Scalable Clean Architecture", "$0 Tech Debt"),
        ("Month 6: In-House Offensive VAPT", "$0 Breach Risk"),
        ("Month 8: Automated CI/CD & Tests", "$0 Regressions"),
        ("Month 10: Seamless Scale & Growth", "$0 Rebuilds")
    ]
    for idx, (lbl, cost) in enumerate(costs_cm):
        draw.text((575, 625 + idx * 45), lbl, font=get_font(FONT_HELVETICA, 16), fill=(180, 255, 210, 255))
        draw.text((880, 625 + idx * 45), cost, font=font_mono, fill=EMERALD)
    draw.line([(575, 840), (950, 840)], fill=(0, 255, 136, 100), width=1)
    draw.text((575, 850), "ACTUAL YEAR 1 COST: $38,000", font=get_font(FONT_AVENIR, 18, index=2), fill=EMERALD)
    
    # Bottom key summary card
    draw_glass_card(img, 60, 1060, 960, 180, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((95, 1090), "THE LESSON EVERY EXPERIENCED CTO KNOWS:", font=get_font(FONT_AVENIR, 22, index=2), fill=CYAN)
    draw_safe_text(draw, 95, 1130, "If you think hiring professional software engineers is expensive, wait until you see how much hiring an amateur costs you.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect hidden costs ->", handle="@cyphermatrixpvtltd", accent=CRIMSON)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d19 = [
        ("02 / 05", "HIDDEN SINKHOLE #1", "Architectural Fragility & Zero Documentation", [
            ("No Separation of Concerns", "Cheap code dumps business logic directly inside UI view controllers. Changing a simple button or API endpoint breaks 14 unrelated database flows."),
            ("Zero Automated Tests or CI/CD", "When you want to release feature #10, features #1 through #9 mysteriously stop working. Manual regression testing takes weeks."),
            ("Zero Architectural Documentation", "When the cheap developer disappears, no new engineer can understand the codebase—forcing you to throw away months of work.")
        ], "SYMPTOM: 80% OF DEVELOPER HOURS SPENT ON REGRESSION BUGS"),
        
        ("03 / 05", "HIDDEN SINKHOLE #2", "Disastrous Security Vulnerabilities", [
            ("Hardcoded API Keys in Client Builds", "Amateur developers leave Stripe private keys, AWS root credentials, and database passwords committed directly inside public or decompileable mobile APKs."),
            ("Zero Input Validation or Escaping", "Exposing your users to SQL injection, Cross-Site Scripting (XSS), and insecure direct object reference (IDOR) flaws that leak sensitive customer data."),
            ("Non-Compliant Data Storage", "Unencrypted SQLite databases on user devices violating GDPR, HIPAA, and RBI financial compliance laws.")
        ], "SECURITY RISK: AVERAGE DATA BREACH COSTS SMBs OVER $150,000"),
        
        ("04 / 05", "THE CYPHER MATRIX STANDARD", "Engineering That Scales From Day One", [
            ("Clean Architecture & Domain Separation", "Decoupled domain models, repositories, and state managers (Bloc/Riverpod/NestJS) engineered for seamless feature additions."),
            ("Built-In Offensive Security Audits", "Every line of code is reviewed by our in-house cybersecurity team to eliminate OWASP Top 10 vulnerabilities before release."),
            ("Comprehensive Test Automation", "Automated unit, integration, and UI end-to-end test suites executing on every Git pull request.")
        ], "ENGINEERING LAW: PREDICTABLE DELIVERY | ZERO COMPROMISE"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Build Your Product the Right Way First", [
            ("Fixed-Scope Production Milestones", "Transparent sprint planning, daily asynchronous updates, and clear deliverables without surprise billing hours."),
            ("Intellectual Property & Source Code Ownership", "You own 100% of your source code, repositories, infrastructure credentials, and documentation from day one."),
            ("Schedule an Architecture Audit", "Have an existing codebase or planning a new digital product? Let our senior team review your technical blueprint.")
        ], "CYPHER MATRIX TECHNOLOGIES | SECURE. BUILD. SCALE.")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d19, 2):
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
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'SCALE' to build the right way ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=CRIMSON if s_idx < 5 else EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 19 generated.")

# ==============================================================================
# DAY 20: CYBERSECURITY MYTHBUSTERS QUIZ (4 Stories, 1080x1920)
# ==============================================================================
def build_day20():
    folder = 'Day_20_Cybersecurity_Mythbusters_Quiz'
    d_dir = folder
    
    def add_story_hdr(im, dr, tag, s_num):
        if os.path.exists(LOGO_PATH):
            logo = Image.open(LOGO_PATH).convert('RGBA')
            logo.thumbnail((200, 70), Image.Resampling.LANCZOS)
            im.alpha_composite(logo, (60, 80))
        draw_pill_badge(dr, 290, 88, tag, get_font(FONT_MENLO, 20), accent_color=CRIMSON)
        bbox = dr.textbbox((0, 0), s_num, font=get_font(FONT_MENLO, 22))
        dr.text((w_reel - 60 - (bbox[2] - bbox[0]), 92), s_num, font=get_font(FONT_MENLO, 22), fill=TEXT_MUTED)

    # Story 1: Myth 1 Poll
    img, draw = create_base_canvas(w_reel, h_reel, glow_color=(255, 51, 102, 35), glow_pos=(540, 850, 500))
    add_story_hdr(img, draw, "SECURITY MYTHBUSTERS", "01 / 04")
    draw_safe_text(draw, 60, 230, "MYTH #1: 'WE HAVE HTTPS, SO OUR APP IS FULLY SECURE'", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img, 60, 420, 960, 420, radius=24, bg=(24, 16, 22, 245), border=(255, 51, 102, 140))
    draw_safe_text(draw, 100, 470, "Many founders believe that an SSL/TLS certificate solves application security. What do you think?", get_font(FONT_AVENIR, 36, index=2), WHITE, max_width=880, line_spacing=12)
    draw.text((100, 740), "[ VOTE IN THE POLL BELOW ]", font=get_font(FONT_MENLO, 22), fill=CYAN)
    
    draw_glass_card(img, 120, 920, 840, 360, radius=28, bg=(14, 18, 26, 255), border=(255, 51, 102, 160), border_width=3)
    draw.text((w_reel // 2, 980), "PLACE INSTAGRAM POLL STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw.rounded_rectangle([180, 1030, 900, 1110], radius=16, fill=(24, 34, 48, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1070), "TRUE (HTTPS ENCRYPTS EVERYTHING)", font=get_font(FONT_AVENIR, 24, index=2), fill=TEXT_MUTED, anchor='mm')
    draw.rounded_rectangle([180, 1140, 900, 1220], radius=16, fill=(34, 20, 26, 255), outline=CARD_BORDER)
    draw.text((w_reel // 2, 1180), "FALSE (IT ONLY PROTECTS DATA IN TRANSIT)", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD, anchor='mm')
    
    draw.text((w_reel // 2, 1500), "Tap next to see why HTTPS is only 15% of security ->", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    save_image_both(img, d_dir, 'Story_01_Myth_HTTPS.jpg')
    
    # Story 2: Myth 1 Reality Breakdown
    img2, draw2 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img2, draw2, "THE REALITY CHECK", "02 / 04")
    draw_safe_text(draw2, 60, 230, "THE VERDICT: COMPLETELY FALSE", get_font(FONT_AVENIR, 50, index=2), CRIMSON, max_width=960)
    
    draw_glass_card(img2, 60, 360, 960, 480, radius=24, bg=(16, 22, 32, 245), border=CARD_BORDER)
    draw.text((100, 400), "WHAT HTTPS ACTUALLY DOES:", font=get_font(FONT_AVENIR, 26, index=2), fill=EMERALD)
    draw_safe_text(draw2, 100, 450, "HTTPS creates an encrypted tunnel between the client and server. It prevents WiFi eavesdroppers at coffee shops from intercepting network packets.", get_font(FONT_HELVETICA, 25), WHITE, max_width=880, line_spacing=8)
    
    draw.text((100, 600), "WHAT HTTPS CANNOT PROTECT:", font=get_font(FONT_AVENIR, 26, index=2), fill=CRIMSON)
    flaws = [
        "❌ Broken Object-Level Authorization (BOLA/IDOR)",
        "❌ SQL Injection or NoSQL injection",
        "❌ Client-side mobile APK decompilation & reverse-engineering",
        "❌ Stolen API bearer tokens or session hijacking"
    ]
    curr_y = 650
    for f in flaws:
        curr_y = draw_safe_text(draw2, 100, curr_y, f, get_font(FONT_HELVETICA, 23), fill=(255, 180, 190, 255), max_width=880) + 12
        
    draw_glass_card(img2, 60, 890, 960, 560, radius=24, bg=(14, 18, 26, 250), border=(0, 255, 136, 140))
    draw.text((100, 930), "MYTH #2: 'AUTOMATED SCANNERS CATCH 95% OF BUGS'", font=get_font(FONT_AVENIR, 26, index=2), fill=CYAN)
    draw_safe_text(draw2, 100, 985, "Commercial vulnerability scanners only detect known syntax patterns and CVEs. They cannot understand your business workflow.", get_font(FONT_HELVETICA, 25), WHITE, max_width=880, line_spacing=8)
    draw_safe_text(draw2, 100, 1140, "A scanner has no idea that changing `quantity = -5` in a checkout request shouldn't refund $500 to a user's wallet. That requires human offensive security expertise.", get_font(FONT_HELVETICA, 25), WHITE, max_width=880, line_spacing=8)
    
    draw2.text((w_reel // 2, 1600), "Tap next to see what true application security requires ->", font=get_font(FONT_HELVETICA, 26), fill=CYAN, anchor='mm')
    save_image_both(img2, d_dir, 'Story_02_Reality_Check.jpg')
    
    # Story 3: True Security Stack
    img3, draw3 = create_base_canvas(w_reel, h_reel, glow_color=(0, 240, 255, 35), glow_pos=(540, 800, 500))
    add_story_hdr(img3, draw3, "APPLICATION HARDENING", "03 / 04")
    draw_safe_text(draw3, 60, 230, "THE 3 LAYERS OF REAL DEFENSE", get_font(FONT_AVENIR, 46, index=2), WHITE, max_width=960)
    
    layers = [
        ("01. TRANSPORT SECURITY (BASELINE)", CYAN, "TLS 1.3 + Strict Certificate Pinning (SPKI) so even proxies with installed root certs cannot decrypt your traffic."),
        ("02. AUTHORIZATION & OBJECT DEFENSE", EMERALD, "Strict database-level policy checks on every single request ensuring the authenticated user owns the resource."),
        ("03. OFFENSIVE PENETRATION AUDITS", CRIMSON, "Human security researchers systematically attempting to bypass your business rules, privilege escalations, and payment logic.")
    ]
    for idx, (title, col, desc) in enumerate(layers):
        cy = 380 + idx * 365
        draw_glass_card(img3, 60, cy, 960, 330, radius=20, bg=(16, 22, 32, 245), border=CARD_BORDER)
        draw_pill_badge(draw3, 95, cy + 22, title, get_font(FONT_MENLO, 19), accent_color=col)
        draw_safe_text(draw3, 95, cy + 85, desc, get_font(FONT_HELVETICA, 25), WHITE, max_width=870, line_spacing=6)
        
    draw3.text((w_reel // 2, 1580), "Tap next to get a confidential security assessment ->", font=get_font(FONT_HELVETICA, 26), fill=EMERALD, anchor='mm')
    save_image_both(img3, d_dir, 'Story_03_True_Defense.jpg')
    
    # Story 4: Q&A Box
    img4, draw4 = create_base_canvas(w_reel, h_reel, glow_color=(0, 255, 136, 40), glow_pos=(540, 900, 500))
    add_story_hdr(img4, draw4, "SECURITY AUDIT", "04 / 04")
    draw_safe_text(draw4, 60, 230, "IS YOUR APP AT RISK?\nASK OUR SECURITY TEAM", get_font(FONT_AVENIR, 48, index=2), WHITE, max_width=960, line_spacing=12)
    
    draw_glass_card(img4, 100, 460, 880, 520, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw4.text((w_reel // 2, 530), "PLACE INSTAGRAM 'QUESTIONS' STICKER HERE", font=get_font(FONT_MENLO, 22), fill=CYAN, anchor='mm')
    draw4.text((w_reel // 2, 600), "Ask any question about mobile appsec, VAPT, or cloud leaks 👇", font=get_font(FONT_AVENIR, 28, index=2), fill=WHITE, anchor='mm')
    draw4.rounded_rectangle([160, 680, 920, 840], radius=18, fill=(24, 32, 46, 255), outline=CARD_BORDER)
    draw4.text((w_reel // 2, 760), "Type your security question...", font=get_font(FONT_HELVETICA, 28), fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img4, 60, 1040, 960, 360, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw4.text((100, 1085), "CYPHER MATRIX CYBERSECURITY SERVICES:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    points = [
        "✓ Mobile Application Penetration Testing (iOS & Android)",
        "✓ Web Application & REST/GraphQL API VAPT",
        "✓ Cloud Infrastructure & IAM Misconfiguration Audits"
    ]
    curr_y = 1145
    for p in points:
        curr_y = draw_safe_text(draw4, 100, curr_y, p, get_font(FONT_HELVETICA, 24), WHITE, max_width=880) + 16
        
    draw4.text((w_reel // 2, 1580), "CYPHER MATRIX  |  cyphermatrix.io", font=get_font(FONT_MENLO, 22), fill=TEXT_MUTED, anchor='mm')
    save_image_both(img4, d_dir, 'Story_04_QA_Box.jpg')
    print("Day 20 generated.")

# ==============================================================================
# DAY 21: MOBILE APP CERTIFICATE PINNING WITH CODE (5 Slides, 1080x1350)
# ==============================================================================
def build_day21():
    folder = 'Day_21_Certificate_Pinning_Code'
    
    # Slide 1: Cover
    img, draw = create_base_canvas(w_port, h_port, glow_color=(0, 255, 136, 35), glow_pos=(850, 400, 450))
    add_header(img, draw, category="MOBILE SECURITY MASTERCLASS", slide_str="01 / 05", accent=EMERALD)
    draw_pill_badge(draw, 60, 145, "STOPPING MAN-IN-THE-MIDDLE ATTACKS", get_font(FONT_MENLO, 19), accent_color=EMERALD)
    
    font_hero = get_font(FONT_AVENIR, 44, index=2)
    font_body = get_font(FONT_HELVETICA, 22)
    font_mono = get_font(FONT_MENLO, 18)
    
    draw_safe_text(draw, 60, 210, "MOBILE APP CERTIFICATE PINNING:\nTHE DEFINITIVE IMPLEMENTATION GUIDE", font_hero, WHITE, max_width=960, line_spacing=10)
    draw_safe_text(draw, 60, 345, "How attackers bypass default mobile HTTPS encryption in 30 seconds using Burp Suite, and how to harden Flutter, iOS, and Android with SHA-256 SPKI pinning.", font_body, TEXT_MUTED, max_width=960, line_spacing=6)
    
    # Visual Terminal
    draw_glass_card(img, 60, 450, 960, 600, radius=20, bg=(14, 18, 26, 250), border=CARD_BORDER)
    draw.ellipse([80, 470, 92, 482], fill=(255, 95, 86, 255))
    draw.ellipse([100, 470, 112, 482], fill=(255, 189, 46, 255))
    draw.ellipse([120, 470, 132, 482], fill=(39, 201, 63, 255))
    draw.text((150, 468), "MITM ATTACK ANATOMY: TRUST STORE POISONING VS PINNING", font=font_mono, fill=TEXT_MUTED)
    
    # Left Box: Standard HTTPS
    draw.rounded_rectangle([90, 510, 520, 870], radius=14, fill=(24, 14, 18, 255), outline=(255, 51, 102, 120))
    draw.text((115, 535), "STANDARD HTTPS (VULNERABLE)", font=get_font(FONT_AVENIR, 19, index=2), fill=CRIMSON)
    steps_mitm = [
        "1. Attacker installs custom CA on device",
        "2. Device trusts all certs signed by attacker",
        "3. Burp Suite proxy intercepts mobile traffic",
        "4. TLS handshake succeeds with rogue cert",
        "5. Full API payloads decrypted in plaintext",
        "6. Session tokens & user data exfiltrated"
    ]
    for idx, s in enumerate(steps_mitm):
        draw_safe_text(draw, 115, 580 + idx * 46, s, font=get_font(FONT_HELVETICA, 17), fill=(255, 180, 190, 255), max_width=380, line_spacing=2)
    draw.text((115, 880), "Status: 100% Compromised by Proxy", font=font_mono, fill=CRIMSON)
    
    # Right Box: Hardened with Certificate Pinning
    draw.rounded_rectangle([550, 510, 980, 870], radius=14, fill=(10, 24, 18, 255), outline=(0, 255, 136, 120))
    draw.text((575, 535), "CERTIFICATE PINNED (HARDENED)", font=get_font(FONT_AVENIR, 19, index=2), fill=EMERALD)
    steps_pin = [
        "1. App embeds server public key hash (SPKI)",
        "2. Handshake inspects remote cert chain",
        "3. Rogue proxy cert hash does NOT match pin",
        "4. TLS handshake severed immediately (abort)",
        "5. Zero network packets sent to proxy",
        "6. Security event logged to telemetry"
    ]
    for idx, s in enumerate(steps_pin):
        draw_safe_text(draw, 575, 580 + idx * 46, s, font=get_font(FONT_HELVETICA, 17), fill=(180, 255, 210, 255), max_width=380, line_spacing=2)
    draw.text((575, 880), "Status: Handshake Rejected (Safe)", font=font_mono, fill=EMERALD)
    
    # Bottom key takeaway
    draw_glass_card(img, 60, 1080, 960, 150, radius=18, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw_safe_text(draw, 95, 1110, "Without SSL pinning, any user on a rooted/jailbroken phone or corporate network can inspect your app's secret headers, payment tokens, and internal endpoints.", font_body, WHITE, max_width=890, line_spacing=6)
    
    add_footer(draw, w_port, h_port, cta_text="Swipe to inspect Dart / Flutter code ->", handle="@cyphermatrixpvtltd", accent=EMERALD)
    save_image_both(img, folder, 'Slide_01_Cover.jpg')
    
    # Slides 2-5:
    slides_d21 = [
        ("02 / 05", "CERTIFICATE VS PUBLIC KEY PINNING", "Why SubjectPublicKeyInfo (SPKI) Pinning is Superior", [
            ("The Full Certificate Pinning Trap", "If you pin the leaf X.509 certificate, your mobile app will permanently break when your SSL certificate auto-renews after 90 days (Let's Encrypt)—forcing an emergency app store release."),
            ("SubjectPublicKeyInfo (SPKI) Pinning", "Pinning the public key hash inside the certificate allows you to renew the SSL certificate using the same private/public key pair without updating client code."),
            ("Always Include a Backup Pin", "Production rule: Always hardcode at least one backup pin (e.g., intermediate CA key or secondary backup key) to ensure zero downtime in disaster recovery.")
        ], "BEST PRACTICE: PIN SHA-256 SPKI HASHES WITH BACKUP KEYS"),
        
        ("03 / 05", "PRODUCTION IMPLEMENTATION", "Hardening HttpOverrides in Flutter & Dart", [
            ("Native SecurityContext Loading", "Dart's `SecurityContext` allows supplying trusted certificates directly, bypassing the Android/iOS OS TrustManager."),
            ("Custom BadCertificateCallback Validation", "Intercept the server certificate during `SecurityContext` establishment, compute the SHA-256 fingerprint, and compare against your cryptographic pin."),
            ("Anti-Tamper Integrity Checks", "Verify your pinning logic cannot be easily patched out by binary byte modification or runtime Frida hooking scripts.")
        ], "FRAMEWORK: DART DART:IO HTTPCLIENT & DIO PINNING INTERCEPTOR"),
        
        ("04 / 05", "DEFENDING AGAINST DYNAMIC HOOKING", "Protecting Certificate Pinning Against Frida Scripts", [
            ("The Frida Bypass Threat", "On rooted Android or jailbroken iOS devices, reverse engineers use tools like Frida or Objection to hook SSL verification functions and return `true` unconditionally."),
            ("Runtime Jailbreak & Root Detection", "Inspect device filesystem for `su` binaries, test-keys builds, Cydia substrates, and Frida server daemon sockets (`27042`)."),
            ("Native C++ Core Implementation", "Compile critical cryptographic pinning routines into native C/C++ libraries via Dart FFI—making dynamic function hooking exponentially harder.")
        ], "DEFENSE: DART FFI NATIVE INTEGRATION + ANTI-TAMPER TELEMETRY"),
        
        ("05 / 05", "SECURE. BUILD. SCALE.", "Is Your Mobile Application Truly Protected?", [
            ("Mobile Security Architecture", "At Cypher Matrix, offensive security is not an afterthought—it's built directly into every Flutter, Android, and iOS application we deliver."),
            ("Comprehensive Mobile VAPT", "We test your binaries against Frida hooking, binary decompilation, local data leaks, and API privilege escalation before release."),
            ("Consult with Our Senior Engineers", "Ensure your fintech, healthcare, or enterprise application meets global banking security standards.")
        ], "CYPHER MATRIX TECHNOLOGIES | SECURE. BUILD. SCALE.")
    ]
    
    for s_idx, (s_num, s_badge, s_title, cards, footer_txt) in enumerate(slides_d21, 2):
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
        
        cta = "Swipe to continue ->" if s_idx < 5 else "DM 'SECURITY' to harden your mobile app ->"
        add_footer(s_draw, w_port, h_port, cta_text=cta, handle="@cyphermatrixpvtltd", accent=EMERALD)
        save_image_both(s_img, folder, f'Slide_{s_idx:02d}.jpg')
        
    print("Day 21 generated.")

if __name__ == '__main__':
    build_day15()
    build_day16()
    build_day17()
    build_day18()
    build_day19()
    build_day20()
    build_day21()
    print("Week 03 completely generated successfully!")
