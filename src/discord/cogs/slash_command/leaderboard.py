from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction, TextChannel, Option, OptionType


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


class LeaderboardCommand(Cog):

  bot: InteractionBot

  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot

  @slash_command(
    name='leaderboard',
    description='Spawn Leaderboard in select channels',
    options=CmdConfig.options
  )
  async def leaderboard(self, interaction: ApplicationCommandInteraction, channel, server) -> None:
    print(channel, server)
    await interaction.response.send_message('Nice Leaderboard', ephemeral=True)


# load ext
def setup(bot: InteractionBot):
  bot.add_cog(LeaderboardCommand(bot))