from data.mongo_setup import global_init
from data.Contact import Contact, ContactUpdateRequest


global_init()

def new_contact(f_name: str, l_name: str, gender: str) -> Contact:
    new_contact = Contact()
    new_contact.f_name = f_name
    new_contact.l_name = l_name
    new_contact.gender = gender

    new_contact.save()
    

    return new_contact



while True:
    name = input('Enter name: ')
    surname = input('Enter last name: ')
    gender = input('Enter gender: ')
    print('say sumthin pls')
    new_contact(name, surname, gender)