import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from generate_week01_assets import (
    BASE_DIR, ASSETS_DIR, LOGO_PATH, REF_DIR, WEEK1_DIR,
    BG_DARK, CARD_BG, CARD_BORDER, EMERALD, CRIMSON, CYAN, WHITE, TEXT_MUTED, SLATE_LINE,
    FONT_HELVETICA, FONT_AVENIR, FONT_MENLO,
    get_font, create_base_canvas, draw_glass_card, draw_pill_badge, wrap_text, draw_safe_text
)

DAY6_DIR = os.path.join(WEEK1_DIR, 'Day_06_Founder_Security_Poll')
os.makedirs(DAY6_DIR, exist_ok=True)

def add_story_header(img, draw, story_tag="FOUNDER & CTO AUDIT", story_num="01 / 04"):
    w, h = 1080, 1920
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((200, 70), Image.Resampling.LANCZOS)
        img.alpha_composite(logo, (60, 80))
        
    draw_pill_badge(draw, 290, 88, story_tag, get_font(FONT_MENLO, 20), accent_color=CRIMSON)
    
    font_slide = get_font(FONT_MENLO, 22)
    bbox = draw.textbbox((0, 0), story_num, font=font_slide)
    draw.text((w - 60 - (bbox[2] - bbox[0]), 92), story_num, font=font_slide, fill=TEXT_MUTED)

