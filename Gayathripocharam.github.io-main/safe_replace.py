import os
import glob

files_to_check = glob.glob('**/*.html', recursive=True) + glob.glob('**/*.js', recursive=True) + glob.glob('**/*.md', recursive=True)

for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    dirty = False
    
    if 'RishvinReddy' in content:
        content = content.replace('RishvinReddy', 'Gayathripocharam')
        dirty = True
        
    if 'GayathriReddy' in content:
        content = content.replace('GayathriReddy', 'Gayathripocharam')
        dirty = True
        
    if 'Rishvin' in content:
        content = content.replace('Rishvin', 'Gayathri')
        dirty = True

    if 'pe_cache_v3' in content or 'pe_cache_v4' in content:
        content = content.replace('pe_cache_v3', 'pe_cache_v6').replace('pe_cache_v4', 'pe_cache_v6')
        dirty = True
        
    if dirty:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

print("Done.")
