#Other libraries
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union

#Local
from src.model.order import Order


class OrderRepository:

    @staticmethod
    async def create_customer(session: AsyncSession, new_order: Order) -> bool:
        """
        Create a new customer
        """

        try:
            session.add(new_order)
            await session.commit()
            return True
        except Exception as ex:
            return False

    @staticmethod
    async def get_order_by_id(session: AsyncSession, id_order: int) -> Union[Order, None]:
        """
        Find 1 order by id
        """

        stmt = select(Order).where(Order.id == id_order)
        order_by_id = (await session.execute(stmt)).one_or_none()

        if order_by_id:
            return order_by_id[0]
        return None

    @staticmethod
    async def get_all_orders(session: AsyncSession) -> List[Order, List]:
        """
        Find all orders
        """

        stmt = select(Order)
        all_orders = (await session.execute(stmt)).fetchall()
        return all_orders

    @staticmethod
    async def get_order_by_status(session: AsyncSession, status: str ) -> Union[List[Order], List]:
        """
        Find all orders by status
        """

        stmt = select(Order).where(Order.status == True)
        all_order_by_status = (await session.execute(stmt)).fetchall()
        return all_order_by_status

    @staticmethod
    async def get_orders_by_id_customer(session: AsyncSession, id_customer: int) -> Union[List[Order], List]:
        """
        Find all orders by id customer
        """

        stmt = select(Order).where(Order.customer_id == id_customer)
        all_order_by_customer = (await session.execute(stmt)).fetchall()
        return all_order_by_customer

    @staticmethod
    async def update_status_order(session: AsyncSession, status: bool, id_customer: int) -> bool:
        """
        Update status order for customer
        """

        stmt = update(Order).where(Order.customer_id == id_customer).values(status=status)
        await session.execute(stmt)
        await session.commit()
        return True

    @staticmethod
    async def delete_order(session: AsyncSession, id_customer: int) -> bool:
        """
        Delete order for customer
        """

        try:
            stmt = delete(Order).where(Order.customer_id == id_customer)
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as ex:
            return False