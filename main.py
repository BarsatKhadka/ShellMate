import typer
import os
from openai import OpenAI

app = typer.Typer()

@app.command()
def shellmate():
    if check_api_key():
        print("Type your command in natural language and I will convert it to a shell command.")
        print("Type exit() to quit.")




def check_api_key():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ OPENAI_API_KEY is not set.")
        print("👉 Set it in your environment as shown in the README.")
        return False

    client = OpenAI(api_key=api_key)
    try:
        client.models.list()
        print("✅  API key is valid.")
        print("🤖 Welcome to shellmate!")
        return True
    except Exception as e:
        if(e.code == 'invalid_api_key'):
            print("❌ Invalid API key.")
            print("👉 Check your API key and try again.")
        else:
            print("❌ An error occurred while validating the API key.")
            print(f"Error details. {e}")
        return False
    
    
    

if __name__ == "__main__":
    app()