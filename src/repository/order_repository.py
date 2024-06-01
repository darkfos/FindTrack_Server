#System
from typing import Sequence, Tuple

#Other libraries
from sqlalchemy import select, Row
from sqlalchemy.ext.asyncio import AsyncSession

#Local
from src.repository.general_sql_repository import GeneralSQLRepository
from src.model.order import Order


class OrderRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Order):
        super().__init__(session=session, model=model)

    async def get_all_order_by_status(self, status: bool) -> Sequence[Row[Tuple[Order]]]:
        """
        Getting order by status
        """

        stmt = select(Order).where(Order.status == status)
        res_order_status = await self.session.execute(stmt)
        return res_order_status.fetchall()