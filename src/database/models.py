from tortoise.models import Model
from tortoise import fields


class AuthToken(Model):
  token = fields.CharField(max_length=255)
  created_at = fields.DatetimeField(auto_now_add=True)

