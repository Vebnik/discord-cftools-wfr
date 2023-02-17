from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction, Option, OptionType, Permissions

from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import CfConfig
from src.discord.embdes import GrantsEmbed
from src.discord.views import LeaderboardComponents
from settings import CF_CONFIG

class CmdConfig:
  options = [
    Option(
      name='update',
      description='Update grants ?',
      type=OptionType.boolean,
      required=False
    )
  ]


class GrantsCommand(Cog):

  bot: InteractionBot
  api: CfToolsApi

  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot
    self.api = CfToolsApi(CF_CONFIG)

  @slash_command(
    name='grants',
    description='Get active server grant',
    options=CmdConfig.options,
    default_member_permissions=Permissions(administrator=True)
  )
  async def grants(self, interaction: ApplicationCommandInteraction, update=False) -> None:
    grants = await self.api.get_grants(update=update)
    embed = GrantsEmbed.get_embed(grants)
    components = LeaderboardComponents.get_components()

    await interaction.response.send_message(embed=embed, ephemeral=True, components=components)


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(GrantsCommand(bot))