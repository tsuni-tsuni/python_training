from model.contact import Contact
import re
import random
import string
from random import randrange


def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname=generate_random_string(), firstname=generate_random_string(), address=generate_random_string(), home=generate_random_string(), email=generate_random_string()))
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(
        filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))

def generate_random_string():
    return ''.join([random.choice(string.ascii_letters) for i in range(random.randrange(20))])
