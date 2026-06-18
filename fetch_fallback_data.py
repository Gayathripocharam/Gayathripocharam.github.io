import os
import json
import urllib.request

USERNAME = "Gayathripocharam"
DATA_DIR = "data"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(f"{DATA_DIR}/trees", exist_ok=True)
os.makedirs(f"{DATA_DIR}/readmes", exist_ok=True)

def fetch_json(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f)
            return data
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def fetch_text(url, filename):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read().decode()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(data)
            return data
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

print("Fetching repos...")
repos = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated&type=owner", f"{DATA_DIR}/fallback_repos.json")

print("Fetching events...")
fetch_json(f"https://api.github.com/users/{USERNAME}/events?per_page=15", f"{DATA_DIR}/fallback_events.json")

if repos:
    for repo in repos:
        name = repo['name']
        print(f"Fetching data for {name}...")
        # Fetch tree
        fetch_json(f"https://api.github.com/repos/{USERNAME}/{name}/git/trees/main?recursive=1", f"{DATA_DIR}/trees/{name}.json")
        # Fetch readme
        readme_data = fetch_json(f"https://api.github.com/repos/{USERNAME}/{name}/readme", f"{DATA_DIR}/readmes/{name}.json")
        if readme_data and 'download_url' in readme_data and readme_data['download_url']:
            fetch_text(readme_data['download_url'], f"{DATA_DIR}/readmes/{name}.md")

print("Fallback data fetched successfully.")
