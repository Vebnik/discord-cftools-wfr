from tortoise import Model, fields


class User(Model):
  discord_id: fields.CharField(max_length=255)
  name = fields.CharField(max_length=255)
  command_used = fields.CharField(max_length=64)
  used_at = fields.DatetimeField(auto_now_add=True)