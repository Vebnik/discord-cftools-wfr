import os, logging

from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import (
  ApplicationCommandInteraction, Option, OptionType, OptionChoice, TextChannel, Permissions
)

from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import CfConfig, StatsDetail, StatsPlayer

from src.discord.embdes import LeaderboardEmbed

from settings import SERVERS, BOARD_STATS


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
      choices=[OptionChoice(name=name, value=value) for name, value in SERVERS]
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
    dm_permission=False,
    options=CmdConfig.options,
    default_member_permissions=Permissions()
  )


  async def leaderboard(self, interaction: ApplicationCommandInteraction, channel: TextChannel, server: str) -> None:
    try:
      grants = await self.api.get_grants()
      servers_id = [item.resource.id for item in grants.tokens.server]

      if server in servers_id:
        await interaction.response.send_message('Work in progress', ephemeral=True)

        leaderboards = await self.api.get_leaderboard(server, interaction=interaction)
        stats_detail: list[StatsDetail] = []

        for index, stats in enumerate(BOARD_STATS):
          ind_stats: list[StatsPlayer] = []

          for single_stats in leaderboards[index].leaderboard:
            ind_stats.append(
              StatsPlayer(name=single_stats.latest_name, stats=single_stats.dict().get(stats, 'Empty'))
            )
          
          stats_detail.append(StatsDetail(name=stats, players=ind_stats))

        embed = LeaderboardEmbed.get_embed(stats_detail)
        await channel.send(embed=embed)
        await interaction.edit_original_message('Done')
      else: raise Exception('Bad server id')

    except Exception as ex:
      logging.critical(ex)
      await interaction.edit_original_message(f'Some error | Check logs ```fix\n{ex}```')


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(LeaderboardCommand(bot))