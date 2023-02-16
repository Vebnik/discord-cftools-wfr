import logging
from disnake import MessageInteraction
from disnake.ext.commands import InteractionBot

from settings import BOARD_STATS, CF_CONFIG
from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import StatsDetail, StatsPlayer
from src.discord.embdes import LeaderboardEmbed
from src.discord.views import LeaderboardComponents


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
        try:
          if not interaction.user.guild_permissions.administrator:
            return await interaction.response.send_message('Dont have permissions 🛑', ephemeral=True)

          grants = await cls.api.get_grants()
          servers_id = [item.resource.id for item in grants.tokens.server]

          if server in servers_id:
            await interaction.response.send_message('Work in progress 🔄', ephemeral=True)

            leaderboards = await cls.api.get_leaderboard(server, interaction=interaction)
            stats_detail: list[StatsDetail] = []

            for index, stats in enumerate(BOARD_STATS):
              ind_stats: list[StatsPlayer] = []

              for single_stats in leaderboards[index].leaderboard:
                ind_stats.append( StatsPlayer(name=single_stats.latest_name, stats=single_stats.dict().get(stats, 'Empty')) )
              
              stats_detail.append(StatsDetail(name=stats, players=ind_stats))

            embed = LeaderboardEmbed.get_embed(stats_detail)
            components = LeaderboardComponents.get_components(server)

            await interaction.message.edit(embed=embed, components=components)
          else: raise Exception('Bad server id')

        except Exception as ex:
          await interaction.response\
            .send_message(f'Some error | Check logs ```fix\n{ex}\n{leaderboards[0].error if leaderboards[0].error else ""}```')
          logging.critical(ex)

      case 'del_board_btn': 
        if not interaction.user.guild_permissions.administrator:
          return await interaction.response.send_message('Dont have permissions 🛑', ephemeral=True)
        await interaction.message.delete()
          

