from model.contact import Contact
import random
import string
from random import randrange


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home=generate_random_phone(), mobile=generate_random_phone(), work=generate_random_phone(), phone2=generate_random_phone()))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def generate_random_phone():
    return ''.join([random.choice(string.digits) for i in range(random.randrange(11))])
