from datetime import datetime
from typing import Optional
from sqlalchemy import CheckConstraint, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship



class Base(DeclarativeBase):
    pass


class TableModel(Base):
    __tablename__ = 'Table'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[Optional[str]] = mapped_column(String(128), unique=True, index=True)
    seats: Mapped[Optional[int]] = mapped_column(default=1)
    location: Mapped[str] = mapped_column(String(128))
    reservation_rel: Mapped[list["ReservationModel"]] = relationship(back_populates="table_rel")

    __table_args__ = (
        CheckConstraint('seats > 0', name='check_seats_positive'),
    )


class ReservationModel(Base):
    __tablename__ = 'Reservation'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column(String(128), nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey('Table.id', ondelete='CASCADE'), index=True)
    reservation_time: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    duration_minutes: Mapped[Optional[int]] = mapped_column(default=60)
    table_rel: Mapped["TableModel"] = relationship(back_populates='reservation_rel')