import typer
from utils import check_api_key
import config

app = typer.Typer()

@app.command()
def shellmate():
    api_key_valid, client = check_api_key()
    if api_key_valid:
        print("🤖 Welcome to ShellMate!")
        print("ShellMate > Type your command in natural language, and I will convert it to a shell command.")
        print("💡 Tip: Type 'exit()' to quit the application.")
        
        SHELL_NAME = config.SHELL_NAME
        ask_user(client, SHELL_NAME)

def ask_user(client, SHELL_NAME):
    while True:
        user_input = input(f"ShellMate ({SHELL_NAME}) > ")
        if user_input.lower() == "exit()":
            print("👋 Goodbye!")
            break
        else:
            command = generate_shell_command(client, user_input)
            if command:
                print(f"ShellMate ({SHELL_NAME}) > {command}")
            else:
                print("❌ Failed to generate shell command.")

def generate_shell_command(client,user_input):
    try:
        response = client.chat.completions.create(
            model=config.DEFAULT_OPENAI_MODEL,
            messages=[
                {"role": "system", "content": config.SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=config.OPENAI_TEMPERATURE
        )
        command = response.choices[0].message.content.strip()
        return command
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None
        

if __name__ == "__main__":
    app()