# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.contact.open_add_contact_page()
    app.contact.create(
        Contact(firstname="first_name", middlename="middle_name", lastname="last_name", nickname="nickname",
                title="title", company="company", address="address", home="111111", mobile="222222", work="333333",
                fax="444444", email="email_1", email2="email_2", email3="email_3", homepage="homepage.com",
                bday="4", bmonth="April", byear="1993", aday="13", amonth="March", ayear="1995", address2="address_2",
                phone2="555555", notes="hello! :)"))
    app.contact.return_to_home_page()


def test_add_empty_contact(app):
    app.open_home_page()
    app.contact.open_add_contact_page()
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                aday="", amonth="-", ayear="",
                address2="", phone2="", notes=""))
    app.contact.return_to_home_page()
