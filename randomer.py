import random
import string
from datetime import date, timedelta
from entities import Phone, Group, Contact

def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_phone_number():
    return f"+79{random.randint(100000000, 999999999)}"

def random_date(start_date=date(1950, 1, 1), end_date=date.today()):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_phone():
    return Phone(random_phone_number())

def random_contact():
    contact = Contact()
    contact.id = random.randint(1, 1000)
    contact.Username = random_string()
    contact.GivenName = random_string()
    contact.FamilyName = random_string()
    contact.phone = random_phone()
    contact.email = f"{random_string()}@example.com"
    contact.birthdate = random_date()
    return contact

def random_group():
    group = Group()
    group.id = random.randint(1, 1000)
    group.title = random_string()
    group.description = random_string(20)
    group.contacts = [random_contact() for _ in range(random.randint(1, 10))]
    return group

