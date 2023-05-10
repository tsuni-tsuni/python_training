from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["num of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "  # * 10 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 32))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                    mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-",
                    byear="", aday="", amonth="-", ayear="", address2="", phone2="", notes="")] + \
           [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_string("home", 10), mobile=random_string("", 10),
                    work=random_string("", 10), fax=random_string("", 10), email=random_string("", 10),
                    email2=random_string("", 10), email3=random_string("", 10), homepage=random_string("", 10),
                    bday=random_day(), bmonth="-", byear=random_string("", 10), aday=random_day(), amonth="-",
                    ayear=random_string("", 10), address2=random_string("", 10), phone2=random_string("", 10),
                    notes=random_string("notes", 10))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
