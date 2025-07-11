import os
import requests
import subprocess
from datetime import datetime

REPO_PATH = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(REPO_PATH, "data")

URLS = {
    "google_doc": "https://docs.google.com/document/d/1YG2bbiTAWMzcpoAEsRCA0JhLeeG3yJdlMgbfKum2Yg0/export?format=txt"
}

def download_files():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    for name, url in URLS.items():
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(DOWNLOAD_DIR, f"{name}.txt")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"[OK] Downloaded and saved: {file_path}")
        else:
            print(f"[ERROR] Failed to download {name} - {response.status_code}")

def commit_and_push():
    os.chdir(REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    
    # check if there is anything to commit
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip() == "":
        print("[GIT] No changes to commit.")
        return
    
    msg = f"Auto commit on {datetime.now().strftime('%Y-%m-%d')}"
    subprocess.run(["git", "commit", "-m", msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print("[DONE] Changes pushed to GitHub")


def main():
    download_files()
    commit_and_push()

if __name__ == "__main__":
    main()
