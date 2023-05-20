import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def group_count(self):
        # cursor = self.connection.cursor()
        # try:
        #     cursor.execute("select count(*) from group_list")
        #     res = cursor.fetchone()
        #     num = res[0]
        # finally:
        #     cursor.close()
        num = len(self.get_group_list())
        return num

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def contact_count(self):
        num = len(self.get_contact_list())
        return num

    def get_contacts_in_all_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append({'id': str(id), 'group_id': str(group_id)})
        finally:
            cursor.close()
        return list

    def get_contacts_in_group_list(self, group):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where group_id='%s'" % group)
            for row in cursor:
                (id, group_id) = row
                list.append({'id': str(id), 'group_id': str(group_id)})
        finally:
            cursor.close()
        return list

    def contacts_in_all_groups_count(self):
        num = len(self.get_contacts_in_all_groups_list())
        return num

    def contacts_in_group_count(self, group):
        num = len(self.get_contacts_in_group_list(group))
        return num

    def destroy(self):
        self.connection.close()
