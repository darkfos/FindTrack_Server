#Other libraries
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class DatabaseSettings(BaseSettings):
    """
    Settings for database
    """

    db_user: str = Field(alias="DB_USER")

    db_host: str = Field(alias="DB_HOST")

    db_password: str = Field(alias="DB_PASSWORD")

    db_name: str = Field(alias="DB_NAME")

    db_port: str = Field(alias="DB_PORT")

    model_config = SettingsConfigDict(env_file="template.env")
    db_echo: bool = True

db_sett = DatabaseSettings()