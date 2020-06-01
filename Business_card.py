from faker import Faker
fake = Faker("pl_PL")

class Card:

    def __init__(self, first_name, last_name, company, position, email, phone) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
        self.phone = phone


        def __str__(self) -> str:
            return f"{self.first_name} {self.last_name}, {self.phone}, {self.email}"

        def __repr__(self) -> str:
            return f"Card(first_name={self.first_name} last_name={self.last_name},phone={self.phone}, tel_priv={self.tel_priv}, email_address={self.email})"

        def contact(self):
            return f"Wybieram number: {self.phone}, tel_priv={self.tel_priv}, i dzwonię do  {self.first_name} {self.last_name}, position - {self.position}, email - {self.email}) "


class BaseContact(Card):
    def __init__(self, tel_priv, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_priv = tel_priv

    def base_contact(self):
        return f"Wybieram number telefonu prywatnego: {self.tel_priv}, i dzwonię do  {self.first_name} {self.last_name}, email - {self.email}) "

    @property
    def label_length(self):
        return f"Długość imenia i nazwiska: {sum([len(self.first_name), len(self.last_name)])}"

persona_1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email=fake.email(), phone=fake.phone_number(), tel_priv=fake.phone_number())


class BusinessContact(Card):

    def business_contact(self):
        return f"Wybieram number: {self.phone}, i dzwonię do  {self.first_name} {self.last_name}, position - {self.position}, email - {self.email}) "

    @property
    def label_length(self):
        return f"Długość imenia i nazwiska: {sum([len(self.first_name), len(self.last_name)])}"

persona_2 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email=fake.email(), phone=fake.phone_number())


print(persona_1.base_contact())                       # Base Contact
print(persona_1.label_length)                         # Długość znaków
print(persona_2.business_contact())                   # Business Contact
print(persona_2.label_length)                         # Długość znaków
