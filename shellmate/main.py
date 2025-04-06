import typer
import config
import os

##Custom functions in utils.py
from utils import check_api_key
from utils import generate_shell_command
from utils import clear_terminal
from utils import intro_text

app = typer.Typer()

@app.command()
def shellmate():
    api_key_valid, client = check_api_key()

    if api_key_valid:
        intro_text()
        ask_user(client)

def ask_user(client):
    while True:
        print(f"ShellMate @{config.SHELL_NAME} > ", end="")
        user_input = input(f"{os.getcwd()}$ ")

        if user_input.lower() == "exit()":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "clear":
            clear_terminal()
        else:
            command, updated_cwd = generate_shell_command(client, user_input)
            if command:
                print(f"ShellMate @{config.SHELL_NAME} > {updated_cwd}$ {command}")
            else:
                print("❌ Failed to generate shell command.")


        

if __name__ == "__main__":
    app()