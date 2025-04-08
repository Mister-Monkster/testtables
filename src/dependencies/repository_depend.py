from typing import Annotated

from fastapi import Depends

from db.repositories.reservation_repository import ReservationRepository
from db.repositories.table_repository import TableRepository
from dependencies.session_depend import SessionDep


async def get_table_repository(session: SessionDep) -> TableRepository:
    return TableRepository(session)

TableRepDep = Annotated[TableRepository, Depends(get_table_repository)]


async def get_reservation_repository(session: SessionDep) -> ReservationRepository:
    return ReservationRepository(session)

ReservationRepDep = Annotated[ReservationRepository, Depends(get_reservation_repository)]