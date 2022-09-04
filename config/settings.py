import os
from dotenv import load_dotenv

load_dotenv()

# secrets
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DISCORD_TOKEN_ID = "DISCORD_TOKEN"
DISCORD_TOKEN_ID_VER = "1"
