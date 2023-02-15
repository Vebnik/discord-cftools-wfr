import logging, os
from tortoise import Tortoise, run_async
from src.cftools.models import AuthToken
from dotenv import load_dotenv; load_dotenv()

class Connector:
  
  async def init_db(self) -> None:
    logging.info('Init db')
    await Tortoise.init(
      db_url=os.getenv('DB_URL'),
      modules={'models': ['src.cftools.models', 'src.discord.models']}
    )

  async def close(self) -> None:
    await Tortoise.close_connections()