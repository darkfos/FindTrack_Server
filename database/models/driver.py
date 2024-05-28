#Other libraries
from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict
from datetime import datetime


#Local
from database.main_base import MainBase


class Driver(MainBase):

    first_name: Mapped[str] = mapped_column(name="first_name_driver", type_=String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(name="last_name_driver", type_=String(150), nullable=True)
    #Question
    surname: Mapped[str] = mapped_column(name="surname_driver", type_=String(150), nullable=True)
    passport_series: Mapped[int] = mapped_column(name="passport_series", type_=Integer, nullable=True)
    passport_number: Mapped[int] = mapped_column(name="passport_number", type_=Integer, nullable=True)
    date_issue: Mapped[datetime] = mapped_column(name="date_issue", type_=DateTime(timezone=True))
    department_code: Mapped[int] = mapped_column(name="department_code", type_=Integer, nullable=True)
    place_issue: Mapped[str] = mapped_column(name="place_issue", type_=String(250), nullable=True)
    #Question - ссылка на фото, или bytes -> (я понял как ссылка)
    passport_photo_main: Mapped[str] = mapped_column(name="passport_photo_main", type_=Text, nullable=True)
    passport_photo_registration: Mapped[str] = mapped_column(name="passport_photo_registration", nullable=True)

    #Relation
    order: Mapped["Order"] = relationship("Order", back_populates="driver")

    def __repr__(self):
        res_dict: Dict[str, str] = {
            f"{k}": f"{v}"
            for k, v in self.__dict__.items()
        }

        return str(res_dict)

    def __str__(self):
        return self.__repr__()