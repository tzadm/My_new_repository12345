import pprint
import inspect


def introspection_info(abj):
    dict_ = {'type': '', 'attributes': [], 'methods': [], 'module': ''}
    dict_['type'] = f'{type(abj)}'[7:].strip("'>")
    dict_['module'] = inspect.getmodule(abj)

    for i in dir(abj):
        if callable(eval(f'abj.{i}')):
            dict_['methods'].append(i)
        else:
            dict_['attributes'].append(i)

    return dict_
class AddressBook:
    number_of_addresses = 0
    _streets = []
    _cities = []


    def __init__(self,city,street, house_number, apartment_number ):
        self.city = city
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number
        self.add_cities()
        self.add_streets()
        # self.number_of_addresses_sum()
        AddressBook.number_of_addresses += 1

    def add_cities(self):
        if self.city not in self._cities:
            self._cities.append(self.city)


    def add_streets(self):
        if self.street not in self._streets:
            self._streets.append(self.street)
    # @classmethod
    # def number_of_addresses_sum(cls):
    #     cls.number_of_addresses += 1


address_1 = AddressBook("Казань","Карбышева",56,34)
address_2 = AddressBook("Набережные Челны", "Гагарина", 12, 39)
qw = introspection_info(address_1)
pprint.pprint(qw)








