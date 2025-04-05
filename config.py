import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default model 
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = (
    "You are an assistant that converts natural language into safe and accurate shell commands. "
    "Respond with only the command, without explanation."
)

OPENAI_TEMPERATURE = 0
DEBUG_MODE = False
