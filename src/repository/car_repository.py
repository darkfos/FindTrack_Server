#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

#Local
from src.model.car import Car


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
        Get all car for carrier
        """

        pass