import os
import json

RUNTIME_CONFIG_DIR = os.path.expanduser("~/shellmate")
RUNTIME_CONFIG_PATH = os.path.join(RUNTIME_CONFIG_DIR, "runtime_config.json")


DEFAULT_RUNTIME_CONFIG = {
    "AUTO_EXECUTE": False,
}


def no_config_dir_exists():
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
    