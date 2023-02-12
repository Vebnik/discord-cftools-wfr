from tortoise import Tortoise, run_async
from src.database.models import models
from dotenv import load_dotenv; load_dotenv()
import os


async def init():
  await Tortoise.init(
    db_url=os.getenv('DB_URL'),
    modules={'models': ['models']}
  )

  await Tortoise.generate_schemas()


def migrate():
  run_async(init())