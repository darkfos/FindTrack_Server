#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Union

#Local
from src.repository.general_sql_repository import GeneralSQLRepository
from src.model.carrier import Carrier


class CarrierRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Carrier):
        super().__init__(session=session, model=model)