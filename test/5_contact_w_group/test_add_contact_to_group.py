from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    if len(contacts) == 0:
        app.contact.create(Contact(lastname="testContact_last", firstname="testContact_first"))
        contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="testGroup"))
        groups = db.get_group_list()
    group = random.choice(groups)
    old_list = db.get_contacts_in_group_list(group.id)
    contact = random.choice(contacts)
    if any(d['id'] == contact.id for d in old_list):
        app.contact.create(Contact(lastname="testContact_last", firstname="testContact_first"))
        contacts = db.get_contact_list()
        contact = max(contacts, key=id)
    old_list = db.get_contacts_in_group_list(group.id)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_list = db.get_contacts_in_group_list(group.id)
    if not any(d['id'] == contact.id and d['group_id'] == group.id for d in old_list):
        old_list.append({'id': contact.id, 'group_id': group.id})
    assert sorted(old_list, key=lambda k: k['id']) == sorted(new_list, key=lambda k: k['id'])
