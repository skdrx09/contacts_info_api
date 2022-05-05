from mongoengine import connect
from data.Contact import Contact


connect(alias="my_db", host='mongodb+srv://admin:1346795@clusterunit01.ngqrj.mongodb.net/my_db?retryWrites=true&w=majority')

print("\nMini test program for testing db querying...\n")
db_contact = []
for data in Contact.objects:
    q_format = {}
    q_format['id'] = data.id  # DOES NOT WORK
    q_format['f_name'] = data.f_name
    q_format['l_name'] = data.l_name
    q_format['gender'] = data.gender
    db_contact.append(q_format)
print(db_contact)