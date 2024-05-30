from dotenv import load_dotenv
from os import getenv

load_dotenv("../../.env")


class DatabaseSettingsForConnection:

    db_name: str = getenv("DB_NAME")
    db_user: str = getenv("DB_USER")
    db_password: str = getenv("DB_PASSWORD")
    db_port: str = getenv("DB_PORT")
    db_host: str = getenv("DB_HOST")
    db_echo: bool = True

db = DatabaseSettingsForConnection()