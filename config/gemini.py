from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


print("Loaded key:", os.getenv("GEMINI_API_KEY")[:10])

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)