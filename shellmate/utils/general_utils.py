import config.static_config as static_config
import os

def intro_text():
    print("🤖 Welcome to ShellMate!")
    print("ShellMate > Type your command in natural language, and I will convert it to a shell command.")
    print("💡 Tip: Type 'exit()' to quit the application.\n")


def clear_terminal():
    if static_config.OS_NAME == "windows":
        os.system("cls")
    else:
        os.system("clear")
