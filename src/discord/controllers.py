from disnake import MessageInteraction
from disnake.ext.commands import InteractionBot


class ButtonInteractionHandler:

  @staticmethod
  async def bind(interaction: MessageInteraction) -> None:
    match interaction.component.custom_id:
      case 'upd_board_btn': 
        print(interaction.component.custom_id)
      case 'del_board_btn': 
        await interaction.message.delete()

