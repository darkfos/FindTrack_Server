#Other libraries
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union

#Local
from src.repository.general_sql_repository import GeneralSQLRepository
from src.model.order import Order


class OrderRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Order):
        super().__init__(session=session, model=model)