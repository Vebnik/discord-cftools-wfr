from disnake.ui import Button
from disnake import Component, ButtonStyle


class LeaderboardComponents:
  @classmethod
  def get_components(cls, server: str) -> Component:
    return [
      Button(
        label='Update', 
        custom_id=f'upd_board_btn|{server}', 
        disabled=False,
        style=ButtonStyle.success
      ),
      Button(
        label='Delete', 
        custom_id='del_board_btn', 
        disabled=False,
        style=ButtonStyle.danger
      )
    ]
