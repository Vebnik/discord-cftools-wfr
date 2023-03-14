import re
from disnake.ext.commands import Cog, InteractionBot, slash_command
from disnake import ApplicationCommandInteraction, Option, OptionType, OptionChoice

from src.cftools.cftools_api import CfToolsApi
from src.discord.embdes import StatsEmbed
from src.discord.models import User
from settings import CF_CONFIG, SERVERS


class CmdConfig:
  options = [
    Option(
      name='server',
      required=True,
      choices=[OptionChoice(name=name, value=value) for name, value in SERVERS]
    ),
    Option(
      name='steam_id',
      description='You steamid. To get steamid use -> steamid.pro',
      required=True,
      type=OptionType.string
    )
  ]


class StatsCommand(Cog):
  def __init__(self, bot: InteractionBot) -> None:
    self.bot = bot
    self.api = CfToolsApi(CF_CONFIG)

  @slash_command(
    name='stats',
    description='Get a single statistic in server',
    options=CmdConfig.options
  )
  async def stats(self, interaction: ApplicationCommandInteraction, server, steam_id) -> None:
    try:
      # await interaction.response.defer(ephemeral=True)
      await User.create(discord_identity=interaction.user.id, name=interaction.user.name, command_used='stats')
      
      if await self._valid_steam_id(steam_id) is False:
        return await self._send_error(interaction, steam_id)

      convert_data = await self.api.convert_steamid_to_cfid(steam_id)

      if convert_data.status is False:
        return await self._send_error(interaction, steam_id)

      stats = await self.api.get_individual_stats(convert_data.cftools_id, server)
      embed = StatsEmbed.get_embed(stats)

      await interaction.response.send_message(embed=embed, ephemeral=True)
    except Exception as ex:
      await interaction.response.send_message(f'```fix\n{ex}\n```', ephemeral=True)

  async def _send_error(self, interaction: ApplicationCommandInteraction, steam_id):
    await interaction.response.send_message(f'🛑\nNot a valid steamid: {steam_id}', ephemeral=True)

  async def _valid_steam_id(self, steam_id: str) -> bool:
    return not bool(re.search(r'[^\d]', steam_id))

# load ext
def setup(bot: InteractionBot):
  bot.add_cog(StatsCommand(bot)) 