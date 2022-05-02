from data.mongo_setup import global_init
from data.Contact import Contact, ContactUpdateRequest
from mongoengine.errors import ValidationError
from uuid import UUID
from mongoengine import QuerySet, UUIDField


global_init()


def new_contact(f_name: str, l_name: str, sex: str) -> Contact:
    n_contact = Contact()
    n_contact.f_name = f_name
    n_contact.l_name = l_name
    n_contact.gender = sex

    n_contact.save()

    return n_contact


def del_contact(key: UUIDField()):
    for contact in Contact.objects():
        print(contact.id)
        if contact.id == key:
            print("THIS WOULD DELETE THE DOCUMENT")
        else:
            print("NO MATCHING DOC ID FOUND")
    return


def query_contacts():
    for contact in Contact.objects.only('id'):
        print(contact.f_name, contact.l_name, contact.gender)
    # query = QuerySet(collection='my_db', document='contacts')
    # print(query.all_fields())


while True:
    print("\nWelcome to the local test API For interacting with MongoDB Atlas!\n")
    print("What would you like to do?"
          "\n1 - Query    (GET)"
          "\n2 - Write    (POST)"
          "\n3 - Update   (PUT)"
          "\n4 - Delete   (DELETE)")
    action = input("\n> ")

    if action == '1':
        print()
        query_contacts()
        input()
    elif action == '2':
        name = input('\nEnter name: ')
        surname = input('Enter last name: ')
        gender = input('Enter gender: ')
        print('Attempting to save contact info...')
        new_contact(name, surname, gender)
        print('Contact info successfully saved!')

    elif action == '3':
        pass
    elif action == '4':
        del_key = input("Enter the key of the contact you wish to delete: ")
        print(type(del_key))
        print(del_key)
        del_contact(del_key)
        input()




