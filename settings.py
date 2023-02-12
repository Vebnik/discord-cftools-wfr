from dotenv import load_dotenv; load_dotenv()
import os


TORTOISE_ORM = {
    "connections": {"default": os.getenv('DB_URL')},
    "apps": {
        "models": {
            "models": ["src.database.models", "src.discord.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}