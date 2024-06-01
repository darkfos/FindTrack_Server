#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Union

#Local
from src.model.car import Car
from src.config.database import db_obj
from src.repository.general_sql_repository import GeneralSQLRepository
import asyncio


class CarRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Car):
        super().__init__(session=session, model=model)