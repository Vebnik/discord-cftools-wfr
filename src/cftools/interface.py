from pydantic import BaseModel


class Config(BaseModel):
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


class ApiMethods:

  api_ver = 'v1'

  auth = f'{api_ver}/auth/register'
  grants = f'{api_ver}/@app/grants'