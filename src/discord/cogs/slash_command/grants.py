import os

from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction, Option, OptionType

from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import CfConfig

from src.discord.embdes import GrantsEmbed

class CmdConfig:
  options = [
    Option(
      name='update',
      description='Update grants ?',
      type=OptionType.boolean,
      required=False
    )
  ]
  
  cf_config = CfConfig(
		api_url=os.getenv('CF_TOOLS_ROOT_API'),
		secret=os.getenv('CF_TOOLS_SECRET'),
		app_id=os.getenv('CF_TOOLS_APPID')
	)


class GrantsCommand(Cog):

  bot: InteractionBot
  api: CfToolsApi

  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot
    self.api = CfToolsApi(CmdConfig.cf_config)

  @slash_command(
    name='grants',
    description='Get active server grant',
    options=CmdConfig.options
  )
  async def grants(self, interaction: ApplicationCommandInteraction, update=False) -> None:
    grants = await self.api.get_grants(update=update)
    embed = GrantsEmbed.get_embed(grants)

    await interaction.response.send_message(embed=embed, ephemeral=False)


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(GrantsCommand(bot))