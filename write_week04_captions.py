import os, re

calendar_file = '/Users/cyphermatrix/scratch/CypherMatrix_Instagram_Marketing/03_Content_Calendar/Captions_and_Hashtags.md'
with open(calendar_file, 'r', encoding='utf-8') as f:
    full_text = f.read()

days_map = {
    'DAY 22': ('Day_22_Flutter_StateManagement_Riverpod_Bloc', 'Software Development & Technology (25%)', 'Carousel Masterclass (5 Slides, 1080x1350)', 'Mobile Architects, Senior Flutter Engineers, Tech Leads'),
    'DAY 23': ('Day_23_BillMitra_Inventory_Stock', 'Product Promotions (15%)', 'Problem-Solution Carousel (5 Slides, 1080x1080 Square)', 'Retailers, Wholesalers, Inventory Managers'),
    'DAY 24': ('Day_24_CaseStudy_Patnagar_Organic', 'Portfolio & Case Studies (15%)', 'Case Study Carousel (5 Slides, 1080x1350)', 'Agri-Business Founders, Supply Chain Directors, E-Commerce Founders'),
    'DAY 25': ('Day_25_Modern_SQL_Injection', 'Cybersecurity Education (30%)', 'Cybersecurity Breakdown Carousel (5 Slides, 1080x1350)', 'Backend Engineers, Database Admins, Security Researchers, CTOs'),
    'DAY 26': ('Day_26_Behind_The_Sprints_Hub', 'Company Branding & Authority (10%)', 'Engineering Culture Creative (1080x1350)', 'Potential Clients, Tech Talent, Industry Peers'),
    'DAY 27': ('Day_27_DevSecOps_Quiz', 'Engagement & Community (5%)', 'Interactive Instagram Stories Series (4 Slides, 1080x1920)', 'DevOps Engineers, Developers, Engineering Managers'),
    'DAY 28': ('Day_28_PreLaunch_Security_Checklist', 'Cybersecurity Education (30%)', 'Technical Carousel Masterclass (5 Slides, 1080x1350)', 'CTOs, Startup Founders, Product Managers preparing for launch'),
    'DAY 29': ('Day_29_Microservices_vs_ModularMonolith', 'Software Development & Technology (25%)', 'Architecture Carousel Masterclass (5 Slides, 1080x1350)', 'Tech Co-Founders, Backend Architects, Engineering Leads'),
    'DAY 30': ('Day_30_TractorHisab_Season_Audit', 'Product Promotions (15%)', 'Reel Video (1080x1920) + Telemetry Card', 'Rural Tractor Owners, Agri-Contractors, Farm Fleet Managers')
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
        date_str = date_m.group(1).strip() if date_m else 'Week 04'
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
            target_dir = os.path.join(base, '04_Post_Creatives', 'Week_04', folder_name)
            os.makedirs(target_dir, exist_ok=True)
            with open(os.path.join(target_dir, 'Post_Brief_and_Caption.md'), 'w', encoding='utf-8') as out_f:
                out_f.write(out_content)
        print(f'Wrote {day_key} brief to {folder_name}')
