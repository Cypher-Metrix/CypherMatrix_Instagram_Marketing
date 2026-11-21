import os, re

calendar_file = '/Users/cyphermatrix/scratch/CypherMatrix_Instagram_Marketing/03_Content_Calendar/Captions_and_Hashtags.md'
with open(calendar_file, 'r', encoding='utf-8') as f:
    full_text = f.read()

days_map = {
    'DAY 15': ('Day_15_Voice_AI_Mobile_Apps', 'Software Development & Technology (25%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'Mobile Architects, CTOs, AI Engineers'),
    'DAY 16': ('Day_16_BillMitra_vs_Desktop_Billing', 'Product Promotions (15%)', 'Problem-Solution Carousel (5 Slides, 1080x1080 Square)', 'Retail Owners, Supermarket Managers, Wholesale Distributors'),
    'DAY 17': ('Day_17_CaseStudy_GladAI_Workspace', 'Portfolio & Case Studies (15%)', 'Case Study Carousel (5 Slides, 1080x1350)', 'Enterprise Founders, Operations Heads, Remote Team Leaders'),
    'DAY 18': ('Day_18_Inside_VAPT_Audit', 'Cybersecurity Education (30%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'CTOs, Engineering Directors, Compliance Officers'),
    'DAY 19': ('Day_19_Cost_of_Cheap_Code', 'Company Branding & Authority (10%)', 'B2B Founder Advisory (5 Slides, 1080x1350)', 'Startup Founders, Non-Technical Co-Founders, Angel Investors'),
    'DAY 20': ('Day_20_Cybersecurity_Mythbusters_Quiz', 'Engagement & Community (5%)', 'Interactive Instagram Stories Series (4 Slides, 1080x1920)', 'Founders, Developers, Tech Enthusiasts'),
    'DAY 21': ('Day_21_Certificate_Pinning_Code', 'Cybersecurity Education (30%)', 'Technical Carousel Masterclass (5 Slides, 1080x1350)', 'Lead Mobile Engineers, Security Engineers, FinTech Developers')
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
        date_str = date_m.group(1).strip() if date_m else 'Week 03'
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
            target_dir = os.path.join(base, '04_Post_Creatives', 'Week_03', folder_name)
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, 'Post_Brief_and_Caption.md'), 'w', encoding='utf-8') as out_f:
                out_f.write(out_content)
        print(f'Wrote {day_key} brief to {folder_name}')
