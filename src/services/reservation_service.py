from db.repositories.reservation_repository import ReservationRepository
from schemas.reservation_schemas import ReservationPostSchema


class ReservationService:
    def __init__(self, repository: ReservationRepository):
        self.repository = repository

    async def get_all_reservations(self):
        result = await self.repository.get_all()
        if result:
            return result
        else:
            return False

    async def create_reservation(self, reservation: ReservationPostSchema):
        try:
            reservation_dict = reservation.model_dump()
            if res := await self.repository.create(reservation_dict):
                return res
        except Exception as e:
            print(e)
            return False

    async def delete_reservation(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except Exception as e:
            print(e)
            return False