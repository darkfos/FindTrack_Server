#Other libraries
from sqlalchemy import Double, String, Text, Date, Enum, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict
from datetime import datetime


#Local
from src.model.base import Base


class StatusOrder(Enum):
    """Status for order"""
    IN_PROGRESS: str = "В процессе"
    COMPLETED: str = "Завершен"


class Order(Base):

    cargo_name: Mapped[str] = mapped_column(name="cargo_name", type_=String(300), index=True, nullable=True)
    departure_address: Mapped[str] = mapped_column(name="departure_address", type_=String(350),
                                                   index=True, nullable=True)
    departure_date: Mapped[datetime] = mapped_column(name="departure_date", type=Date, nullable=True)
    arrival_address: Mapped[str] = mapped_column(name="arrival_address", type_=String(350), index=True, nullable=True)
    arrival_date: Mapped[datetime] = mapped_column(name="arrival_date", type_=Date, nullable=True)
    cargo_weight: Mapped[float] = mapped_column(name="cargo_weight", type_=Double, nullable=True)
    cargo_dimensions: Mapped[float] = mapped_column(name="cargo_dimensions", type_=Double, nullable=False)
    money: Mapped[float] = mapped_column(name="money", type_=Double, nullable=True)
    description: Mapped[str] = mapped_column(name="description", type_=Text, nullable=True)
    status: Mapped[str] = mapped_column(name="status", type_=Enum(StatusOrder), nullable=True)

    #Foreign key
    driver_id: Mapped[int] = mapped_column(ForeignKey("Driver.id"), type_=Integer)
    car_id: Mapped[int] = mapped_column(ForeignKey("Car.id"), type_=Integer)

    #Relations
    driver: Mapped["Driver"] = relationship("Driver", back_populates="order")
    car: Mapped["Car"] = relationship("Car", back_populates="order")

    def __repr__(self):

        res_dict: Dict[str, str] = {
            f"{k}": f"{v}"
            for k,v in self.__dict__.items()
        }

        return str(res_dict)

    def __str__(self):
        return self.__repr__()