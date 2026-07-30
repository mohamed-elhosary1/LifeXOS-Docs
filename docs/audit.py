import os
import glob
import re

DOCS_DIR = r"E:\LifeXOS-Docs\docs"
DATE_STR = "2026-07-31"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix terminology
    content = re.sub(r'(?i)ai\s+assistant', 'Orbit AI', content)

    lines = content.split('\n')
    if not lines:
        return

    title_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title_idx = i
            break
            
    if title_idx == -1:
        fname = os.path.basename(filepath)
        title = fname.replace('.md', '').replace('-', ' ').title()
        lines.insert(0, f"# {title}")
        title_idx = 0

    title_text = lines[title_idx].replace('# ', '').strip()

    # Check for existing Purpose and Last Updated
    has_purpose = False
    has_last_updated = False
    purpose_idx = -1
    last_updated_idx = -1
    
    for i, line in enumerate(lines[:15]):
        if line.startswith('**Purpose:**'):
            has_purpose = True
            purpose_idx = i
        if line.startswith('**Last Updated:**'):
            has_last_updated = True
            last_updated_idx = i

    # If no purpose, find the first non-empty line after title that is not a header
    # and turn it into the purpose.
    if not has_purpose:
        for i in range(title_idx + 1, min(title_idx + 10, len(lines))):
            if lines[i].strip() and not lines[i].startswith('#') and not lines[i].startswith('**'):
                lines[i] = f"**Purpose:** {lines[i]}"
                has_purpose = True
                purpose_idx = i
                break

    if not has_purpose:
        # Fallback
        lines.insert(title_idx + 1, f"**Purpose:** Documentation outlining the {title_text.lower()} aspects of LifeXOS.")
        purpose_idx = title_idx + 1
        lines.insert(title_idx + 2, "")

    if not has_last_updated:
        lines.insert(purpose_idx + 1, f"**Last Updated:** {DATE_STR}")
        lines.insert(purpose_idx + 2, "")
    else:
        # Update date if existing
        lines[last_updated_idx] = f"**Last Updated:** {DATE_STR}"

    # Remove existing TOC to recreate it
    toc_idx = -1
    for i, line in enumerate(lines):
        if line.strip() == "## Table of Contents":
            toc_idx = i
            break
            
    if toc_idx != -1:
        end_idx = toc_idx + 1
        while end_idx < len(lines):
            if lines[end_idx].startswith('#') and not lines[end_idx].strip() == "## Table of Contents":
                break
            if lines[end_idx].strip() == '' and end_idx + 1 < len(lines) and lines[end_idx+1].startswith('#'):
                break
            end_idx += 1
        lines = lines[:toc_idx] + lines[end_idx:]

    # Create TOC
    if len(lines) > 30:
        headers = []
        for line in lines:
            if line.startswith('## ') and "Table of Contents" not in line and "Related Documents" not in line:
                headers.append(line.replace('## ', '').strip())
                
        if headers:
            toc = ["## Table of Contents"]
            for h in headers:
                anchor = re.sub(r'[^\w\s-]', '', h.lower()).strip().replace(' ', '-')
                anchor = re.sub(r'-+', '-', anchor)
                toc.append(f"- [{h}](#{anchor})")
            toc.append("")
            
            lu_idx = -1
            for i, line in enumerate(lines):
                if '**Last Updated:**' in line:
                    lu_idx = i
                    break
            
            if lu_idx != -1:
                ins_toc_idx = lu_idx + 1
                while ins_toc_idx < len(lines) and lines[ins_toc_idx].strip() == '':
                    ins_toc_idx += 1
                lines = lines[:ins_toc_idx] + [""] + toc + lines[ins_toc_idx:]

    # Related Documents
    has_related = False
    rel_idx = -1
    for i, line in enumerate(lines):
        if '**Related Documents:**' in line:
            has_related = True
            rel_idx = i
            break
            
    if not has_related:
        related = [
            "",
            "**Related Documents:**",
            "- [Index](index.md)"
        ]
        lines.extend(related)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def generate_index(md_files):
    index_lines = [
        "# LifeXOS Documentation Index",
        "**Purpose:** Central hub linking to all documentation pages.",
        f"**Last Updated:** {DATE_STR}",
        "",
        "## Table of Contents",
        "- [Documentation Index](#documentation-index)",
        "",
        "## Documents",
        ""
    ]
    
    docs = []
    for f in md_files:
        fname = os.path.basename(f)
        if fname == 'index.md':
            continue
        title = fname.replace('.md', '').replace('-', ' ').title()
        docs.append(f"- [{title}]({fname})")
        
    docs.sort()
    index_lines.extend(docs)
    
    index_lines.extend([
        "",
        "**Related Documents:**",
        "- [Index](index.md)"
    ])
    
    with open(os.path.join(DOCS_DIR, 'index.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))

def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, "*.md"))
    for f in md_files:
        if os.path.basename(f) == 'index.md':
            continue
        process_file(f)
    
    generate_index(md_files)
    print(f"Processed {len(md_files)} files and generated index.md.")

if __name__ == '__main__':
    main()
