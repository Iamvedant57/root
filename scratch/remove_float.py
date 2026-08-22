with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

float_html = '<a class="whatsapp-float trigger-apt-modal" href="#" aria-label="Book Appointment"><i class="fa-regular fa-calendar-check"></i></a>'

if float_html in html:
    html = html.replace(float_html, '')
    print('Removed floating icon button HTML element!')

html = html.replace(', .whatsapp-float', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully removed floating icon button from index.html!')
