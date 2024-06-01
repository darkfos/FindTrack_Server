#System
from typing import List, Union
import asyncio

#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

#Local
from src.model.car import Car
from src.config.database import db_obj
from src.repository.general_sql_repository import GeneralSQLRepository


class CarRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Car):
        super().__init__(session=session, model=model)