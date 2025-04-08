import config.static_config as static_config
import os
import shutil

def intro_text():
    print("🤖 Welcome to ShellMate!")
    print("ShellMate > Type your command in natural language, and I will convert it to a shell command.")
    print("💡 Tip: Type 'exit()' to quit the application.\n")


def clear_terminal():
    if static_config.OS_NAME == "windows":
        os.system("cls")
    else:
        os.system("clear")

def is_direct_shell_command(user_input):
    command = user_input.strip().split(" ")[0]
    return shutil.which(command) is not None

