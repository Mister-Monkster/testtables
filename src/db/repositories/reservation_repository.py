from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.models import ReservationModel


class ReservationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        try:
            query = select(ReservationModel)
            result = await self.session.execute(query)
            res = result.scalars().all()
            return res
        except Exception as e:
            print(e)
            return None

    async def create(self, reservation: dict) -> bool:
        try:
            new_reservation = ReservationModel(**reservation)
            self.session.add(new_reservation)
            await self.session.commit()
            return True
        except IntegrityError as e:
            print(f"Integrity Error: {e}")
            await self.session.rollback()
            return False

    async def delete(self, id: int):
        try:
            query = delete(ReservationModel).where(ReservationModel.id == id)
            await self.session.execute(query)
            await self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False