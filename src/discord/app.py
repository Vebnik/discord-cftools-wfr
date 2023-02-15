import disnake, logging, datetime, os
from disnake.ext import commands

from src.cftools.cftools_api import CfToolsApi
from src.discord.interface import DisConfig


class App:

  config: DisConfig
  bot: commands.InteractionBot

  def __init__(self, config: DisConfig) -> None:
    try:
      self.config = config
      
      if os.getenv('MODE') == 'dev':
        self.bot = commands.InteractionBot(reload=True)
      elif os.getenv('MODE') == 'prod':
        self.bot = commands.InteractionBot(reload=False)

      # main event
      @self.bot.event
      async def on_ready():
        logging.info(f'App started at: {datetime.datetime.now()}')

      # extension
      self.bot.load_extensions(os.path.join(os.getcwd(), 'src', 'discord', 'cogs', 'slash_command'))

      # start main loop
      self.bot.run(config.token)

    except Exception as ex:
      logging.critical(ex)