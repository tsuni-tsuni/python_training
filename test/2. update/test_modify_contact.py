from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testContact"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New contact firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(address="testContact"))
#     app.contact.modify_first_contact(Contact(address="New contact address"))