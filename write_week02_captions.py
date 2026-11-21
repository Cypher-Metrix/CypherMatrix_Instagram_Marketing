import os, re

calendar_file = '/Users/cyphermatrix/scratch/CypherMatrix_Instagram_Marketing/03_Content_Calendar/Captions_and_Hashtags.md'
with open(calendar_file, 'r', encoding='utf-8') as f:
    full_text = f.read()

days_map = {
    'DAY 09': ('Day_09_Tractor_Hisab_Agritech', 'Product Promotions (15%)', 'Reel Video (1080x1920) + Telemetry Card', 'Rural Tractor Owners, Agri-Contractors, Farm Fleet Managers'),
    'DAY 10': ('Day_10_CaseStudy_VeggieKing_Retail', 'Portfolio & Case Studies (15%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'E-Commerce Founders, Supply Chain Directors, Retail CTOs'),
    'DAY 11': ('Day_11_Mobile_Reverse_Engineering', 'Cybersecurity Education (30%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'Fintech CTOs, Mobile Security Leads, App Founders'),
    'DAY 12': ('Day_12_Odoo_Flutter_Library', 'Company Branding & Authority (10%)', 'Single-Image Engineering Showcase (1080x1350)', 'Open Source Engineers, Enterprise Flutter Developers, Tech Leads'),
    'DAY 13': ('Day_13_Flutter_vs_Native_Debate', 'Engagement & Community (5%)', 'Instagram Stories Series (4 Slides, 1080x1920)', 'Mobile Founders, Startup Engineers, Product Managers'),
    'DAY 14': ('Day_14_Cloud_Breach_S3_IAM', 'Cybersecurity Education (30%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'DevOps Engineers, Cloud Architects, SaaS Founders, CTOs')
}

sections = re.split(r'## DAY (\d+):', full_text)
for i in range(1, len(sections), 2):
    day_num = int(sections[i])
    day_key = f'DAY {day_num:02d}'
    if day_key in days_map:
        folder_name, pillar, fmt, audience = days_map[day_key]
        content = sections[i+1].strip()
        
        lines = content.split('\n')
        title_line = lines[0].strip().lstrip('#').strip()
        
        date_m = re.search(r'\*\*Publishing Date:\*\*\s*(.*)', content)
        time_m = re.search(r'\*\*Publishing Time:\*\*\s*(.*)', content)
        date_str = date_m.group(1).strip() if date_m else 'Week 02'
        time_str = time_m.group(1).strip() if time_m else '19:30 IST'
        
        caption_m = re.search(r'\*\*Complete Caption:\*\*\s*```text\n(.*?)```', content, re.DOTALL)
        caption_text = caption_m.group(1).strip() if caption_m else ''
        
        hashtags_m = re.search(r'\*\*Targeted Hashtags:\*\*\s*```text\n(.*?)```', content, re.DOTALL)
        hashtags_text = hashtags_m.group(1).strip() if hashtags_m else ''
        
        out_content = f'''# {day_key}: {title_line}

- **Publishing Date:** {date_str}
- **Scheduled Time:** {time_str}
- **Content Pillar:** {pillar}
- **Format:** {fmt}
- **Target Audience:** {audience}

---

## COMPLETE CAPTION
```text
{caption_text}
```

---

## TARGETED HASHTAGS
```text
{hashtags_text}
```
'''
        for base in ['/Users/cyphermatrix/scratch/CypherMatrix_Instagram_Marketing', '/Users/cyphermatrix/.gemini/antigravity/scratch/CypherMatrix_Instagram_Marketing']:
            target_dir = os.path.join(base, '04_Post_Creatives', 'Week_02', folder_name)
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, 'Post_Brief_and_Caption.md'), 'w', encoding='utf-8') as out_f:
                out_f.write(out_content)
        print(f'Wrote {day_key} brief to {folder_name}')
