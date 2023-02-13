from discord import Client, Interaction

from src.discord.views import LeaderboardView
from src.discord.embdes import LeaderboardEmbed

class InteractionCommandHandler:
  client: Client

  def __init__(self, client) -> None:
    self.client = client
    self.bind()

  def bind(self):

    @self.client.tree.command()
    async def grants(interaction: Interaction) -> None:
      await interaction.response.send_message(f'No have grant')

    @self.client.tree.command()
    async def test(interaction: Interaction) -> None:
      embed = LeaderboardEmbed({'title': 'Hello'})
      await interaction.response.send_message(
        content='Test', view=LeaderboardView(), embed=embed.get_embed())


class ButtonInteractionHandler:
  def __init__(self, client, interaction) -> None:
    self.client = client
    self.bind(interaction)

  def bind(self, interaction: Interaction) -> None:
    print(interaction)


class TextCommandHandler:
  def __init__(self) -> None:
    pass

