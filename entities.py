from datetime import date

class Phone:
    def __init__(self, number):
        self._number = number

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, new_number):
        if len(new_number) < 12:
            raise Exception('Number should be in full-form: +79999999999')
        self._number = new_number
    def to_dict(self):
        return {'number': self.number}
    def __str__(self):
        return f'{self.number}'

class Contact:
    id: int
    Username: str
    GivenName: str
    FamilyName: str
    phone: Phone
    email: str
    birthdate: date
    def __str__(self):
        return f'Contact: id - {self.id}'
    def to_dict(self):
        return {
            'id': self.id,
            'Username': self.Username,
            'GivenName': self.GivenName,
            'FamilyName': self.FamilyName,
            'phone': self.phone.to_dict() if self.phone else None,
            'email': self.email,
            'birthdate': self.birthdate.isoformat() if self.birthdate else None
        }

class Group:
    id: int
    title: str
    description: str
    contacts: list[Contact]
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'contacts': self.contacts
        }