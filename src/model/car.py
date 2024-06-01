#System
from typing import Dict, List

#Other libraries
from sqlalchemy import String, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

#Local
from src.model.base import Base


class Car(Base):

    name: Mapped[str] = mapped_column(name="name_car", type_=String(250), nullable=True, index=True)
    body_type: Mapped[str] = mapped_column(name="body_type", type_=String(150), nullable=True)
    #Question
    body_dimensions: Mapped[str] = mapped_column(name="body_dimensions", type_=String(150), nullable=True)
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
    workload_car: Mapped[bool] = mapped_column(type_=Boolean, name="workload_car", default=False, nullable=False)
    id_carrier: Mapped[int] = mapped_column(ForeignKey("Carrier.id"), name="id_carrier")

    #Relations
    carrier: Mapped["Carrier"] = relationship(back_populates="car_carrier", uselist=False)
    order: Mapped[List["Order"]] = relationship(back_populates="car", uselist=True)

    def __repr__(self):

        res_dict: Dict[str, str] = {
            f"{k}": f"{v}"
            for k,v in self.__dict__.items()
        }

        return str(res_dict)

    def __str__(self):
        return self.__str__()