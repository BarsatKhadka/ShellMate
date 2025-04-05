import typer
import os

app = typer.Typer()

@app.command()
def shellmate():
    if check_api_key():
        print("Shellmate is running...")



def check_api_key():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Set the OPENAI_API_KEY in your environment variable.")
        print("Instructions provided in the README.")
        return False

    return True   
    
    

if __name__ == "__main__":
    app()