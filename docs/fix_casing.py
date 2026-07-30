import os
import glob
import re

DOCS_DIR = r"E:\LifeXOS-Docs\docs"

def fix_title(title):
    # Fix casing for specific known words
    fixes = {
        'Api': 'API',
        'Faq': 'FAQ',
        'Orbit Ai': 'Orbit AI',
        'Ui': 'UI',
        'Db': 'DB'
    }
    for k, v in fixes.items():
        title = title.replace(k, v)
    return title

def fix_index():
    idx_path = os.path.join(DOCS_DIR, 'index.md')
    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for bad, good in [('Api', 'API'), ('Faq', 'FAQ'), ('Orbit Ai', 'Orbit AI')]:
        content = re.sub(r'\[(.*?)' + bad + r'(.*?)\]', r'[\1' + good + r'\2]', content)
        
    with open(idx_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_index()
print("Fixed index.md casing")
