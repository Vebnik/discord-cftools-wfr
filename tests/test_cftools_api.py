from src.cftools.cftools_api import CfToolsApi
from src.cftools.interface import Config
from dotenv import load_dotenv; load_dotenv()
import os, logging

# init
logging.basicConfig(level=logging.INFO)

config = Config(
  api_url=os.getenv('CF_TOOLS_ROOT_API'),
  secret=os.getenv('CF_TOOLS_SECRET'),
  app_id=os.getenv('CF_TOOLS_APPID')
)

api = CfToolsApi(config)

# tests
def test_get_get_auth_token():
  auth_data = api.get_auth_token()
  assert isinstance(auth_data.token, str) == True


def test_get_grants():
  grants = api.get_grants()
  logging.critical(grants)

  assert True == False