#System
from typing import Tuple, Sequence

#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Row

#Local
from src.model.car import Car
from src.repository.general_sql_repository import GeneralSQLRepository


class CarRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Car):
        super().__init__(session=session, model=model)

    async def get_all_car_for_id_carrier(self, id_carrier: int) -> Sequence[Row[Tuple[Car]]]:
        """
        Receipt of all carrier vehicles
        """

        stmt = select(Car).where(Car.id_carrier == id_carrier)
        car_for_carrier = await self.session.execute(stmt)
        return car_for_carrier.fetchall()

    async def get_all_working_car(self) -> Sequence[Row[Tuple[Car]]]:
        """
        Getting all working car
        """

        stmt = select(Car).where(Car.workload_car == True)
        all_working_car = await self.session.execute(stmt)
        return all_working_car.fetchall()

    async def get_all_working_car_by_carrier(self, id_carrier: int) -> Sequence[Row[Tuple[Car]]]:
        """
        Getting all working car for carrier
        """

        stmt = select(Car).where(Car.id_carrier == id_carrier and Car.workload_car == True)
        all_working_car_for_carrier = await self.session.execute(stmt)
        return all_working_car_for_carrier.fetchall()