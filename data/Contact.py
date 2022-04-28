from mongoengine.fields import StringField, UUIDField, DateTimeField, EnumField
from mongoengine import Document
import datetime
from enum import Enum


class Gender(str, Enum):                # Accepts only two gender options
    male = "male"
    female = "female"


class ContactDB(Document):                                            # DataBase model class
    id = UUIDField                                                    # Generates a random id number
    registered_date = DateTimeField(default=datetime.datetime.now)
    f_name = StringField(required=True)
    l_name = StringField(required=True)
    gender = EnumField(Gender, required=False)                                        # gender is of Gender class type (male/female)

    meta = {                                                          # Mongodb stuff
        'db_alias': 'core',
        'collection': 'contacts'
    }


class ContactUpdateRequest(Document):
    new_f_name = StringField(required=False)
    new_l_name = StringField(required=False)
    new_gender = EnumField(Gender, required=False)
