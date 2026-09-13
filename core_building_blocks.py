import os
import warnings
from pathlib import Path
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

# Suppress unnecessary deprecation and library warnings
warnings.filterwarnings("ignore")

# Find .env relative to this file
script_dir = Path(__file__).resolve().parent
env_path = script_dir / ".env"

load_dotenv(dotenv_path=env_path)

# Verify that the Gemini API key is loaded
print("GEMINI_API_KEY found:", bool(os.getenv("GEMINI_API_KEY")))

# ---------------------------------------------------------
# 1. MODELS - The Reasoning Engine
# ---------------------------------------------------------
# Universal model initialization pointing to Google Gemini
model = init_chat_model("google_genai:gemini-2.5-flash")

# Test query
response = model.invoke("What is LangChain in one sentence?")
print("\n=== Model Response ===")
print(response.content)
print()

# ---------------------------------------------------------
# 2. PROMPT TEMPLATES - Steering the Model
# ---------------------------------------------------------
