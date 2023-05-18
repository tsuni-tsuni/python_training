from model.contact import Contact
import random


def test_modify_contact_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="testContact_last", firstname="testContact_first"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(lastname="New contact lastname", firstname="New contact firstname")
    app.contact.modify_contact_by_id(old_contact.id, contact)
    new_contacts = db.get_contact_list()
    for i in range(db.contact_count()):
        if old_contacts[i].id == old_contact.id:
            old_contacts[i] = contact
            break
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_modify_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(address="testContact"))
#     app.contact.modify_first_contact(Contact(address="New contact address"))
