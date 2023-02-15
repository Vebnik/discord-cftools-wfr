import requests, logging, datetime as dt
from src.cftools.interface import CfConfig, Grants, ApiMethods, AuthData, StatsBoard
from src.database.connector import Connector
from src.cftools.models import AuthToken, Grant
from tortoise import Tortoise


class CfToolsApi:

  api_url: str
  secret: str
  app_id: str
  auth_data: AuthData
  grants: Grants
  db_connector: Connector

  def __init__(self, config: CfConfig) -> None:
    self.api_url = config.api_url
    self.secret = config.secret
    self.app_id = config.app_id
    self.db_connector = Connector()

  async def get_grants(self, update=False) -> Grants:
    try:
      grant = await Grant.all().order_by('created_at').first()

      if not grant or update:
        headers = { 'Authorization': f'Bearer {self.auth_data.token}' }
        response = requests.get(f'{self.api_url}{ApiMethods.grants}', headers=headers)

        await Grant.create(data=response.json())
        self.grants = Grants.parse_obj(response.json())

        return self.grants

      self.grants = Grants.parse_obj(grant.data)

      return self.grants
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

        return self.auth_data

      self.auth_data = AuthData(status=True, token=is_valid)

      return self.auth_data
    except Exception as ex:
      logging.critical(ex)

  async def get_leaderboard(self, server_id, url=None) -> StatsBoard:
    try:
      headers = { 'Authorization': f'Bearer {self.auth_data.token}' }
      root_url = url or f'{self.api_url}{ApiMethods.board(server_id=server_id)}'
      response = requests.get(root_url, headers=headers)

      return StatsBoard.parse_obj(response.json())
    except Exception as ex:
      logging.critical(ex)

  async def _valid_time_token(self) -> bool|str:
    data = await AuthToken.all().order_by('created_at').first()
    diff_time = dt.datetime.now() - data.created_at.replace(tzinfo=None)

    if diff_time.days >= 1:
      return False

    return data.token