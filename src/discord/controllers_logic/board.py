import logging
from disnake import MessageInteraction

from settings import BOARD_STATS
from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import StatsDetail, StatsPlayer
from src.discord.embdes import LeaderboardEmbed
from src.discord.views import LeaderboardComponents


async def update_board(interaction: MessageInteraction, server, api: CfToolsApi) -> None:
    try:
        if not interaction.user.guild_permissions.administrator:
            return await interaction.response.send_message('Dont have permissions 🛑', ephemeral=True)

        grants = await api.get_grants()
        servers_id = [item.resource.id for item in grants.tokens.server]

        if server in servers_id:
            await interaction.response.send_message('Work in progress 🔄', ephemeral=True)

            leaderboards = await api.get_leaderboard(server)
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
            .send_message(f'Some error | Check logs ```fix\n{ex}\n```')
        logging.critical(ex)


async def delete_board(interaction: MessageInteraction) -> None:
    if not interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message('Dont have permissions 🛑', ephemeral=True)
    await interaction.message.delete()