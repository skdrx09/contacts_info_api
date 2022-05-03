from secrets import choice
from mongoengine.fields import StringField, UUIDField, DateTimeField, EnumField
from mongoengine import Document, ValidationError
import datetime
from enum import Enum
from typing import Optional


class Gender(str, Enum):                # Accepts only two gender options
    male = "male"
    female = "female"


GENDER = (("M", "Male"), ("F", "Female"))


def _not_empty(val):
    if not val:
        raise ValidationError('value can not be empty')


class Contact(Document):                                            # DataBase model class
    id = UUIDField                                                    # Generates a random id number
    registered_date = DateTimeField(default=datetime.datetime.now)
    f_name = StringField(required=True, validation=_not_empty)
    l_name = StringField(required=True, validation=_not_empty)
    # gender = EnumField(Gender, required=False)                                        # gender is of Gender class type (male/female)
    gender = StringField(required=False, choices=GENDER)

    meta = {                                                          # Mongodb stuff
        'db_alias': 'my_db',
        'collection': 'contacts'
    }


class ContactUpdateRequest(Document):
    new_f_name = StringField(required=False)
    new_l_name = StringField(required=False)
    new_gender = EnumField(Gender, required=False)
