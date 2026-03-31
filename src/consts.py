from dotenv import load_dotenv
import os

load_dotenv()

gemini_model_name = "gemini-2.0-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CLIENT_TYPE = "mock"
RETRIES_COUNT = 3
