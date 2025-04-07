import os
import json

RUNTIME_CONFIG_DIR = os.path.expanduser("~/shellmate")
RUNTIME_CONFIG_PATH = os.path.join(RUNTIME_CONFIG_DIR, "runtime_config.json")


DEFAULT_RUNTIME_CONFIG = {
    "AUTO_EXECUTE": False,
}

def is_first_run():
    if not os.path.exists(RUNTIME_CONFIG_DIR):
        os.makedirs(RUNTIME_CONFIG_DIR)
        print(f"📁 Created config folder: {RUNTIME_CONFIG_DIR}")

    if not os.path.exists(RUNTIME_CONFIG_PATH):
        with open(RUNTIME_CONFIG_PATH, "w") as f:
            json.dump(DEFAULT_RUNTIME_CONFIG, f)
        print(f"📝 Created config file: {RUNTIME_CONFIG_PATH}")
        return True
    else:
        print(f"✅Config file exists on path: {RUNTIME_CONFIG_PATH}\n")
        return False

def get_auto_execute():
    if not os.path.exists(RUNTIME_CONFIG_PATH):
        is_first_run()
    with open(RUNTIME_CONFIG_PATH,"r") as f:
        return json.load(f).get("AUTO_EXECUTE",False)
    
def toggle_auto_execute():
    with open(RUNTIME_CONFIG_PATH,"r+") as f:
        current_config = json.load(f)
        current_config["AUTO_EXECUTE"] = not current_config.get("AUTO_EXECUTE",False)
        f.seek(0)
        f.truncate()
        json.dump(current_config, f)