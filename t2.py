from Utils.decorator import dec_log

class Contact:

    @dec_log('C:\\Users\\Александр\\PycharmProjects\\HW_2.4.2')
    def __init__(self, name, surname, number, favorites=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        self.add_info = kwargs
        if favorites:
            self.favorites = 'да'
        else:
            self.favorites = 'нет'

    def __str__(self):
        contact_data = 'Имя: {}\nФамилия: {}\nТелефон: {}\n' \
                       'В избранных: {}\nДополнительная информация:\n'.format(self.name, self.surname, self.number, self.favorites)
        for adv_info_key, adv_info_value in self.add_info.items():
            contact_data += '\t {}: {} \n'.format(adv_info_key, adv_info_value)
        return contact_data


class PhoneBook:

    def __init__(self, name_phone_book):
        self.name = name_phone_book
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def print_all_contacts(self):
        for contact in self.contacts:
            print(contact)

    def del_contact_by_number(self, number):
        for contact in self.contacts[:]:
            if contact.number == number:
                self.contacts.remove(contact)

    def print_favorites_contacts(self):
        for contact in self.contacts:
            if contact.favorites == 'Да':
                print(contact)

    def search_by_name(self, name, surname=''):
        for contact in self.contacts:
            if name == contact.name:
                print(contact)
            elif surname == contact.surname:
                print(contact)


if __name__ == "__main__":
    phone_book1 = PhoneBook('Телефонная книга')

    phone_book1.add_contact(Contact('Ivan', 'Ivanov', '+79051231234', telegram='@ivanka', email='ivanov.i@mail.ru'))
    phone_book1.add_contact(Contact('Petr', 'Petrenko', '+79051234567', favorites=True, telegram='@petrushka'))
    phone_book1.add_contact(Contact('Sergio', 'Italiano', '+10958785412',  email='factor@gmail.com'))

    phone_book1.print_all_contacts()

    phone_book1.del_contact_by_number('+79051234567')

    phone_book1.print_favorites_contacts()

    phone_book1.search_by_name('Ivan', 'Ivanov')