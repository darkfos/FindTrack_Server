#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import create_engine

#Local
from src.model.base import Base
from src.config.database_settings import db


class Database:

    def __init__(self):
        self.engine = create_engine(
            url="postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}".format(db.db_user, db.db_password,
                                                                  db.db_host, db.db_port, db.db_name),
            echo=db.db_echo
        )
        self.as_session_maker: async_sessionmaker = async_sessionmaker(bind=self.engine)

    async def get_session(self) -> AsyncSession:
        async with self.as_session_maker.begin() as local_session:
            yield local_session

    async def create_tables(self) -> None:
        """
        Creating tables with help Base metadata
        :return:
        """

        async with self.engine.begin() as engine:
            await engine.run_sync(Base.metadata.create_all)


db_obj: Database = Database()
