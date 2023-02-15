from discord import Embed
import datetime as dt

class LeaderboardEmbed:

  content: dict

  def __init__(self, content) -> None:
    self.content = content

  def get_embed(self) -> Embed:
    dict_embed = self.get_row_embed(self.content)
    return Embed.from_dict(dict_embed)

  def get_row_embed(self, content) -> dict:
    return {
      "type": "rich",
      "title": content or 'Leaderborad',
      "description": "",
      "color": 0x9d8ce1,
      "fields": [
        {
          "name": 'kills',
          "value": '```css\n1. Test\n1. Test\n1. Test\n1. Test\n```'
        },
        {
          "name": 'k\d ratio',
          "value": '```css\n1. Test\n1. Test\n1. Test\n1. Test\n```'
        }
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