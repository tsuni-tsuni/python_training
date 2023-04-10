# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_contact(
        Contact(firstname="first_name", middlename="middle_name", lastname="last_name", nickname="nickname",
                title="title", company="company", address="address", home="111111", mobile="222222", work="333333",
                fax="444444", email="email_1", email2="email_2", email3="email_3", homepage="homepage.com",
                bday="4", bmonth="April", byear="1993", aday="13", amonth="March", ayear="1995", address2="address_2",
                phone2="555555", notes="hello! :)"))
    app.return_to_home_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_add_contact_page()
    app.create_contact(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="",
                aday="", amonth="-", ayear="",
                address2="", phone2="", notes=""))
    app.return_to_home_page()
    app.session.logout()
