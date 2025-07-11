import os
import requests
import subprocess
from datetime import datetime

# === CONFIG ===
REPO_PATH = os.path.dirname(os.path.abspath(__file__))
URLS = {
    "app1": "https://example.com/files/app1.json",
    "app2": "https://example.com/files/app2.json"
    # Add more URLs as needed
}
DOWNLOAD_DIR = os.path.join(REPO_PATH, "data")

def download_files():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    for app, url in URLS.items():
        print(f"[DOWNLOAD] Fetching {app} from {url}")
        r = requests.get(url)
        if r.status_code == 200:
            ext = os.path.splitext(url)[1] or ".dat"
            path = os.path.join(DOWNLOAD_DIR, f"{app}{ext}")
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"[OK] Saved to {path}")
        else:
            print(f"[WARN] Failed {app}, status {r.status_code}")

def commit_and_push():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    msg = f"Auto commit on {datetime.now().strftime('%Y-%m-%d')}"
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print("[DONE] Changes pushed to GitHub")

def main():
    download_files()
    commit_and_push()

if __name__ == "__main__":
    main()
