import os

from pathlib import Path

from dotenv import load_dotenv

# Load environment variables

PROJECT_ROOT = Path(__file__).parent

#en_path = os.path.join(PROJECT_ROOT, ".env") #load_dotenv(en_path) this works , better to use os.path.join

load_dotenv(PROJECT_ROOT / ".env")
# API Configuration

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# LLM Settings

DEFAULT_MODEL = "gemini-2.5-flash"

MAX_RETRIES = 3

RETRY_DELAY = 2
 
# Processing Settings

DEFAULT_BATCH_SIZE = 10

SPECSENSE_BATCH_SIZE = 5