#Other libraries
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union

#Local
from src.model.customer import Customer


class CustomerRepository:

    @staticmethod
    async def create_customer(session: AsyncSession, new_customer: Customer) -> bool:
        """
        Create a new customer
        """

        try:
            session.add(new_customer)
            await session.commit()
            return True
        except Exception as ex:
            return False

    @staticmethod
    async def get_all_customers(session: AsyncSession) -> Union[List[Customer], List]:
        """
        Get information about all customers
        """

        stmt = select(Customer)
        all_customers = (await session.execute(stmt)).fetchall()
        return all_customers

    @staticmethod
    async def get_customer_by_id(session: AsyncSession, id_customer: int) -> Union[Customer, None]:
        """
        Get information about customer by id
        """

        stmt = select(Customer).where(Customer.id == id_customer)
        information_about_customer = (await session.execute(stmt)).one_or_none()

        if information_about_customer:
            return information_about_customer[0]
        return None

    @staticmethod
    async def update_rating_customer(session: AsyncSession, id_customer: int, rating: int) -> bool:
        """
        Update rating customer
        """

        stmt = select(Customer).where(Customer.id == id_customer)
        data = (await session.execute(stmt)).one_or_none()
        if data:
            stmt = update(Customer).where(Customer.id == id_customer).values(rating=data[0].rating+rating)
            await session.execute(stmt)
            await session.commit()
        return False

    @staticmethod
    async def update_total_orders_customer(session: AsyncSession, id_customer: int, count_end_order: int = 1) -> bool:
        """
        Update total orders customer
        """

        stmt = select(Customer).where(Customer.id == id_customer)
        data = (await session.execute(stmt)).one_or_none()
        if data:
            stmt = update(Customer).where(Customer.id == id_customer).values(total_orders=data[0].total_orders+count_end_order)
            await session.execute(stmt)
            await session.commit()
        return False

    @staticmethod
    async def update_completed_orders_customer(session: AsyncSession, id_customer: int, count_end_order: int = 1) -> bool:
        """
        Update total orders customer
        """

        stmt = select(Customer).where(Customer.id == id_customer)
        data = (await session.execute(stmt)).one_or_none()
        if data:
            stmt = update(Customer).where(Customer.id == id_customer).values(total_orders=data[0].completed_orders+count_end_order)
            await session.execute(stmt)
            await session.commit()
            return True
        return False

    @staticmethod
    async def delete_customer(session: AsyncSession, id_customer: int) -> bool:
        """
        Delete customer for id
        """

        try:
            stmt = delete(Customer).where(Customer.id == id_customer)
            await session.execute(stmt)
            await session.commit()
            return True
        except Exception as ex:
            return False