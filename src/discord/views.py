from discord.ui import View, Button, button
from discord import Interaction, Emoji

from src.discord.embdes import LeaderboardEmbed


class LeaderboardView(View):
  def __init__(self, *, timeout = None):
    super().__init__(timeout=timeout)

  @button(label='Update', custom_id='upd_btn_board')
  async def update(self, interaction: Interaction, button: Button) -> None:
    embed = LeaderboardEmbed({'title': 'Hello'})
    await interaction.response.edit_message(view=self, embed=embed.get_embed())
