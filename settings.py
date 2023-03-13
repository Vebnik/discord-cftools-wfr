from dotenv import load_dotenv; load_dotenv()
from src.cftools.interface import CfConfig
import os

COMMAND_PERMISSIONS = (
    '324889109355298829',
)

SERVERS = (
    ('WFR_3PP', '55a3b79b-f4be-40ec-b602-afb045596214'),
    ('WFR_1PP', '07cf8e39-bbdb-4ce0-b3d3-91e4e8832545'),
    ('WFRLIvonia', '20918114-e69b-466f-aafc-54da95b1be06'),
    ('WFR_Classic_1pp', '92a692d6-facd-488c-8ebd-cfd60d4bf7f4'),
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

CF_CONFIG = CfConfig(
    api_url=os.getenv('CF_TOOLS_ROOT_API'),
    secret=os.getenv('CF_TOOLS_SECRET'),
    app_id=os.getenv('CF_TOOLS_APPID')
)

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

