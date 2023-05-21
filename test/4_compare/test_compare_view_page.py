from model.contact import Contact
import random
import string
from random import randrange


def test_phones_on_contact_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(home=generate_random_phone(), mobile=generate_random_phone(), work=generate_random_phone(), phone2=generate_random_phone()))
    contacts = db.get_contact_list()
    contacts_from_view_page = app.contact.get_contacts_from_view_page()
    contacts_from_edit_page = app.contact.get_contacts_info_from_edit_page()
    assert len(contacts) == len(contacts_from_view_page) and len(contacts) == len(contacts_from_edit_page)
    for i in range(len(contacts)):
        s = contacts_from_view_page[i].home
        assert contacts_from_view_page[i].home == contacts_from_edit_page[i].home
        assert contacts_from_view_page[i].mobile == contacts_from_edit_page[i].mobile
        assert contacts_from_view_page[i].work == contacts_from_edit_page[i].work
        assert contacts_from_view_page[i].phone2 == contacts_from_edit_page[i].phone2


def generate_random_phone():
    return ''.join([random.choice(string.digits) for i in range(random.randrange(11))])
