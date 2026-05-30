from collections import UserDict
import re

class Field(UserDict):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Ствоорення класу Name, який є обов'язковим полем для контакту (не може бути порожнім) та успадковує Field
class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value.strip())

# Створення класу Phone, який успадковує Field та має валідацію для телефонного номера (наприклад, 10 цифр)
class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

# Необов'язкове поле Email з валідацією формату електронної пошти
class Email(Field):
    def __init__(self, value):
        # Прроста валідація формату email за допомогою регулярного виразу
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format.")
        super().__init__(value)

# Клас Record для зберігання інформації про контакт, який містить ім'я, список телефонів та список email
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.emails = []  # Список для зберігання email адрес, оскільки контакт може мати кілька email
    # керування телефонів (додавання, видалення, редагування)
    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_phone_number, new_phone_number):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_number:
                self.phones[i] = Phone(new_phone_number)
                return True
        return False
        
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    # керування Email (додавання, видалення, редагування)
    def add_email(self, email_address):
        email = Email(email_address)
        self.emails.append(email)

    def remove_email(self, email_address):
        for email in self.emails:
            if email.value == email_address:
                self.emails.remove(email)
                return True
        return False

    def edit_email(self, old_email, new_email):
        for i, email in enumerate(self.emails):
            if email.value == old_email:
                self.emails[i] = Email(new_email)
                return True
        return False

    def __str__(self):
        phones_str = '; '.join(p.value for p in self.phones) if self.phones else "None"
        emails_str = '; '.join(e.value for e in self.emails) if self.emails else "None"
        return f"Contact name: {self.name.value}, Phones: {phones_str}, Emails: {emails_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    # Універсальний пошук по імені, телефону та email
    def search(self, query):
        query = query.lower()
        results = []
        
        for record in self.data.values():
            # Перевіряємо ім'я на відповідність запиту (ігноруємо регістр)
            if query in record.name.value.lower():
                results.append(record)
                continue
            
            # Перевіряємо телефони  на відповідність запиту (ігноруємо регістр) та підтримуємо частковий пошук
            phone_match = any(query in phone.value for phone in record.phones)
            if phone_match:
                results.append(record)
                continue
                
            # Перевіряємо email на відповідність запиту (ігноруємо регістр) та підтримуємо частковий пошук
            email_match = any(query in email.value.lower() for email in record.emails)
            if email_match:
                results.append(record)
                continue
                
        return results

# Приклад використання класу AddressBook та Record для демонстрації функціоналу пошуку та керування контактами
if __name__ == "__main__":

    address_book = AddressBook()
    # Створюємо запис для контакта "John"
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_email("john@example.com")
    address_book.add_record(john_record)
    # Створюємо запис для контакта "Alice"
    alice_record = Record("Alice")
    alice_record.add_phone("0987654321")
    alice_record.add_email("alice@example.com")
    address_book.add_record(alice_record)
    # Виводимо всі записи
    for record in address_book.data.values():
        print(record)  
    # Пошук по імені
    print("\nSearch results for 'John':")   
    for record in address_book.search("John"):
        print(record)
    # Пошук по телефону
    print("\nSearch results for '0987':")
    for record in address_book.search("0987"):
        print(record)
    # Пошук по email
    print("\nSearch results for 'example.com':")
    for record in address_book.search("example.com"):
        print(record)
    # Видалення контакта
    address_book.delete("John")
    print("\nAfter deleting 'John':")
    for record in address_book.data.values():
        print(record)
    # Редагування контакта
    alice_record.edit_phone("0987654321", "5555555555") 
    alice_record.edit_email("alice@example.com", "alice.new@example.com")
    print("\nAfter editing 'Alice':")
    for record in address_book.data.values():
        print(record)
    query = "5552"
    print(f"\nSearch results for '{query}':")
    for record in address_book.search(query):
        print(record)