from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        if not (wd.current_url.endswith("/addressbook/edit.php") and len(wd.find_elements(By.NAME, "submit")) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # ph = wd.find_element(By.NAME, "photo")
        # action = webdriver.common.action_chains.ActionChains(wd)
        # action.move_to_element_with_offset(ph, 5, 5)
        # action.click()
        # action.perform()
        # wd.find_element(By.NAME, "photo").clear()
        # wd.find_element(By.NAME, "photo").send_keys("C:\\fakepath\\uspeha_psihologiya.jpg")
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.bday)
        self.change_dropdown_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_dropdown_value("aday", contact.aday)
        self.change_dropdown_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # init contact creation
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.XPATH, "//input[@name='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # self.select_contact_by_index(index)
        # open modification form
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.XPATH, "//input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        l = self.count()
        self.select_contact_by_id(id)
        # open modification form
        checkbox = wd.find_elements(By.NAME, "selected[]")
        for i in range(l):
            if checkbox[i].get_attribute('checked'):
                wd.find_elements(By.XPATH, "//img[@title='Edit']")[i].click()
                break
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.XPATH, "//input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def select_contact_in_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (((wd.current_url.endswith("/addressbook/")) or (
                wd.current_url.endswith("/addressbook/index.php"))) and len(
            wd.find_elements(By.NAME, "searchstring")) > 0):
            wd.find_element(By.LINK_TEXT, "home page").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.XPATH, "//tr[@name='entry']"):
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                text_last = element.find_element(By.XPATH, "./td[2]").text
                text_first = element.find_element(By.XPATH, "./td[3]").text
                address = element.find_element(By.XPATH, "./td[4]").text
                all_emails = element.find_element(By.XPATH, "./td[5]").text
                all_phones = element.find_element(By.XPATH, "./td[6]").text
                self.contact_cache.append(Contact(id=id, lastname=text_last, firstname=text_first, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        home = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contacts_info_from_edit_page(self):
        wd = self.app.wd
        l = self.count()
        contacts = []
        for i in range(l):
            self.open_contact_to_edit_by_index(i)
            id = wd.find_element(By.NAME, "id").get_attribute("value")
            firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
            lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
            address = wd.find_element(By.NAME, "address").get_attribute("value")
            home = wd.find_element(By.NAME, "home").get_attribute("value")
            mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
            work = wd.find_element(By.NAME, "work").get_attribute("value")
            phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
            email = wd.find_element(By.NAME, "email").get_attribute("value")
            email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
            email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
            contacts.append(
                Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                        home=home, mobile=mobile, work=work, phone2=phone2,
                        email=email, email2=email2, email3=email3))
        return contacts

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text)
        mobile = re.search("M: (.*)", text)
        work = re.search("W: (.*)", text)
        phone2 = re.search("P: (.*)", text)
        return Contact(home=self.str_is_none(home), mobile=self.str_is_none(mobile), work=self.str_is_none(work),
                       phone2=self.str_is_none(phone2))

    def get_contacts_from_view_page(self):
        wd = self.app.wd
        l = self.count()
        contacts = []
        for i in range(l):
            self.open_contact_to_view_by_index(i)
            text = wd.find_element(By.ID, "content").text
            home = re.search("H: (.*)", text)
            mobile = re.search("M: (.*)", text)
            work = re.search("W: (.*)", text)
            phone2 = re.search("P: (.*)", text)
            contacts.append(
                Contact(home=self.str_is_none(home), mobile=self.str_is_none(mobile), work=self.str_is_none(work),
                        phone2=self.str_is_none(phone2)))
        return contacts

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact)
        dropdown = Select(wd.find_element(By.NAME, 'to_group'))
        dropdown.select_by_value(group)
        group_name = dropdown.first_selected_option.text
        wd.find_element(By.NAME, 'add').click()
        wd.find_element(By.LINK_TEXT, 'group page "%s"' % (group_name)).click()

    def open_group_view_page_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        dropdown = Select(wd.find_element(By.NAME, 'group'))
        dropdown.select_by_value(id)

    def get_contacts_info_from_group_view_page(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements(By.XPATH, "//tr[@name='entry']"):
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            text_last = element.find_element(By.XPATH, "./td[2]").text
            text_first = element.find_element(By.XPATH, "./td[3]").text
            address = element.find_element(By.XPATH, "./td[4]").text
            all_emails = element.find_element(By.XPATH, "./td[5]").text
            all_phones = element.find_element(By.XPATH, "./td[6]").text
            contacts.append(Contact(id=id, lastname=text_last, firstname=text_first, address=address,
                                    all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return contacts

    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        dropdown = Select(wd.find_element(By.NAME, 'group'))
        dropdown.select_by_value(group)
        # group_name = dropdown.first_selected_option.text
        self.select_contact_in_group_by_id(contact)
        wd.find_element(By.NAME, 'remove').click()
        # wd.find_element(By.LINK_TEXT, 'group page "%s"' % (group_name)).click()

    def str_is_none(self, s):
        if s:
            return s.group(1)
        else:
            return ""
