import typer
import os

app = typer.Typer()

@app.command()
def shellmate():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Set the OPENAI_API_KEY in your environment variable.")
        print("Instructions provided in the README.")
    
    

if __name__ == "__main__":
    app()