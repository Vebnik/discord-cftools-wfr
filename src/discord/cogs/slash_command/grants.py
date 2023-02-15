from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction


class CmdConfig:
  options = []


class GrantsCommand(Cog):

  bot: InteractionBot

  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot

  @slash_command(
    name='grants',
    description='Get active server grant',
  )
  async def grants(self, interaction: ApplicationCommandInteraction) -> None:
    await interaction.response.send_message('Nice commands', ephemeral=True)


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(GrantsCommand(bot))