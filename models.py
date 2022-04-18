from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str, Enum):                # Accepts only two gender options
    male = "male"
    female = "female"


class Contact(BaseModel):               # DataBase model class
    id: Optional[UUID] = uuid4()        # Generates a random id number
    f_name: str
    l_name: str
    gender: Gender                      # gender is of Gender class type (male/female)


class ContactUpdateRequest(BaseModel):
    new_f_name: Optional[str]
    new_l_name: Optional[str]
    new_gender: Optional[Gender]  
