from fastapi import HTTPException

from fastapi import APIRouter

from dependencies.service_depend import table_service
from schemas.table_schemas import TablePostSchema, TableGetSchema

table_router = APIRouter(prefix='/tables', tags=['Столики',])

"""
GET /tables/ — список всех столиков
POST /tables/ — создать новый столик
DELETE /tables/{id} — удалить столик
"""


@table_router.get("/", summary='Получить все столики*️⃣')
async def get_all_tables(service: table_service) -> list[TableGetSchema] | dict:
    try:
        res = await service.get_all_tables()
        if res:
            return res
        else:
            return {"ok": True, 'detail': 'В базе данных нет ни одного столика.'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')


@table_router.post("/", summary='Добавить столик➕')
async def create_table(table: TablePostSchema, service: table_service):
    try:
        res = await service.create_table(table)
        if res:
            return {'ok': True, "detail": 'Столик успешно добавлен.'}
        else:
            return {'ok': False, "detail": 'При добавлении столика произошла ошибка'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')


@table_router.delete("/{id}", summary='Удалить столик❌')
async def delete_table(id: int, service: table_service):
    try:
        res = await service.delete_table(id)
        if res:
            return {'ok': True, "detail": f'Столик c id {id} успешно удален.'}
        else:
            return {'ok': False, "detail": 'При удалении столика произошла ошибка'}
    except:
        raise HTTPException(status_code=500, detail='Server Error')