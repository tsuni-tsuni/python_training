from model.contact import Contact


def test_update_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(
        Contact(firstname="first_name_1", middlename="middle_name_1", lastname="last_name_1", nickname="nickname_1",
                title="title_1", company="company_1", address="address_1", home="111111_1", mobile="222222_1", work="333333_1",
                fax="444444_1", email="email_1_1", email2="email_2_1", email3="email_3_1", homepage="homepage_1.com",
                bday="1", bmonth="January", byear="1901", aday="29", amonth="February", ayear="2020", address2="address_2_1",
                phone2="555555", notes="hello! :) updated contact"))
    app.contact.return_to_home_page()
    app.session.logout()