import requests, logging, datetime as dt
from src.cftools.interface import Config, Grants, ApiMethods, AuthData
from src.database.connector import Connector
from src.database.models import AuthToken
from tortoise import Tortoise


class CfToolsApi:

  api_url: str
  secret: str
  app_id: str
  auth_data: AuthData
  db_connector: Connector

  def __init__(self, config: Config) -> None:
    self.api_url = config.api_url
    self.secret = config.secret
    self.app_id = config.app_id
    self.db_connector = Connector()

  async def get_grants(self) -> Grants:
    try:
      headers = { 'Authorization': f'Bearer {self.auth_data.token}' }
      response = requests.get(f'{self.api_url}{ApiMethods.grants}', headers=headers)

      return Grants.parse_obj(response.json())
    except Exception as ex:
      logging.critical(ex)

  async def get_auth_token(self) -> AuthData:
    try:
      is_valid = await self._valid_time_token()

      if not is_valid:
        body = { 'application_id': self.app_id, 'secret': self.secret }
        response = requests.post(f'{self.api_url}{ApiMethods.auth}', json=body)

        self.auth_data = AuthData.parse_obj(response.json())

        await AuthToken.create(token=self.auth_data.token)
        await Tortoise.close_connections()

        return self.auth_data

      await Tortoise.close_connections()

      self.auth_data = AuthData(status=True, token=is_valid)
      return self.auth_data
    except Exception as ex:
      logging.critical(ex)

  async def _valid_time_token(self) -> bool|str:
    data = await AuthToken.all().order_by('created_at').first()
    diff_time = dt.datetime.now() - data.created_at.replace(tzinfo=None)

    if diff_time.days >= 1:
      return False

    return data.token
