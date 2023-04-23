# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="first_name", middlename="middle_name", lastname="last_name", nickname="nickname",
                title="title", company="company", address="address", home="111111", mobile="222222", work="333333",
                fax="444444", email="email_1", email2="email_2", email3="email_3", homepage="homepage.com",
                bday="4", bmonth="April", byear="1993", aday="13", amonth="March", ayear="1995", address2="address_2",
                phone2="555555", notes="hello! :)")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                aday="", amonth="-", ayear="", address2="", phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)