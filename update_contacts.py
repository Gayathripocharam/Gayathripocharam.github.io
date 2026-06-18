import os
import glob
import re

for file in glob.glob('**/*.html', recursive=True):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace links
    content = content.replace('Contact_page.html', 'https://wa.me/918639430057')
    content = content.replace('CTA_page.html', 'https://wa.me/918639430057')
    content = content.replace('Contact_Page.html', 'https://wa.me/918639430057')
    content = content.replace('CTA_Page.html', 'https://wa.me/918639430057')
    
    # Replace phone numbers
    content = content.replace('98487 23235', '86394 30057')
    content = content.replace('9848723235', '8639430057')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated contacts in all html files!')
