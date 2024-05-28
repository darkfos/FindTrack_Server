#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import create_engine

#Local
from database.main_base import MainBase


class Database:

    def __init__(self):
        self.engine = create_engine(url=...)
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
            await engine.run_sync(MainBase.metadata.create_all)


db_obj: Database = Database()