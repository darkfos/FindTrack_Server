#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, insert


class GeneralSQLRepository:

    def __init__(self, session: AsyncSession, model=None):
        self.session = session
        self.model = model

    async def add_one(self, data: dict):
        """
        Added information
        """

        stmt = insert(self.model).values(**data).returning(self.model.id)
        res_to_add = await self.session.execute(stmt)
        return res_to_add.scalar_one()

    async def find_one(self, other_id: int):
        """
        Find information
        """

        stmt = select(self.model).where(self.model.id == other_id)
        res_find_information = await self.session.execute(stmt)
        return res_find_information.scalar_one()

    async def find_all(self):
        """
        Find all information
        """

        stmt = select(self.model)
        res_all_information = await self.session.execute(stmt)
        return res_all_information.fetchall()

    async def edit_one(self, other_id: int, other_data_to_update: dict):
        """
        Update information
        """

        stmt = update(self.model).where(self.model.id == other_id).values(**other_data_to_update)
        res_to_update = await self.session.execute(stmt)
        return res_to_update.scalar_one()

    async def delete_one(self, other_id: int):
        """
        Delete information
        """

        stmt = delete(self.model).where(self.model.id == other_id)
        res_to_delete = await self.session.execute(stmt)
        return res_to_delete.rowcount