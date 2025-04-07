import os
import platform

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SHELL_PATH = os.getenv("SHELL")
OS_NAME = platform.system().lower()
SHELL_NAME = os.path.basename(SHELL_PATH) if SHELL_PATH else OS_NAME

# Default model 
DEFAULT_OPENAI_MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = (
    "You are an assistant that converts natural language into safe and accurate shell commands. "
    "Respond with only the command, without explanation. " 
    f"OS NAME: {OS_NAME}. "
    f"SHELL NAME: {SHELL_NAME}. "
    "Current working directory: {cwd}"
    "IMPORTANT: If the command uses 'alias', 'export', 'source', or 'function', you MUST respond like this:\n"
    "REQUIRES_REAL_SHELL: <the full command>\n"
    "This format is required for compatibility with the user's environment."
)

OPENAI_TEMPERATURE = 0
DEBUG_MODE = False

