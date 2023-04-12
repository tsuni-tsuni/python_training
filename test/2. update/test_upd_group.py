from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="grName_1", header="grHeader_1", footer="grFooter_1"))
    app.session.logout()