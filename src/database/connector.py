import logging, os
from tortoise import Tortoise, run_async
from src.database.models import AuthToken
from dotenv import load_dotenv; load_dotenv()

class Connector:
  
  async def init_db(self) -> None:
    await Tortoise.init(
      db_url=os.getenv('DB_URL'),
      modules={'models': ['src.database.models']}
    )
