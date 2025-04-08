from typing import Annotated

from fastapi import Depends

from dependencies.repository_depend import TableRepDep, ReservationRepDep
from services.reservation_service import ReservationService
from services.table_service import TableService


async def get_table_service(repository: TableRepDep) -> TableService:
    return TableService(repository)

table_service = Annotated[TableService, Depends(get_table_service)]


async def get_reservation_service(repository: ReservationRepDep) -> ReservationService:
    return ReservationService(repository)

reservation_service = Annotated[ReservationService, Depends(get_reservation_service)]