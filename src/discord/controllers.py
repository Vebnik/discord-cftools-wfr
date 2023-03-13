from disnake import MessageInteraction

from settings import CF_CONFIG
from src.cftools.cftools_api import CfToolsApi
from src.discord.controllers_logic import (
  board,
)


class ButtonInteractionHandler:

  api = CfToolsApi(CF_CONFIG)

  @classmethod
  async def bind(cls, interaction: MessageInteraction) -> None:

    try:
      id = interaction.component.custom_id.split('|')[0]
      server = interaction.component.custom_id.split('|')[1]
    except: ...

    match id:
      case 'upd_board_btn': 
        await board.update_board(interaction, server, cls.api)

      case 'del_board_btn':
        await board.delete_board(interaction) 
          

