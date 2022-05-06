from data.mongo_setup import global_init
from data.Contact import Contact, ContactUpdateRequest
from mongoengine.errors import ValidationError
from uuid import UUID
from mongoengine import queryset, UUIDField, connect, Document
from mongoengine import *
from typing import Optional
from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI()
db = global_init()


@app.get("/contacts/")
async def query_contacts():
    db_contact = []
    for data in Contact.objects:
        q_format = {'id': str(data.id),
                    'registered_date': data.registered_date,
                    'f_name': data.f_name,
                    'l_name': data.l_name,
                    'gender': data.gender
                    }

        db_contact.append(q_format)
    return db_contact


@app.post("/contacts/")
async def new_contact(f_name: str, l_name: str, sex: str) -> Contact:
    n_contact = Contact()
    n_contact.f_name = f_name
    n_contact.l_name = l_name
    n_contact.gender = sex

    n_contact.save()

    return n_contact

# def update_contact(_id: UUID, n_f_name: Optional[str], n_l_name: Optional[str], n_gender: Optional[str]) -> Contact:


# @app.put("/contacts/{contact_id}")
def update_contact(contact_update: ContactUpdateRequest, contact_id: str):
    if contact_id is not None:
        for contact in Contact.objects:
            if contact_id == str(contact.id):
                if contact_update.new_f_name is not None:
                    contact.f_name = contact_update.new_f_name
                if contact_update.new_l_name is not None:
                    contact.l_name = contact_update.new_l_name
                if contact_update.new_gender is not None:
                    contact.gender = contact_update.new_gender
                return
        raise HTTPException(
            status_code=404,
            detail=f"Contact with id: {contact_id} doest not exist"
        )
    return


@app.delete("/contacts/{contact_id}")
def del_contact(contact_id: str):
    for contact in Contact.objects():
        if str(contact.id) == contact_id:
            Contact.delete(contact)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Contact with id: {contact_id} doest not exist"
    )


def local_run():  # Test cases only
    print("\nWelcome to the local test API For interacting with MongoDB Atlas!\n")

    while True:
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
            n_contact = ContactUpdateRequest()
            n_contact.new_f_name = input("Enter new first name (if any): ")
            n_contact.new_l_name = input("Enter new last name (if any): ")
            n_contact.new_gender = input("Enter new gender (if any): ")

            update_contact(contact_update=n_contact, contact_id=c_id)
            input()

        elif action == '4':
            del_key = input("Enter the key of the contact you wish to delete: ")
            print(type(del_key))
            print(del_key)
            del_contact(del_key)
            input()


if __name__ == "__main__":
    # local_run()
    uvicorn.run("db_test:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
