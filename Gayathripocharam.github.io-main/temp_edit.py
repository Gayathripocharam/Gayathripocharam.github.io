import os

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Name Change
content = content.replace(
    'bg-gradient-to-r from-slate-900 via-primary to-indigo-600">Gayathri\n                  Reddy</span>',
    'bg-gradient-to-r from-slate-900 via-primary to-indigo-600">Gayathri</span>'
)

# 2. Hero Bio Change
target_bio = """                Engineering secure, scalable systems. Bridging the gap between
                <span class="font-semibold text-slate-900 border-b-2 border-primary/30 pb-0.5">Data Science
                  hardware</span>,
                <span class="font-semibold text-slate-900 border-b-2 border-indigo-500/30 pb-0.5">Blockchain</span>
                and
                <span class="font-semibold text-slate-900 border-b-2 border-green-500/30 pb-0.5">Modern
                  Web</span>."""

repl_bio = """                Engineering secure, scalable systems. Bridging the gap between
                <span class="font-semibold text-slate-900 border-b-2 border-primary/30 pb-0.5">data science</span>,
                <span class="font-semibold text-slate-900 border-b-2 border-indigo-500/30 pb-0.5">hardware</span>,
                and
                <span class="font-semibold text-slate-900 border-b-2 border-green-500/30 pb-0.5">modern web
                  technologies</span>."""
content = content.replace(target_bio, repl_bio)

# 3. Patent Class Change
target_class = """                  <div class="text-[9px] font-black text-amber-500/70 uppercase tracking-widest">Class</div>
                  <div class="text-base font-black text-slate-800">Data Science</div>"""

repl_class = """                  <div class="text-[9px] font-black text-amber-500/70 uppercase tracking-widest">Class</div>
                  <div class="text-base font-black text-slate-800">data-science System</div>"""
content = content.replace(target_class, repl_class)

# 4. GitHub Links Change
content = content.replace('GayathriReddy', 'Gayathripocharam')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
