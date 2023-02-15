from dotenv import load_dotenv; load_dotenv()
import os, asyncio, logging

from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import CfConfig

from src.discord.app import App
from src.discord.interface import DisConfig


def entry():

	logging.basicConfig(level=logging.INFO)

	api_config = CfConfig(
		api_url=os.getenv('CF_TOOLS_ROOT_API'),
		secret=os.getenv('CF_TOOLS_SECRET'),
		app_id=os.getenv('CF_TOOLS_APPID')
	)

	dis_config = DisConfig(
		token=os.getenv('DISCORD_BOT_TOKEN'),
		app_id=os.getenv('DISCORD_APP_ID')
	)

	api = CfToolsApi(api_config)
	app = App(dis_config)

if __name__ == '__main__':
	entry()