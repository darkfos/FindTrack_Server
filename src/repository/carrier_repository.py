#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from typing import List, Union

#Local
from src.model.carrier import Carrier


class CarrierRepository:

    @staticmethod
    async def create_carrier(session: AsyncSession, new_carrier: Carrier) -> bool:
        """
        Create a new carrier
        """

        try:
            session.add(new_carrier)
            await session.commit()
            return True
        except Exception as ex:
            return False

    @staticmethod
    async def get_carrier_by_id(session: AsyncSession, id_carrier: int) -> Union[Carrier, None]:
        """
        Get information about carrier by id
        """

        stmt = select(Carrier).where(Carrier.id == id_carrier)
        information_about_carrier = (await session.execute(stmt)).one_or_none()

        if information_about_carrier:
            return information_about_carrier[0]
        return None

    @staticmethod
    async def update_rating_carrier(session: AsyncSession, id_carrier: int, score_rating: int) -> bool:
        """
        Update rating carrier
        """

        stmt = select(Carrier).where(Carrier.id == id_carrier)
        data_rating = (await session.execute(stmt)).one_or_none()
        if data_rating:
            stmt = update(Carrier).where(Carrier.id == id_carrier).values(rating=data_rating[0].rating + score_rating)
        return False

    @staticmethod
    async def delete_carrier_by_id(session: AsyncSession, id_carrier: int) -> bool:
        """
        Delete carrier by id
        """

        try:
            stmt = delete(Carrier).where(Carrier.id == id_carrier)
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as ex:
            return False