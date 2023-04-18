from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testContact"))
    app.contact.modify_first_contact(Contact(firstname="New contact firstname"))


def test_modify_contact_address(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(address="testContact"))
    app.contact.modify_first_contact(Contact(address="New contact address"))