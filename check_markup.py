with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('<select id="aptService"> exists:', '<select id="aptService">' in html)
print('aptServicesTrigger exists:', 'aptServicesTrigger' in html)
