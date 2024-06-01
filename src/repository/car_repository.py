#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Union

#Local
from src.model.car import Car
from src.config.database import db_obj
import asyncio


class CarRepository:

    @staticmethod
    async def create_car(session: AsyncSession, new_car: Car) -> bool:
        """
        Add a new car
        """
        try:
            session.add(new_car)
            await session.commit()
            return True
        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    async def get_all_car_for_id_carrier(session: AsyncSession, id_carrier: int) -> Union[List[Car], List]:
        """
        Receipt of all carrier vehicles
        """

        stmt = select(Car).where(Car.id_carrier == id_carrier)
        result = (await session.execute(stmt)).fetchall()
        return result

    @staticmethod
    async def get_all_working_car(session: AsyncSession) -> Union[List[Car], List]:
        """
        Getting all working machines
        """

        stmt = select(Car).where(Car.workload_car == True)
        result = (await session.execute(stmt)).fetchall()
        return result

    @staticmethod
    async def get_all_working_car_by_id_carrier(session: AsyncSession, id_carrier: int) -> Union[List[Car], List]:
        """
        Getting all working machines for carrier
        """

        stmt = select(Car).where(Car.id_carrier == id_carrier and Car.workload_car == True)
        all_working_car_for_carrier = (await session.execute(stmt)).fetchall()
        return all_working_car_for_carrier

    @staticmethod
    async def update_information_about_car(session: AsyncSession, id_car: int, data_update: dict) -> bool:
        """
        Update information about car
        """

        stmt = update(Car).where(Car.id == id_car).values(**data_update)
        await session.execute(stmt)
        await session.commit()

        return True

    @staticmethod
    async def delete_car(session: AsyncSession, id_car: int) -> bool:
        """
        Delete car
        """

        try:
            stmt = delete(Car).where(Car.id == id_car)
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as ex:
            return False