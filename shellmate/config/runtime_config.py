import os

RUNTIME_CONFIG_DIR = os.path.expanduser("~/shellmate")
RUNTIME_CONFIG_PATH = os.path.join(RUNTIME_CONFIG_DIR, "runtime_config.json")


def no_config_dir_exists():
    if not os.path.exists(RUNTIME_CONFIG_DIR):
        os.makedirs(RUNTIME_CONFIG_DIR)
        print(f"Config files created on folder: {RUNTIME_CONFIG_DIR}\n")
        return True
    else:
        print(f"Config files exists on folder: {RUNTIME_CONFIG_DIR}\n")
        return False