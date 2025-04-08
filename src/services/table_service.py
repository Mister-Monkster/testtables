from db.repositories.table_repository import TableRepository
from schemas.table_schemas import TablePostSchema


class TableService:
    def __init__(self, repository: TableRepository):
        self.repository = repository

    async def get_all_tables(self):
        result = await self.repository.get_all()
        if result:
            return result
        else:
            return False

    async def create_table(self, table: TablePostSchema):
        try:
            table_dict = table.model_dump()
            res = await self.repository.create(table_dict)
            return res
        except Exception as e:
            print(e)
            return False

    async def delete_table(self, id: int):
        try:
            await self.repository.delete(id)
            return True
        except Exception as e:
            print(e)
            return False

