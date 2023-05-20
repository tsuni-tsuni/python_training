from model.group import Group
from model.contact import Contact
import random


def test_del_contact_from_group(app, db):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    if len(contacts) == 0:
        app.contact.create(Contact(lastname="testContact_last", firstname="testContact_first"))
        contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="testGroup"))
        groups = db.get_group_list()
    old_list = db.get_contacts_in_all_groups_list()
    if old_list == []:
        contact = random.choice(contacts)
        group = random.choice(groups)
        app.contact.add_contact_to_group(contact.id, group.id)
        old_list = db.get_contacts_in_all_groups_list()
    contact_in_group = random.choice(old_list)
    old_list = db.get_contacts_in_group_list(contact_in_group['group_id'])
    app.contact.delete_contact_from_group(contact_in_group['id'], contact_in_group['group_id'])
    new_list = db.get_contacts_in_group_list(contact_in_group['group_id'])
    old_list.remove(contact_in_group)
    assert sorted(old_list, key=lambda k: k['id']) == sorted(new_list, key=lambda k: k['id'])
