import os
from dotenv import load_dotenv

load_dotenv()

# Facebook Credentials
FB_VERIFY = os.getenv("FB_VERIFY") 
FB_SECRET = os.getenv("FB_SECRET") 
FB_TOKEN = os.getenv("FB_TOKEN")

# OpenAI Credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv('EMBEDDING_MODEL')
CHAT_MODEL = os.getenv('CHAT_MODEL')
