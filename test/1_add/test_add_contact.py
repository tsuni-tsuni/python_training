# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " # * 10 + string.punctuation
    postfix = random.choice(string.ascii_letters)
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


def random_day():
    return str(random.randrange(1, 32))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-",
                    byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),
                       company=random_string("company", 10), address=random_string("address", 10), home=random_string("home", 10),
                       mobile=random_string("", 10), work=random_string("", 10), fax=random_string("", 10),
                       email=random_string("", 10), email2=random_string("", 10), email3=random_string("", 10),
                       homepage=random_string("", 10), bday=random_day(), bmonth="-",
                       byear=random_string("", 10),
                       aday=random_day(), amonth="-", ayear=random_string("", 10),
                       address2=random_string("", 10), phone2=random_string("", 10), notes=random_string("notes", 10))
               for i in range(3)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(firstname="first_name", middlename="middle_name", lastname="last_name", nickname="nickname",
    #                 title="title", company="company", address="address", home="111111", mobile="222222", work="333333",
    #                 fax="444444", email="email_1", email2="email_2", email3="email_3", homepage="homepage.com",
    #                 bday="4", bmonth="April", byear="1993", aday="13", amonth="March", ayear="1995", address2="address_2",
    #                 phone2="555555", notes="hello! :)")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
