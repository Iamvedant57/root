import re, os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
local_imgs = [i for i in imgs if not i.startswith('http') and not i.startswith('data:')]

print("Local image references in index.html:")
for img in set(local_imgs):
    exists = os.path.exists(img)
    print(f" - {img} (Exists: {exists})")
