import typer , config.static_config as static_config , os

##Custom functions in utils.py
from utils.general_utils import clear_terminal, intro_text
from utils.openai_utils import check_api_key, generate_shell_command
from config.runtime_config import no_config_dir_exists

app = typer.Typer()

@app.command()
def shellmate():
    api_key_valid, client = check_api_key()

    if api_key_valid:
        if no_config_dir_exists(): intro_text()
        ask_user(client)

def ask_user(client):
    while True:
        print(f"ShellMate @{static_config.SHELL_NAME} > ", end="")
        user_input = input(f"{os.getcwd()}$ ")

        if user_input.lower() == "exit()":
            print("👋 Goodbye!")
            break
        elif user_input.lower() == "clear":
            clear_terminal()
        else:
            command, updated_cwd = generate_shell_command(client, user_input)
            if command:
                print(f"ShellMate @{static_config.SHELL_NAME} > {updated_cwd}$ {command}")
            else:
                print("❌ Failed to generate shell command.")

if __name__ == "__main__":
    app()