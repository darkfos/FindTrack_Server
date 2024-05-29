#Other libraries
from sqlalchemy import String, Integer, Text, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict


#Local
from database.main_base import MainBase


class BodyType(Enum):
    """Body type for car"""

    EASY: str = "Малотоннажный грузовик" # weight <= 2.5t
    MEDIUM: str = "Среднетоннажный грузовик" # 5 <= weight <= 10t
    HEAVY: str = "Большегрузная машина" # 5 <= weight <= 30


class BodyDimension(Enum):
    """Body dimension for car"""

    ...


class Car(MainBase):

    name: Mapped[str] = mapped_column(name="name_car", type_=String(250), nullable=True, index=True)
    body_type: Mapped[str] = mapped_column(name="body_type", type_=Enum(BodyType), nullable=True)
    #Question
    body_dimensions: Mapped[str] = mapped_column(name="body_dimensions", type_=Enum(BodyDimension), nullable=True)
    car_registration_number: Mapped[int] = mapped_column(name="car_registration_number", type_=Integer, nullable=True)
    #Question
    car_brand_photo: Mapped[str] = mapped_column(name="car_brand_photo", type_=Text, nullable=True)
    #Question
    photo_car_passport_main: Mapped[str] = mapped_column(name="photo_car_passport_main", type_=Text, nullable=True)
    photo_car_passport_additional: Mapped[str] = mapped_column(name="photo_car_passport_additional",
                                                               type_=Text, nullable=True)
    trailer_brand: Mapped[str] = mapped_column(name="trailer_name", type_=String(200), nullable=False)
    trailer_registration_number: Mapped[int] = mapped_column(name="trailer_registration_number",
                                                             type_=Integer, nullable=False)
    photo_trailer_passport_main: Mapped[str] = mapped_column(name="photo_trailer_passport_main",
                                                             type_=Text, nullable=False)
    photo_trailer_passport_additional: Mapped[str] = mapped_column(name="photo_trailer_passport_additional",
                                                                   type_=Text, nullable=False)

    #Relation
    order: Mapped["Order"] = relationship("Order", back_populates="car")

    def __repr__(self):

        res_dict: Dict[str, str] = {
            f"{k}": f"{v}"
            for k,v in self.__dict__.items()
        }

        return str(res_dict)

    def __str__(self):
        return self.__str__()