import datetime as dt, re
from disnake import Embed

from src.cftools.interface import Grants, StatsDetail

class LeaderboardEmbed:

  @classmethod
  def get_embed(cls, data: list[StatsDetail]) -> Embed:
    return Embed.from_dict(cls.get_row_embed(data))

  @classmethod
  def get_row_embed(cls, data: list[StatsDetail]) -> dict:
    return {
      "type": "rich",
      "title": 'Leaderborad',
      "description": "TOP players on server",
      "color": 0x9d8ce1,
      "fields": [
        {
          "name": item.name,
          "value": '```\n'+'\n'.join([f'{player.name} -> {player.stats}' for player in item.players])+'\n```'
        } for item in data
      ],
      "thumbnail": {
        "url": 'https://wfrdayz.ru/gallery_gen/849f813c94022f7f8a820435611f3cec.png',
        "height": 0,
        "width": 0
      },
      "footer": {
        "text": f'Updated at {dt.datetime.now().date()}',
        "icon_url": 'https://wfrdayz.ru/gallery_gen/849f813c94022f7f8a820435611f3cec.png'
      }
    }


class GrantsEmbed:

  reg_exp = re.compile(r"[T]|\.([\s\S])+$")

  @classmethod
  def get_embed(cls, data: Grants) -> Embed:
    return Embed.from_dict(cls.get_row_embed(data))

  @classmethod
  def get_row_embed(cls, data: Grants) -> dict:
    return {
      "type": "rich",
      "title": 'Grants',
      "description": 'Availible server',
      "color": 0x9d8ce1,
      "fields": [
        {
          "name": item.resource.identifier,
          "value": f'```css\nCreated at: {re.sub(cls.reg_exp, " ", item.created_at)}\nID: {item.resource.id}\nIdentifier: {item.resource.identifier}\n```'
        } for item in data.tokens.server
      ],
      "thumbnail": {
        "url": 'https://wfrdayz.ru/gallery_gen/849f813c94022f7f8a820435611f3cec.png',
        "height": 0,
        "width": 0
      },
      "footer": {
        "text": f'updated at {dt.datetime.now().date()}',
        "icon_url": 'https://wfrdayz.ru/gallery_gen/849f813c94022f7f8a820435611f3cec.png'
      }
    }
