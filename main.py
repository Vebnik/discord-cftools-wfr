from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import Config
from dotenv import load_dotenv; load_dotenv()
import os, asyncio, logging

from src.discord.app import AppConfig, App


def entry():

	api_config = Config(
		api_url=os.getenv('CF_TOOLS_ROOT_API'),
		secret=os.getenv('CF_TOOLS_SECRET'),
		app_id=os.getenv('CF_TOOLS_APPID')
	)

	api = CfToolsApi(api_config)

	# await api.db_connector.init_db()

	# token = await api.get_auth_token()
	# print(token)

	# grants = await api.get_grants()
	# print(grants)

	# servers_id = [server.resource.id for server in grants.tokens.server]
	# print(servers_id)

	# # TODO create cache logic, becouse overload mthod on api
	# boards = []
	# for server_id in servers_id:
	# 	boards.append(await api.get_leaderboard(server_id=server_id))
	# print(boards)

	if os.getenv('MODE') == 'dev':
		client = App(intents=AppConfig.intents_all, cf_api=api)
	elif os.getenv('MODE') == 'prod':
		client = App(intents=AppConfig.intents_def)

	client.run(os.getenv('DISCORD_BOT_TOKEN'), log_level=logging.INFO)

if __name__ == '__main__':
	entry()