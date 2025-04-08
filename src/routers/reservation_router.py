from fastapi import APIRouter, HTTPException

from dependencies.service_depend import reservation_service
from schemas.reservation_schemas import ReservationPostSchema, ReservationGetSchema

reservation_router = APIRouter(prefix='/reservations', tags=['Бронь',])

"""
GET /reservations/ — список всех броней
POST /reservations/ — создать новую бронь
DELETE /reservations/{id} — удалить бронь
"""


@reservation_router.get('/', summary='список всех броней*️⃣')
async def get_all_reservations(service: reservation_service) -> list[ReservationGetSchema] | dict:
    try:
        res = await service.get_all_reservations()
        if res:
            return res
        else:
            return {"ok": True, 'detail': 'Ни один столик еще не забронирован.'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')


@reservation_router.post('/', summary="Забронировать столик🖊")
async def create_reservation(reservation: ReservationPostSchema, service: reservation_service):
    try:
        res = await service.create_reservation(reservation)
        if res:
            return {'ok': True, "detail": 'Столик успешно забронирован.'}
        else:
            return {'ok': False, "detail": 'При брони столика произошла ошибка. '
                                           'Проверьте, существует ли столик с указанным id'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')


@reservation_router.delete('/{id}', summary='Снять бронь❌')
async def delete_reservation(id: int, service: reservation_service):
    try:
        res = await service.delete_reservation(id)
        if res:
            return {'ok': True, "detail": f'Бронь c id {id} успешно снята.'}
        else:
            return {'ok': False, "detail": 'При снятии брони произошла ошибка'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')