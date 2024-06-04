#System
from typing import Annotated, Union, List
from datetime import datetime

#Other libraries
from pydantic import BaseModel, Field


class CustomerBase(BaseModel):

    com_name: Annotated[str, Field(max_length=350)]
    status: Annotated[bool, Field(default=False)]
    inn: Annotated[int, Field()]
    ogrn: Annotated[int, Field()]
    kpp: Annotated[int, Field()]
    checking_account: Annotated[bool, Field()]
    correpondent_account: Annotated[bool, Field(default=False)]
    bic: Annotated[str, Field(max_length=650)]
    actual_address: Annotated[str, Field(max_length=400)]
    legal_address: Annotated[str, Field(max_length=400)]
    date_registration: Annotated[datetime.utcnow, Field(default=datetime.utcnow())]
    date_foundation: Annotated[datetime.utcnow, Field(default=datetime.utcnow())]
    total_orders: Annotated[int, Field(default=0)]
    completed_orders: Annotated[int, Field(default=0)]
    rating: Annotated[int, Field(default=0)]