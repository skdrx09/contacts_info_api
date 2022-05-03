from data.mongo_setup import global_init
from data.Contact import Contact, ContactUpdateRequest
from mongoengine.errors import ValidationError
from uuid import UUID
from mongoengine import QuerySet, UUIDField
from typing import Optional
from fastapi import FastAPI
import uvicorn


app = FastAPI()
global_init()


@app.post("/contacts/")
async def new_contact(f_name: str, l_name: str, sex: str) -> Contact:
    n_contact = Contact()
    n_contact.f_name = f_name
    n_contact.l_name = l_name
    n_contact.gender = sex

    n_contact.save()

    return n_contact

# def update_contact(_id: UUID, n_f_name: Optional[str], n_l_name: Optional[str], n_gender: Optional[str]) -> Contact:


def update_contact(contact_id: UUID):
    if contact_id is not None:
        for ID in Contact.objects.only(id):
            print(ID)
            if contact_id == contact_id:
                pass
    return


def del_contact(key: UUID):
    for contact in Contact.objects():
        print(contact.id)
        if contact.id == key:
            print("THIS WOULD DELETE THE DOCUMENT")
        else:
            print("NO MATCHING DOC ID FOUND")
    return


@app.get("/contacts/")
async def query_contacts():
    '''for contact in Contact.objects:
        print(contact.f_name, contact.l_name, contact.gender)'''
    return Contact.objects.only(Contact.f_name)
    # query = QuerySet(collection='my_db', document='contacts')
    # print(query.all_fields())


'''while True:
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
        c_id = input("Enter the id of the contact you wish to update: ")
        update_contact(contact_id=c_id)
        input()

    elif action == '4':
        del_key = input("Enter the key of the contact you wish to delete: ")
        print(type(del_key))
        print(del_key)
        del_contact(del_key)
        input()
'''

if __name__ == "__main__":
    uvicorn.run("db_test:app", host="127.0.0.1", port=5000, log_level="info")
