import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, conint, Field

class Settings(BaseSettings):
    bot_token: SecretStr
    admin_id: conint(gt=0)
    backup_interval: conint(gt=0)

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

config = Settings()
