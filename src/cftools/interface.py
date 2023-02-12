
class Config:
  api_url: str
  secret: str
  app_id: str


class ServerResource:
  gameserver_id: str
  id: str
  identifier: str
  object_id: str

class Server:
  created_at: str
  resource: ServerResource


class Tokens:
  server: list[Server]


class Grants:
  status: bool
  tokens: list[Tokens]