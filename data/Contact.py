from mongoengine import *
import datetime


class ContactDB:                                                      # DataBase model class
    id = UUIDField                                                    # Generates a random id number
    registered_date = DateTimeField(default=datetime.datetime.now)
    f_name = StringField(required=True)
    l_name = StringField(required=True)
    gender = StringField(required=False)                              # gender is of Gender class type (male/female)

    meta = {                                                          # Mongodb stuff
        'db_alias': 'core',
        'collection': 'contacts'
    }

