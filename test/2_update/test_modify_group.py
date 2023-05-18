from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="testGroup"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = Group(name="New group name")
    app.group.modify_group_by_id(old_group.id, group)
    new_groups = db.get_group_list()
    for i in range(db.group_count()):
        if old_groups[i].id == old_group.id:
            old_groups[i] = group
            break
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(header="testGroup"))
#     app.group.modify_first_group(Group(header="New group header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
