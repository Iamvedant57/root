with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert '<a class="whatsapp-float' not in html, 'Floating icon element still present!'
print('Verification successful! Floating icon button removed completely.')
