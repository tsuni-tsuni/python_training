def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group()
    app.session.logout()