import requests

from src.cftools.interface import Config, Grants

class CfToolsApi:

  api_url: str
  secret: str
  app_id: str

  def __init__(self, config: Config) -> None:
    self.api_url = config.api_url
    self.secret = config.secret
    self.app_id = config.app_id

  def get_grants(self) -> Grants:
    pass