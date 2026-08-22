with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace owner number in index.html JS
if '919309419028' in html:
    html = html.replace('919309419028', '919890640303')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with owner WhatsApp number +91 98906 40303!')
