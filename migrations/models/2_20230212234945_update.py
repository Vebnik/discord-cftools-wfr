from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "command_used" VARCHAR(64) NOT NULL,
    "used_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";"""
