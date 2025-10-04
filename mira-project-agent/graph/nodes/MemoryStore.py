import json
from datetime import datetime
import os

class MemoryStore:
    def __init__(self, storage_path="memory_logs.json"):
        self.storage_path = storage_path
        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w") as f:
                json.dump([], f)

    def __call__(self, state):
        summary = state.get("status_summary", "")
        timestamp = datetime.utcnow().isoformat()

        log_entry = {
            "timestamp": timestamp,
            "summary": summary
        }

        # Append to memory log
        with open(self.storage_path, "r+") as f:
            logs = json.load(f)
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f, indent=2)

        return {**state, "memory_logged": True}