# Story 1: Poll
def create_story_1():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 35), glow_pos=(540, 850, 500))
    add_story_header(img, draw, "FOUNDER & CTO AUDIT", "01 / 04")
    
    font_title = get_font(FONT_AVENIR, 50, index=2)
    font_body = get_font(FONT_HELVETICA, 28)
    font_mono = get_font(FONT_MENLO, 22)
    
    draw_safe_text(draw, 60, 230, "CRITICAL QUESTION FOR\nEVERY TECH FOUNDER:", font_title, WHITE, max_width=960, line_spacing=12)
    
    # Question Card
    draw_glass_card(img, 60, 420, 960, 420, radius=24, bg=(18, 22, 32, 245), border=(255, 51, 102, 140))
    q_text = "If your user database leaked right now, do you have a documented incident response plan?"
    draw_safe_text(draw, 100, 470, q_text, get_font(FONT_AVENIR, 38, index=2), WHITE, max_width=880, line_spacing=12)
        
    draw.text((100, 740), "[ VOTE IN THE POLL BELOW ]", font=font_mono, fill=CRIMSON)
    
    # Poll Container
    draw_glass_card(img, 120, 920, 840, 360, radius=28, bg=(14, 18, 26, 255), border=(0, 255, 136, 160), border_width=3)
    draw.text((w // 2, 980), "PLACE INSTAGRAM POLL STICKER HERE", font=font_mono, fill=CYAN, anchor='mm')
    
    draw.rounded_rectangle([180, 1030, 900, 1110], radius=16, fill=(24, 34, 48, 255), outline=CARD_BORDER)
    draw.text((w // 2, 1070), "YES, DOCUMENTED & TESTED", font=get_font(FONT_AVENIR, 24, index=2), fill=WHITE, anchor='mm')
    
    draw.rounded_rectangle([180, 1140, 900, 1220], radius=16, fill=(34, 20, 26, 255), outline=CARD_BORDER)
    draw.text((w // 2, 1180), "NO, WE WOULD BE SCRAMBLING", font=get_font(FONT_AVENIR, 24, index=2), fill=TEXT_MUTED, anchor='mm')
    
    draw.text((w // 2, 1500), "Tap next to see what the average data breach costs in 2026 ->", font=font_body, fill=TEXT_MUTED, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY6_DIR, 'Story_01_Poll.jpg'), quality=95)
    print("Re-generated Day 6 Story 1 (Bounds Guaranteed)")

# Story 2: Breach Stats
def create_story_2():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(255, 51, 102, 45), glow_pos=(540, 750, 500))
    add_story_header(img, draw, "INDUSTRY REALITY", "02 / 04")
    
    font_title = get_font(FONT_AVENIR, 48, index=2)
    font_body = get_font(FONT_HELVETICA, 28)
    font_mono = get_font(FONT_MENLO, 22)
    
    draw.text((60, 230), "THE COST OF SLOW CONTAINMENT", font=font_title, fill=WHITE)
    draw.text((60, 305), "Why seconds matter during an active intrusion:", font=font_body, fill=TEXT_MUTED)
    
    draw_glass_card(img, 60, 390, 960, 520, radius=24, bg=(24, 16, 22, 245), border=(255, 51, 102, 160))
    draw.text((w // 2, 480), "$4.45 MILLION", font=get_font(FONT_AVENIR, 72, index=2), fill=CRIMSON, anchor='mm')
    draw.text((w // 2, 570), "Average global cost of an enterprise data breach", font=font_body, fill=WHITE, anchor='mm')
    draw.text((w // 2, 620), "(Source: IBM Cost of a Data Breach Report)", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    
    draw.line([(120, 670), (960, 670)], fill=CARD_BORDER, width=1)
    stat_sub = "80% of financial & reputational damage occurs during the first 60 minutes of slow incident containment."
    draw_safe_text(draw, 100, 715, stat_sub, font_body, WHITE, max_width=880, line_spacing=8)
        
    draw_glass_card(img, 60, 960, 960, 480, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((100, 1005), "THE MOST COMMON STARTUP MISTAKES:", font=get_font(FONT_AVENIR, 26, index=2), fill=CYAN)
    mistakes = [
        "- No one knows who holds master AWS root keys",
        "- Leaked JWT signing secrets cannot be invalidated",
        "- No isolated backup environment exists",
        "- Logs were overwritten, destroying forensic evidence"
    ]
    curr_y = 1065
    for m in mistakes:
        curr_y = draw_safe_text(draw, 100, curr_y, m, font_body, WHITE, max_width=880) + 18
        
    draw.text((w // 2, 1580), "Tap next for the 3 actions every founder must take ->", font=font_body, fill=EMERALD, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY6_DIR, 'Story_02_Breach_Stats.jpg'), quality=95)
    print("Re-generated Day 6 Story 2 (Bounds Guaranteed)")

# Story 3: Containment Steps
def create_story_3():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(0, 255, 136, 40), glow_pos=(540, 800, 500))
    add_story_header(img, draw, "INCIDENT BLUEPRINT", "03 / 04")
    
    font_title = get_font(FONT_AVENIR, 46, index=2)
    font_body = get_font(FONT_HELVETICA, 26)
    font_mono = get_font(FONT_MENLO, 20)
    
    draw.text((60, 230), "THE 60-MINUTE INCIDENT PLAYBOOK", font=font_title, fill=WHITE)
    draw.text((60, 300), "Three emergency actions every CTO must execute immediately:", font=font_body, fill=TEXT_MUTED)
    
    steps = [
        ("01. SEVER CREDENTIALS & ROTATE SECRETS", CRIMSON, [
            "Instantly invalidate master API tokens and database passwords.",
            "Rotate JWT signing secret keys to force logout across all active sessions.",
            "Revoke compromised AWS IAM / Cloud service credentials."
        ]),
        ("02. ISOLATE COMPROMISED MICROSERVICES", CYAN, [
            "Sever traffic routing to the affected API cluster via reverse proxy.",
            "Preserve memory heap dumps and container snapshots before rebooting.",
            "Route incoming traffic to a static maintenance response page."
        ]),
        ("03. PRESERVE IMMUTABLE AUDIT LOGS", EMERALD, [
            "Lock SIEM and database transaction logs to prevent log tampering.",
            "Identify the exact ingress vector (SQLi, IDOR, or credential leak).",
            "Prepare a transparent, legally sound user disclosure statement."
        ])
    ]
    
    for idx, (title, col, bullets) in enumerate(steps):
        cy = 380 + idx * 365
        draw_glass_card(img, 60, cy, 960, 330, radius=20, bg=(16, 22, 32, 245), border=CARD_BORDER)
        draw_pill_badge(draw, 95, cy + 22, title, font_mono, accent_color=col)
        curr_y = cy + 85
        for b in bullets:
            curr_y = draw_safe_text(draw, 95, curr_y, f"[+] {b}", font_body, WHITE, max_width=870, line_spacing=4) + 12
                
    draw.text((w // 2, 1580), "Tap next to ask our security team your AppSec questions ->", font=font_body, fill=EMERALD, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY6_DIR, 'Story_03_Containment_Steps.jpg'), quality=95)
    print("Re-generated Day 6 Story 3 (Bounds Guaranteed)")

# Story 4: Q&A Box
def create_story_4():
    w, h = 1080, 1920
    img, draw = create_base_canvas(w, h, glow_color=(0, 240, 255, 40), glow_pos=(540, 900, 500))
    add_story_header(img, draw, "LIVE Q&A SESSION", "04 / 04")
    
    font_title = get_font(FONT_AVENIR, 48, index=2)
    font_body = get_font(FONT_HELVETICA, 28)
    font_mono = get_font(FONT_MENLO, 22)
    
    draw_safe_text(draw, 60, 230, "ASK OUR OFFENSIVE\nSECURITY ENGINEERS", font_title, WHITE, max_width=960, line_spacing=12)
    draw.text((60, 375), "Have questions about Mobile AppSec, VAPT audits, or Flutter?", font=font_body, fill=TEXT_MUTED)
    
    draw_glass_card(img, 100, 460, 880, 520, radius=28, bg=(14, 18, 26, 255), border=(0, 240, 255, 160), border_width=3)
    draw.text((w // 2, 530), "PLACE INSTAGRAM 'QUESTIONS' STICKER HERE", font=font_mono, fill=CYAN, anchor='mm')
    draw.text((w // 2, 600), "Drop your AppSec or software questions 👇", font=get_font(FONT_AVENIR, 32, index=2), fill=WHITE, anchor='mm')
    
    draw.rounded_rectangle([160, 680, 920, 840], radius=18, fill=(24, 32, 46, 255), outline=CARD_BORDER)
    draw.text((w // 2, 760), "Type your question...", font=font_body, fill=TEXT_MUTED, anchor='mm')
    
    draw_glass_card(img, 60, 1040, 960, 360, radius=20, bg=(16, 22, 32, 240), border=CARD_BORDER)
    draw.text((100, 1085), "WHAT WE COMMONLY ANSWER:", font=get_font(FONT_AVENIR, 24, index=2), fill=EMERALD)
    common = [
        "1. 'How do I protect my mobile app against reverse engineering?'",
        "2. 'What is the cost & timeline for an enterprise VAPT audit?'",
        "3. 'Should I choose Flutter or React Native for my 2027 MVP?'"
    ]
    curr_y = 1145
    for c in common:
        curr_y = draw_safe_text(draw, 100, curr_y, c, font_body, WHITE, max_width=880) + 16
        
    draw.text((w // 2, 1580), "Our senior security team will reply directly to your questions today.", font=font_body, fill=WHITE, anchor='mm')
    draw.text((w // 2, 1640), "CYPHER MATRIX  |  cyphermatrix.io", font=font_mono, fill=TEXT_MUTED, anchor='mm')
    
    img.convert('RGB').save(os.path.join(DAY6_DIR, 'Story_04_QA_Box.jpg'), quality=95)
    print("Re-generated Day 6 Story 4 (Bounds Guaranteed)")

create_story_1()
create_story_2()
create_story_3()
create_story_4()
