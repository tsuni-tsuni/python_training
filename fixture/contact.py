from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        if not (wd.current_url.endswith("/addressbook/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # ph = wd.find_element_by_name("photo")
        # action = webdriver.common.action_chains.ActionChains(wd)
        # action.move_to_element_with_offset(ph, 5, 5)
        # action.click()
        # action.perform()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("C:\\fakepath\\uspeha_psihologiya.jpg")
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
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        # init contact creation
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        l = self.count()
        self.select_contact_by_id(id)
        # open modification form
        checkbox = wd.find_elements_by_name("selected[]")
        for i in range(l):
            if checkbox[i].get_attribute('checked'):
                wd.find_elements_by_xpath("//img[@title='Edit']")[i].click()
                break
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//input[@name='update']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (((wd.current_url.endswith("/addressbook/")) or (
        wd.current_url.endswith("/addressbook/index.php"))) and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home page").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text_last = element.find_element_by_xpath("./td[2]").text
                text_first = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                self.contact_cache.append(Contact(id=id, lastname=text_last, firstname=text_first, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contacts_info_from_edit_page(self):
        wd = self.app.wd
        l = self.count()
        contacts = []
        for i in range(l):
            self.open_contact_to_edit_by_index(i)
            id = wd.find_element_by_name("id").get_attribute("value")
            firstname = wd.find_element_by_name("firstname").get_attribute("value")
            lastname = wd.find_element_by_name("lastname").get_attribute("value")
            address = wd.find_element_by_name("address").get_attribute("value")
            home = wd.find_element_by_name("home").get_attribute("value")
            mobile = wd.find_element_by_name("mobile").get_attribute("value")
            work = wd.find_element_by_name("work").get_attribute("value")
            phone2 = wd.find_element_by_name("phone2").get_attribute("value")
            email = wd.find_element_by_name("email").get_attribute("value")
            email2 = wd.find_element_by_name("email2").get_attribute("value")
            email3 = wd.find_element_by_name("email3").get_attribute("value")
            contacts.append(
                Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                        home=home, mobile=mobile, work=work, phone2=phone2,
                        email=email, email2=email2, email3=email3))
        return contacts


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text)
        mobile = re.search("M: (.*)", text)
        work = re.search("W: (.*)", text)
        phone2 = re.search("P: (.*)", text)
        return Contact(home=self.str_is_none(home), mobile=self.str_is_none(mobile), work=self.str_is_none(work), phone2=self.str_is_none(phone2))

    def get_contacts_from_view_page(self):
        wd = self.app.wd
        l = self.count()
        contacts = []
        for i in range(l):
            self.open_contact_to_view_by_index(i)
            text = wd.find_element_by_id("content").text
            home = re.search("H: (.*)", text)
            mobile = re.search("M: (.*)", text)
            work = re.search("W: (.*)", text)
            phone2 = re.search("P: (.*)", text)
            contacts.append(Contact(home=self.str_is_none(home), mobile=self.str_is_none(mobile), work=self.str_is_none(work), phone2=self.str_is_none(phone2)))
        return contacts

    def str_is_none(self, s):
        if s:
            return s.group(1)
        else:
            return ""
