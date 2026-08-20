with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace 'Chat on WhatsApp' action buttons with 'Book Appointment'
old_hero_btn = '<a href="https://wa.me/919890640303" target="_blank" rel="noopener" class="btn"><i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp</a>'
new_hero_btn = '<a href="#" class="btn trigger-apt-modal"><i class="fa-regular fa-calendar-check"></i> Book Appointment</a>'

count = html.count(old_hero_btn)
print(f'Found {count} instances of Chat on WhatsApp buttons')

if old_hero_btn in html:
    html = html.replace(old_hero_btn, new_hero_btn)

# Make floating action button trigger appointment modal
old_float = '<a class="whatsapp-float" href="https://wa.me/919890640303" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>'
new_float = '<a class="whatsapp-float trigger-apt-modal" href="#" aria-label="Book Appointment"><i class="fa-regular fa-calendar-check"></i></a>'

if old_float in html:
    html = html.replace(old_float, new_float)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully converted all Chat on WhatsApp buttons into Book Appointment buttons!')
