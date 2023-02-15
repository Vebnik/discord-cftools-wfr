from dotenv import load_dotenv; load_dotenv()
import os, asyncio, logging

from src.discord.app import App
from src.discord.interface import DisConfig


def entry():

	logging.basicConfig(level=logging.INFO)

	dis_config = DisConfig(
		token=os.getenv('DISCORD_BOT_TOKEN'),
		app_id=os.getenv('DISCORD_APP_ID')
	)

	App(dis_config)

if __name__ == '__main__':
	entry()