import requests
from urllib.parse import urlparse
import os

# Ensure the output directory exists
output_dir = "responses"
os.makedirs(output_dir, exist_ok=True)

# Read domains from file
with open("subs.txt", "r") as file:
    domains = [line.strip() for line in file if line.strip()]

def check_domain(domain):
    urls = [f"http://{domain}", f"https://{domain}"]
    for url in urls:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            return response.status_code, url
        except requests.RequestException:
            continue
    return None, None

for domain in domains:
    status_code, url = check_domain(domain)
    if status_code:
        print(f"[{status_code}] {url}")
        with open(os.path.join(output_dir, f"{status_code}.txt"), "a") as f:
            f.write(f"{url}\n")
    else:
        print(f"[Dead] {domain}")
        with open(os.path.join(output_dir, "dead.txt"), "a") as f:
            f.write(f"{domain}\n")
