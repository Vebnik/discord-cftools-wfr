from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import Config
from dotenv import load_dotenv; load_dotenv()
import os, asyncio


async def entry():
	config = Config(
		api_url=os.getenv('CF_TOOLS_ROOT_API'),
		secret=os.getenv('CF_TOOLS_SECRET'),
		app_id=os.getenv('CF_TOOLS_APPID')
	)

	api = CfToolsApi(config)

	await api.db_connector.init_db()
	
	token = await api.get_auth_token()
	print(token)

	grants = await api.get_grants()
	print(grants)

if __name__ == '__main__':
	asyncio.run(entry())