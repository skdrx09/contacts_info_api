from typing import List, Optional
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
import uvicorn
from data.mongo_setup import global_init
from data.Contact import Contact, ContactUpdateRequest


app = FastAPI()
global_init()


db = []


'''async def add_contact(f_name: str, l_name: str, gender: str) -> Contact:
    # n_contact = Contact()
    n_contact.f_name = f_name
    n_contact.l_name = l_name
    n_contact.gender = gender

    n_contact.save()

    return n_contact'''


@app.get("/")
async def read_root():
    return "Welcome to contacts_info_api!\n\nPlease visit /contacts/ path for listing your contacts, or the /docs/ " \
           "path for seeing all available options and supported HTTP methods. "


@app.get("/contacts/")
async def add_contact(f_name: str, l_name: str, gender: str) -> Contact:
    n_contact = Contact()
    n_contact.f_name = f_name
    n_contact.l_name = l_name
    n_contact.gender = gender

    n_contact.save()

    return n_contact


'''async def add_contact(contact: Contact):
    new_id = uuid4()            # Generates a random UUID  
    contact.id = new_id
    db.append(contact)
    return "id:", contact.id'''


@app.post("/contacts/")
async def add_contact(n_contact: Contact) -> Contact:
    n_contact.save()
    return n_contact


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
