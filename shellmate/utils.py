from openai import OpenAI
import config

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