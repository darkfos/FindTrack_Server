#System
from typing import Sequence, Tuple

#Other libraries
from sqlalchemy import select, Row
from sqlalchemy.ext.asyncio import AsyncSession

#Local
from src.repository.general_sql_repository import GeneralSQLRepository
from src.model.driver import Driver


class DriverRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Driver):
        super().__init__(session=session, model=model)

    async def get_all_driver_for_carrier(self, id_carrier: int) -> Sequence[Row[Tuple[Driver]]]:
        """
        Getting all driver for carrier
        """

        stmt = select(Driver).where(Driver.id_carrier == id_carrier)
        all_driver_for_carrier = await self.session.execute(stmt)
        return all_driver_for_carrier.fetchall()