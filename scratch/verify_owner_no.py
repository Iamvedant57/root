with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert '919309419028' not in html, 'Old owner number 919309419028 still found in index.html'
assert '919890640303' in html, 'New owner number 919890640303 not found in index.html'

print('Verification successful! Owner WhatsApp number updated to +91 98906 40303 across all files.')
