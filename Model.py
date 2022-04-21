#!/usr/bin/env python
__author__      = "Silvia Nittel"
__copyright__   = "SIE508, Copyright 2021, Orono, ME, USA"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "silvia.nittel@maine.edu"
__comments__ ="example is built using a MVC example by Giacomo Debidda (2017)"


import basic_backend
import mvc_exceptions as mvc_exc

class ModelBasic(object):

    def __init__(self, application_items):
        self._item_type = 'product'
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        try:
            return basic_backend.read_items()
        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise


    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)



def main():
    my_items = [
        {'name': 'bread', 'price': 2.5, 'quantity': 20},
        {'name': 'milk', 'price': 4.0, 'quantity': 10},
        {'name': 'eggs', 'price': 4.0, 'quantity': 5},
        {'name': 'juice', 'price': 5.75, 'quantity': 10},
        {'name': 'cake', 'price': 10.0, 'quantity': 2},
    ]

    model = ModelBasic(my_items)
    result = model.read_item("bread")
    print(result)

if __name__ == '__main__':
    main()