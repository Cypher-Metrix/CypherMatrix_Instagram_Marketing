import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# Paths
BASE_DIR = '/Users/cyphermatrix/.gemini/antigravity/scratch/CypherMatrix_Instagram_Marketing'
ASSETS_DIR = os.path.join(BASE_DIR, '08_Brand_Assets')
LOGO_PATH = os.path.join(ASSETS_DIR, 'Logo', 'cypher_matrix_logo.png')
BILL_MITRA_LOGO_PATH = os.path.join(ASSETS_DIR, 'Logo', 'bill_mitra_logo.png')
REF_DIR = os.path.join(ASSETS_DIR, 'Reference_Images')
WEEK1_DIR = os.path.join(BASE_DIR, '04_Post_Creatives', 'Week_01')

# Brand Colors
BG_DARK = (8, 10, 15, 255)         # #080A0F
CARD_BG = (18, 24, 34, 235)        # #121822 with alpha
CARD_BORDER = (38, 50, 70, 255)    # #263246
EMERALD = (0, 255, 136, 255)       # #00FF88
CRIMSON = (255, 51, 102, 255)      # #FF3366
CYAN = (0, 240, 255, 255)          # #00F0FF
WHITE = (248, 250, 252, 255)       # #F8FAFC
TEXT_MUTED = (148, 163, 184, 255)  # #94A3B8
SLATE_LINE = (26, 35, 50, 255)

# Fonts
FONT_HELVETICA = '/System/Library/Fonts/HelveticaNeue.ttc'
FONT_AVENIR = '/System/Library/Fonts/Avenir Next.ttc'
FONT_MENLO = '/System/Library/Fonts/Menlo.ttc'

def get_font(path, size, index=0):
    try:
        return ImageFont.truetype(path, size, index=index)
    except:
        return ImageFont.load_default()

def create_base_canvas(w, h, grid_step=60, glow_color=None, glow_pos=None):
    img = Image.new('RGBA', (w, h), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # Grid lines
    for x in range(0, w, grid_step):
        draw.line([(x, 0), (x, h)], fill=(15, 20, 28, 255), width=1)
    for y in range(0, h, grid_step):
        draw.line([(0, y), (w, y)], fill=(15, 20, 28, 255), width=1)
        
    # Ambient Glow if requested
    if glow_color and glow_pos:
        glow_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        gx, gy, gr = glow_pos
        g_draw.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=glow_color)
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(gr // 2))
        img = Image.alpha_composite(img, glow_layer)
        draw = ImageDraw.Draw(img)
        
    return img, draw

def draw_glass_card(img, x, y, w, h, radius=20, bg=CARD_BG, border=CARD_BORDER, border_width=2):
    card = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(card)
    c_draw.rounded_rectangle([0, 0, w, h], radius=radius, fill=bg, outline=border, width=border_width)
    img.alpha_composite(card, (x, y))

def draw_pill_badge(draw, x, y, text, font, accent_color=EMERALD):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 16, 8
    w, h = tw + pad_x * 2, th + pad_y * 2
    
    r, g, b = accent_color[:3]
    bg = (r, g, b, 35)
    border = (r, g, b, 180)
    
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h//2, fill=bg, outline=border, width=1)
    draw.text((x + pad_x, y + pad_y - 2), text, font=font, fill=(r, g, b, 255))
    return x + w + 12

def wrap_text(text, font, max_width, draw):
    """
    Robust word-wrapping that guarantees no line exceeds max_width.
    Handles embedded newlines and long strings safely.
    """
    paragraphs = text.split('\n')
    all_lines = []
    
    for para in paragraphs:
        if not para:
            all_lines.append("")
            continue
        words = para.split(' ')
        curr = []
        for w in words:
            test_line = ' '.join(curr + [w]) if curr else w
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if (bbox[2] - bbox[0]) <= max_width:
                curr.append(w)
            else:
                if curr:
                    all_lines.append(' '.join(curr))
                curr = [w]
        if curr:
            all_lines.append(' '.join(curr))
            
    return all_lines

def draw_safe_text(draw, x, y, text, font, fill, max_width, line_spacing=8):
    """
    Renders text with strict bounds checking. Returns final y coordinate.
    Guarantees no word extends beyond x + max_width.
    """
    lines = wrap_text(text, font, max_width, draw)
    curr_y = y
    for line in lines:
        if line == "":
            curr_y += line_spacing * 2
            continue
        draw.text((x, curr_y), line, font=font, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=font)
        curr_y += (bbox[3] - bbox[1]) + line_spacing
    return curr_y

def add_header(img, draw, category="CYBERSECURITY MASTERCLASS", slide_str="01 / 07", accent=EMERALD):
    w, h = img.size
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert('RGBA')
        logo.thumbnail((160, 60), Image.Resampling.LANCZOS)
        img.alpha_composite(logo, (50, 45))
        
    font_badge = get_font(FONT_MENLO, 18)
    font_slide = get_font(FONT_MENLO, 20)
    
    draw_pill_badge(draw, 230, 48, category, font_badge, accent_color=accent)
    
    bbox = draw.textbbox((0, 0), slide_str, font=font_slide)
    tw = bbox[2] - bbox[0]
    draw.text((w - 50 - tw, 54), slide_str, font=font_slide, fill=TEXT_MUTED)
    draw.line([(50, 115), (w - 50, 115)], fill=SLATE_LINE, width=1)

def add_footer(draw, w, h, cta_text="Swipe to inspect vulnerabilities ->", handle="@cyphermatrixpvtltd", accent=EMERALD):
    font_mono = get_font(FONT_MENLO, 19)
    font_bold = get_font(FONT_AVENIR, 20, index=2)
    
    draw.line([(50, h - 85), (w - 50, h - 85)], fill=SLATE_LINE, width=1)
    draw.text((50, h - 60), f"CYPHER MATRIX  |  {handle}", font=font_mono, fill=TEXT_MUTED)
    
    bbox = draw.textbbox((0, 0), cta_text, font=font_bold)
    tw = bbox[2] - bbox[0]
    draw.text((w - 50 - tw, h - 62), cta_text, font=font_bold, fill=accent)

print("Updated generate_week01_assets framework with strict bounding.")
