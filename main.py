from typing import List, Optional
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
import uvicorn
from data.models import Contact, Gender, ContactUpdateRequest
from data.mongo_setup import global_init
#from data.Contact import Contact, ContactUpdateRequest


app = FastAPI()
global_init()

db: List[Contact] = [
    Contact(
        id=UUID("339b4090-8ea9-4f68-b869-c79d051e1f3c"),
        f_name="Julieta",
        l_name="Roca",
        gender=Gender.female,
    ),
    Contact(
        id=UUID("ef6418dd-e5fe-4f21-8a34-dfda3dd8e0e5"),
        f_name="Sergio",
        l_name="Sanchez",
        gender=Gender.male,
    ),
    Contact(
        id=UUID("52ca3ed6-92d1-4276-b893-364a3f023f54"),
        f_name="Liliana",
        l_name="Fernandez",
        gender=Gender.male,
    )
]

'''def new_contact(f_name: str, l_name: str, gender: str) -> Contact:
    new_contact = Contact()
    new_contact.f_name = f_name
    new_contact.l_name = l_name
    new_contact.gender = gender

    new_contact.save()

    return new_contact'''


@app.get("/")
async def read_root():
    return "Welcome to contacts_info_api!\n\nPlease visit /contacts/ path for listing your contacts, or the /docs/ " \
           "path for seeing all available options and supported HTTP methods. "


@app.get("/contacts/")
async def list_contacts():
    return db


@app.post("/contacts/")
async def add_contact(contact: Contact):
    new_id = uuid4()    
    contact.id = new_id
    db.append(contact)
    return "id:", contact.id
    

@app.put("/contacts/{contact_id}")
async def update_contact(contact_update: ContactUpdateRequest, contact_id: UUID):
    found_id = 0
    for contact in db:
        if contact.id == contact_id:
            found_id += 1
            if contact_update.new_f_name is not None:
                contact.f_name = contact_update.new_f_name
            if contact_update.new_l_name is not None:
                contact.l_name = contact_update.new_l_name
            if contact_update.new_gender is not None:
                contact.gender = contact_update.new_gender
        continue
    if found_id != 0:
        return
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Contact with id: {contact_id} doest not exist"
        )


@app.delete("/contacts/{contact_id}")
async def del_contact(contact_id: UUID):
    for contact in db:
        if contact.id == contact_id:
            db.remove(contact)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Contact with id: {contact_id} doest not exist"
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
