import os
import platform

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SHELL_PATH = os.getenv("SHELL")
OS_NAME = platform.system().lower()
SHELL_NAME = os.path.basename(SHELL_PATH) if SHELL_PATH else OS_NAME

# Default model 
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = (
    f"You are an assistant that converts natural language into safe and accurate shell commands. "
    "Respond with only the command, without explanation. " 
    "OS NAME: {OS_NAME}. "
    "SHELL NAME: {SHELL_NAME}. "
    
)

OPENAI_TEMPERATURE = 0
DEBUG_MODE = False
