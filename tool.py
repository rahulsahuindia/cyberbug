import requests
import re
from urllib.parse import urljoin

target = input("Target URL: ")

visited = set()
js_files = set()
endpoints = set()

def crawl(url):
    if url in visited:
        return
    
    visited.add(url)
    print("[URL]", url)

    try:
        r = requests.get(url, timeout=5)
    except:
        return

    # JS extract
    matches = re.findall(r'src=["\'](.*?\.js)["\']', r.text)
    for m in matches:
        full = urljoin(url, m)
        js_files.add(full)

    # Endpoint extract
    api = re.findall(r'"/api/.*?"', r.text)
    for a in api:
        endpoints.add(a)

crawl(target)

print("\nJS FILES:")
for j in js_files:
    print(j)

print("\nENDPOINT HINTS:")
for e in endpoints:
    print(e)
