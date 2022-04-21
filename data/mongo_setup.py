from mongoengine import register_connection


def global_init():
    register_connection(alias='core', name='contacts_api')
