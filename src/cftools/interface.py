from pydantic import BaseModel
from typing import Any
from datetime import datetime


class CfConfig(BaseModel):
  api_url: str
  secret: str
  app_id: str


class ServerResource(BaseModel):
  gameserver_id: str
  id: str
  identifier: str
  object_id: str


class Server(BaseModel):
  created_at: str
  resource: ServerResource


class Tokens(BaseModel):
  server: list[Server]


class Grants(BaseModel):
  status: bool
  tokens: Tokens


class AuthData(BaseModel):
  status: bool
  token: str
  created_at: datetime


class SingleStats(BaseModel):
  cftools_id: str|Any
  deaths: int|Any
  environment_deaths: int|Any
  falldamage_deaths: int|Any
  hits: int|Any
  kdratio: float|Any
  kills: int|Any
  latest_name: str|Any
  longest_kill: float|Any
  longest_shot: float|Any
  playtime: int|Any
  rank: int|Any
  suicides: int|Any


class Leaderboard(BaseModel):
  leaderboard: list[SingleStats]|Any
  status: bool
  error: str|Any


class StatsPlayer(BaseModel):
  name: str|Any
  stats: str|Any


class StatsDetail(BaseModel):
  name: str|Any
  players: list[StatsPlayer]|Any


class ConvertId(BaseModel):
  cftools_id: str|Any
  status: bool


class GameStatsGeneral(BaseModel):
  deaths: int|Any
  environment_deaths: int|Any
  hits: int|Any
  kdratio: float|Any
  kills: int|Any
  longest_kill: float|Any
  longest_shot: float|Any
  suicides: int|Any


class GameStats(BaseModel):
  general: GameStatsGeneral|Any


class IndividualStats(BaseModel):
  cleared_at: datetime
  created_at: datetime
  updated_at: datetime
  game: GameStats|Any
  omega: dict


# other 
class ApiMethods:

  api_ver = 'v1'

  auth = f'{api_ver}/auth/register'
  grants = f'{api_ver}/@app/grants'
  convert = f'{api_ver}/users/lookup?identifier='

  @classmethod
  def board(cls, server_id, stat=None, order=-1, limit=15) -> str:
    return f'{cls.api_ver}/server/{server_id}/leaderboard?stat={stat or "kills"}&{order=}&{limit=}'

  @classmethod
  def ind_stats(cls, cftools_id: str, server: str) -> str:
    return f'{cls.api_ver}/server/{server}/player?cftools_id={cftools_id}'

  