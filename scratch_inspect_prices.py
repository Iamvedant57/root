import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

price_rows = re.findall(r'<div class="price-row">.*?</div>\s*</div>', html, re.DOTALL)
print(f'Found {len(price_rows)} price rows in index.html:')
for r in price_rows:
    name_match = re.search(r'<div class="name">(.*?)<small>', r, re.DOTALL)
    amount_match = re.search(r'<div class="amount">(.*?)</div>', r, re.DOTALL)
    if name_match and amount_match:
        name = name_match.group(1).strip()
        amount = amount_match.group(1).strip()
        print(f"  * {name} -> {amount}".encode('ascii', 'ignore').decode('ascii'))
