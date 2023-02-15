import os, logging

from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction, Option, OptionType

from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import CfConfig


class CmdConfig:
  options = [
    Option(
      name='channel', 
      description='Where spawn leaderboard', 
      required=True,
      type=OptionType.channel
    ),
    Option(
      name='server', 
      description='Target server to get statistic', 
      required=True,
      choices=['server 1', 'server 2', 'server 3']
    ),
  ]
  cf_config = CfConfig(
		api_url=os.getenv('CF_TOOLS_ROOT_API'),
		secret=os.getenv('CF_TOOLS_SECRET'),
		app_id=os.getenv('CF_TOOLS_APPID')
	)


class LeaderboardCommand(Cog):

  bot: InteractionBot
  api: CfToolsApi

  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot
    self.api = CfToolsApi(CmdConfig.cf_config)

  @slash_command(
    name='leaderboard',
    description='Spawn Leaderboard in select channels',
    options=CmdConfig.options
  )
  
  async def leaderboard(self, interaction: ApplicationCommandInteraction, channel, server) -> None:
    print(channel, server)
    try:
      grants = await self.api.get_grants()
      servers_id = [item.resource.id for item in grants.tokens.server]
      leaderboard = [await self.api.get_leaderboard(id) for id in servers_id]

      for board in leaderboard:
        print(board)

      await interaction.response.send_message(leaderboard, ephemeral=True)
    except Exception as ex:
      logging.critical(ex)
      await interaction.response.send_message('Some error | Check logs', ephemeral=True)


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(LeaderboardCommand(bot))