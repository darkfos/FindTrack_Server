#Other libraries
from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Dict, List

#Local
from src.model.base import Base


class Carrier(Base):

    com_name: Mapped[int] = mapped_column(name="company_name", type_=Integer, index=True, nullable=True)
    status: Mapped[bool] = mapped_column(name="status", type_=Boolean, index=False, nullable=False)
    inn: Mapped[int] = mapped_column(name="inn_carrier", type_=Integer, nullable=True)
    ogrn: Mapped[int] = mapped_column(name="ogrn_carrier", type_=Integer, nullable=False)
    kpp: Mapped[int] = mapped_column(name="kpp_customer", type_=Integer, nullable=False)
    checking_account: Mapped[bool] = mapped_column(name="checking_account", type_=Boolean, nullable=True)
    correpondent_account: Mapped[bool] = mapped_column(name="correpondent_account", type_=Boolean, nullable=False)
    bic: Mapped[str] = mapped_column(name="bic", type_=String(650), nullable=True)
    actual_address: Mapped[str] = mapped_column(name="actual_address", type_=String(400), nullable=True)
    legal_address: Mapped[str] = mapped_column(name="legal_address", type_=String(400), nullable=True)
    date_registration: Mapped[datetime] = mapped_column(name="date_registration", type_=DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    date_foundation: Mapped[datetime] = mapped_column(name="date_foundation", type_=DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    taken_orders: Mapped[int] = mapped_column(name="taken_orders", type_=Integer, nullable=False, default=0)
    completed_orders: Mapped[int] = mapped_column(name="completed_orders", type_=Integer, nullable=False, default=0)
    rating: Mapped[int] = mapped_column(name="rating", type_=Integer, nullable=False, default=0)

    #Relations
    car_carrier: Mapped[List["Car"]] = relationship(back_populates="carrier", uselist=True)
    driver: Mapped["Driver"] = relationship(back_populates="carrier")

    def __repr__(self):
        res_dict: Dict[str, str] = {
            f"{k}": f"{v}"
            for k, v in self.__dict__.items()
        }

        return str(res_dict)

    def __str__(self):
        return self.__repr__()