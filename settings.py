from dotenv import load_dotenv; load_dotenv()
import os

COMMAND_PERMISSIONS = (
    '324889109355298829',
)

STATS_CHANNEL_ID = (
    ('test', '780745208622219294'),
)

SERVERS = (
    ('WFR_DM', 'd634e3f0-76de-42f0-9dab-cafe4bfab920'),
)

BOARD_STATS = [
    "kills",
    "deaths",
    "suicides",
    "playtime",
    "longest_kill",
    "longest_shot",
    "kdratio"
]

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