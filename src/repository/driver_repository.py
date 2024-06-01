#Other libraries
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union

#Local
from src.model.driver import Driver


class DriverRepository:

    @staticmethod
    async def create_driver(session: AsyncSession, new_driver: Driver) -> bool:
        """
        Create a new driver
        """

        try:
            session.add(new_driver)
            await session.commit()
            return True
        except Exception as ex:
            return False

    @staticmethod
    async def get_all_drivers(session: AsyncSession) -> Union[List[Driver], List]:
        """
        Get all drivers
        """

        stmt = select(Driver)
        all_drivers = (await session.execute(stmt)).fetchall()
        return all_drivers

    @staticmethod
    async def get_driver_by_carrier(session: AsyncSession, id_carrier: int) -> Union[List[Driver], List]:
        """
        Get all drivers for carrier
        """

        stmt = select(Driver).where(Driver.id_carrier == id_carrier)
        all_drivers = (await session.execute(stmt)).fetchall()
        return all_drivers

    @staticmethod
    async def delete_driver(session: AsyncSession, id_driver: int) -> bool:
        """
        Delete driver by id
        """

        try:
            delete_driver = delete(Driver).where(Driver.id == id_driver)
            await session.execute(delete_driver)
            await session.commit()
            return True
        except Exception as ex:
            return False