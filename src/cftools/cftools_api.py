import requests, logging, datetime as dt

from src.cftools.interface import CfConfig, Grants, ApiMethods, AuthData, Leaderboard
from src.cftools.models import AuthToken, Grant


class CfToolsApi:

  api_url: str
  secret: str
  app_id: str
  auth_data: AuthData|None = None

  def __init__(self, config: CfConfig) -> None:
    self.api_url = config.api_url
    self.secret = config.secret
    self.app_id = config.app_id

  async def get_grants(self, update=False) -> Grants:
    try:
      if not await self._valid_time_token(): await self._init_auth()

      grant = await Grant.all().order_by('-created_at').first()

      if not grant or update:
        headers = { 'Authorization': f'Bearer {self.auth_data.token}' }
        response = requests.get(f'{self.api_url}{ApiMethods.grants}', headers=headers)

        await Grant.create(data=response.json())
        return Grants.parse_obj(response.json())

      return Grants.parse_obj(grant.data)
    except Exception as ex:
      logging.critical(ex)

  async def get_leaderboard(self, server_id, url=None) -> Leaderboard:
    try:
      if not await self._valid_time_token(): await self._init_auth()

      headers = { 'Authorization': f'Bearer {self.auth_data.token}' }
      root_url = url or f'{self.api_url}{ApiMethods.board(server_id=server_id)}'
      response = requests.get(root_url, headers=headers)

      return Leaderboard.parse_obj(response.json())
    except Exception as ex:
      logging.critical(ex)

  # ------ Private ------
  async def _init_auth(self) -> AuthData:
    try:
      body = { 'application_id': self.app_id, 'secret': self.secret }
      response = requests.post(f'{self.api_url}{ApiMethods.auth}', json=body)

      new_token = await AuthToken.create(token=response.json().get('token'))
      self.auth_data = AuthData(token=new_token.token, created_at=new_token.created_at, status=True)

      return self.auth_data
    except Exception as ex:
      logging.critical(ex)
  
  async def _valid_time_token(self) -> bool|str:
    data = await AuthToken.all().order_by('-created_at').first()

    if self.auth_data is None and data:
      diff_time = dt.datetime.now() - data.created_at.replace(tzinfo=None)

      if diff_time.days >= 1: 
        return False
      else: 
        self.auth_data = AuthData(token=data.token, created_at=data.created_at, status=True)
        return True

    if self.auth_data is not None:
      diff_time = dt.datetime.now() - self.auth_data.created_at.replace(tzinfo=None)

      if diff_time.days >= 1: return False
      else: return True

    return False
