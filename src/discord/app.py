import discord, logging
from discord import Client, Intents, app_commands, Interaction

from src.cftools.cftools_api import CfToolsApi
from src.discord.controllers import InteractionCommandHandler, ButtonInteractionHandler


class AppConfig:
  intents_def = Intents.default()
  intents_all = Intents.all()


class App(Client):

  cf_api: CfToolsApi

  def __init__(self, *, intents: Intents, cf_api, **options) -> None:
    super().__init__(intents=intents, **options)
    self.cf_api = cf_api
    self.tree = app_commands.CommandTree(self)

  async def on_ready(self) -> None:
    await self.cf_api.db_connector.init_db()
    await self.add_event_handlers()

    logging.critical(f'Init db | Start app - {self.user}')

  async def on_interaction(self, interaction: Interaction) -> None:
    ButtonInteractionHandler(client=self, interaction=interaction)

  async def add_event_handlers(self) -> None:
    InteractionCommandHandler(client=self)