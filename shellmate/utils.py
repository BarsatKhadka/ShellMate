from openai import OpenAI
import config
import os

def check_api_key():
    api_key = config.OPENAI_API_KEY

    if not api_key:
        print("❌ OPENAI_API_KEY is not set.")
        print("👉 Set it in your environment as shown in the README.")
        return False , None

    print("🔑 Validating API key...")
    client = OpenAI(api_key=api_key)
    try:
        client.models.list()
        print("✅  API key is valid.")
        return True , client
    except Exception as e:
        if(e.code == 'invalid_api_key'):
            print("❌ Invalid API key.")
            print("👉 Check your API key and try again.")
        else:
            print("❌ An error occurred while validating the API key.")
            print(f"Error details. {e}")
        return False , None
    
def generate_shell_command(client,user_input):
    try:
        cwd = os.getcwd()
        system_prompt = config.SYSTEM_PROMPT.format(cwd=cwd)
        
        response = client.chat.completions.create(
            model=config.DEFAULT_OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=config.OPENAI_TEMPERATURE
        )
        command = response.choices[0].message.content.strip()
        return command , cwd
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None
    
def clear_terminal():
    if config.OS_NAME == "windows":
        os.system("cls")
    else:
        os.system("clear")


