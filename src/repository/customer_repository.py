#System
...

#Other libraries
from sqlalchemy.ext.asyncio import AsyncSession

#Local
from src.model.customer import Customer
from src.repository.general_sql_repository import GeneralSQLRepository


class CustomerRepository(GeneralSQLRepository):

    def __init__(self, session: AsyncSession, model=Customer):
        super().__init__(session=session, model=model)