from dotenv import load_dotenv; load_dotenv()
import os

STATS_CHANNEL_ID = {
    
}

TORTOISE_ORM = {
    "connections": {"default": os.getenv('DB_URL')},
    "apps": {
        "models": {
            "models": [
                "src.cftools.models", 
                "src.discord.models", 
                "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}