from model.contact import Contact
import re
import random
import string


def test_contact_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname=generate_random_string(), firstname=generate_random_string(), address=generate_random_string(), home=generate_random_string(), email=generate_random_string()))
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_edit_page = app.contact.get_contacts_info_from_edit_page()
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].lastname == contacts_from_edit_page[i].lastname
        assert contacts_from_home_page[i].firstname == contacts_from_edit_page[i].firstname
        assert contacts_from_home_page[i].address == contacts_from_edit_page[i].address
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_edit_page[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_edit_page[i])


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
