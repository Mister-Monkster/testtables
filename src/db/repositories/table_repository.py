from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.models import TableModel


class TableRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        try:
            query = select(TableModel)
            result = await self.session.execute(query)
            res = result.scalars().all()
            return res
        except Exception as e:
            print(e)
            return None


    async def create(self, table: dict) -> bool:
        try:
            new_table = TableModel(**table)
            self.session.add(new_table)
            await self.session.commit()
            return True
        except IntegrityError as e:
            print(f"Integrity Error: {e}")
            await self.session.rollback()
            return False

    async def delete(self, id: int) -> bool:
        try:
            query = delete(TableModel).where(TableModel.id == id)
            await self.session.execute(query)
            await self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False