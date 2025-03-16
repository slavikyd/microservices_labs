import random
import string
from datetime import date, timedelta
from entities import Phone, Group, Contact


def random_string(length=8):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def random_phone_number():
    """Generate a random phone number in the format +79999999999."""
    return f"+79{random.randint(100000000, 999999999)}"

def random_date(start_date=date(1950, 1, 1), end_date=date.today()):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_contact():
    """Generate a random Contact instance."""
    contact = Contact()
    contact.id = random.randint(1, 1000)
    contact.Username = random_string()
    contact.GivenName = random_string()
    contact.FamilyName = random_string()
    contact.phone = random_phone()
    contact.email = f"{random_string()}@example.com"
    contact.birthdate = random_date()
    return contact

def random_phone():
    """Generate a random Phone instance."""
    phone = Phone(random_phone_number())
    #phone.number = 
    return phone

def random_group():
    """Generate a random Group instance."""
    group = Group()
    group.id = random.randint(1, 1000)
    group.title = random_string()
    group.description = random_string(20)
    group.contacts = [random.randint(1, 1000) for _ in range(random.randint(1, 10))]
    return group

def generate_random_instances():
    """Generate a random set of instances of Phone, Contact, and Group."""
    phones = [random_phone() for _ in range(5)]
    contacts = [random_contact() for _ in range(5)]
    groups = [random_group() for _ in range(5)]
    return phones, contacts, groups
