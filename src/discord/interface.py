from pydantic import BaseModel


class DisConfig(BaseModel):
  token: str
  app_id: str