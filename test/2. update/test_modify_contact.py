from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_add_contact_page()
        app.contact.create(Contact(firstname="testContact"))
        app.open_home_page()
    app.contact.modify_first_contact(Contact(firstname="New contact firstname"))
    app.contact.return_to_home_page()


def test_modify_contact_address(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.open_add_contact_page()
        app.contact.create(Contact(address="testContact"))
        app.open_home_page()
    app.contact.modify_first_contact(Contact(address="New contact address"))
    app.contact.return_to_home_page()