from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, address=None, id=None,
                 home=None, mobile=None, work=None, phone2=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None,
                 nickname=None, title=None, company=None, fax=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s: %s, %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and ((self.lastname == other.lastname) or (self.lastname is None and other.lastname == "") or (self.lastname == "" and other.lastname is None)) and ((self.firstname == other.firstname) or (self.firstname is None and other.firstname == "") or (self.firstname == "" and other.firstname is None)) #\
            #and ((self.home == other.home) or (self.home is None and other.home == "") or (self.home == "" and other.home is None)) and ((self.work == other.work) or (self.work is None and other.work == "") or (self.work == "" and other.work is None)) and ((self.mobile == other.mobile) or (self.mobile is None and other.mobile == "") or (self.mobile == "" and other.mobile is None)) and ((self.phone2 == other.phone2) or (self.phone2 is None and other.phone2 == "") or (self.phone2 == "" and other.phone2 is None))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
