import disnake, logging, datetime, os, asyncio
from disnake.ext import commands

from src.database.connector import Connector
from src.discord.interface import DisConfig


class App:

  config: DisConfig

  bot: commands.InteractionBot
  db: Connector

  def __init__(self, config: DisConfig) -> None:
    try:
      self.config = config
      self.db = Connector()

      if os.getenv('MODE') == 'dev':
        self.bot = commands.InteractionBot(reload=True)
      elif os.getenv('MODE') == 'prod':
        self.bot = commands.InteractionBot(reload=False)

      self.bot.loop.create_task(self.db.init_db())

      @self.bot.event
      async def on_ready():
        logging.info(f'App started at: {datetime.datetime.now()}')

      self.bot.load_extensions(os.path.join(os.getcwd(), 'src', 'discord', 'cogs', 'slash_command'))
      self.bot.run(config.token)

    except Exception as ex:
      logging.critical(ex)