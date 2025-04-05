import typer
from utils import check_api_key

app = typer.Typer()

@app.command()
def shellmate():
    api_key_valid, client = check_api_key()
    if api_key_valid:
        print("🤖 Welcome to ShellMate!")
        print("ShellMate > Type your command in natural language, and I will convert it to a shell command.")
        print("💡 Tip: Type 'exit()' to quit the application.")
        
        ask_user(client)

def ask_user(client):
    while True:
        user_input = input("ShellMate > ")
        if user_input.lower() == "exit()":
            print("👋 Goodbye!")
            break



if __name__ == "__main__":
    app()