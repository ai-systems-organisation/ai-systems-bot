from dotenv import load_dotenv  # Import dotenv at the top of the file
import os

from app import create_app
from load_azd_env import load_azd_env

# Load environment variables from the .env file
load_dotenv('/workspaces/ai-systems-bot/.azure/ai-systems-chatbot/.env')

# # WEBSITE_HOSTNAME is always set by App Service, RUNNING_IN_PRODUCTION is set in main.bicep
# RUNNING_ON_AZURE = os.getenv("WEBSITE_HOSTNAME") is not None or os.getenv("RUNNING_IN_PRODUCTION") is not None

# if not RUNNING_ON_AZURE:
#     load_azd_env()

app = create_app()

# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8000))
#     app.run(host="0.0.0.0", port=port)