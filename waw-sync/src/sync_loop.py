import time
import requests
import json
from pathlib import Path

STATE = Path.home() / ".waw/state.json"
BACKEND_URL = "http://localhost:8000/profile"

def load_last_sync():
    if STATE.exists():
        return json.loads(STATE.read_text())["last_synced_at"]
    return 0

def save_last_sync(ts):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"last_synced_at": ts}))


def sync_loop():
    print("[sync] starting loop")
    last_ts = load_last_sync()
    while True:
        # TODO: read identity.db timestamp
        ts = last_ts + 1  # placeholder
        if ts > last_ts:
            print(f"[sync] posting delta ts={ts}")
            try:
                requests.post(BACKEND_URL, json={"id": "demo", "updated_at": ts})
                last_ts = ts
                save_last_sync(ts)

                # Add logic here to:
                # 1. Fetch data from the source (e.g., identity service)
                # 2. Fetch data from the destination (e.g., backend mock)
                # 3. Compare and sync data
            except requests.ConnectionError:
                print("[sync] backend offline, will retry")
        time.sleep(60)


if __name__ == "__main__":
    sync_loop() 