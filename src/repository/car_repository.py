#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, Result

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
            return False

    @staticmethod
    async def delete_car(session: AsyncSession, id_car: int) -> bool:
        """
        Delete car
        """

        del_car = delete(Car).where(Car.id == id_car)
        await session.execute(del_car)
        await session.commit()

        return True

    @staticmethod
    async def get_all_car_for_id_carrier(session: AsyncSession, id_carrier: int):
        """
        Receipt of all carrier vehicles
        """

        res_sel_cars: Result = select(Car).where(Car.id_carrier == id_carrier)
        result = (await session.execute(res_sel_cars)).fetchall()
        print(result, type(result))


async def main():
    async with db_obj.as_session_maker.begin() as session:
        await CarRepository.get_all_car_for_id_carrier(session=session, id_carrier=1)

asyncio.run(main())