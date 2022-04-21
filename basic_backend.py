"""basic_backend.py: simple CRUD backend to store inventory items"""

__author__ = "Silvia Nittel"
__copyright__ = "Copyright 2022, SIE508, University of Maine"
__credits__ = ["Silvia Nittel"]

import mvc_exceptions as mvc_exc
import csv

item_type = "product"

# Function reads specified file and outputs a list ##
def read_inv():
    with open("current_inv.txt", 'r') as file:
        items = []
        temp = csv.DictReader(file)
        for row in temp:
            items.append(row)
    return items


## Function writes list to specified file ##
def write_inv(items):
    with open("current_inv.txt", 'w', newline='') as file:
        headers = ['name', 'price', 'quantity']
        csv_file = csv.DictWriter(file, fieldnames=headers)
        csv_file.writeheader()
        csv_file.writerows(items)
        print("Inventory Updated!")


# create item, add it to file
def create_item(name, price, quantity):
    # reference list created from reading file
    items = read_inv()
    # search first if that item already exists
    results = list(filter(lambda x: x['name'] == name, items))
    # if we find an existing item with the name, we raise an exception
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
    # if not, we append the item to the dictionary
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})
        # appended dictionary is written to file
        write_inv(items)


# bulk create times
def create_items(app_items):
    items = app_items
    write_inv(items)


# read a particular item
def read_item(name):
    items = read_inv()
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(name))


# read all items
def read_items():
    items = read_inv()
    return [item for item in items]


# update item in file
def update_item(name, price, quantity):
    items = read_inv()
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
        write_inv(items)
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t update "{}" because it\'s not stored'.format(name))


# delete item from file
def delete_item(name):
    items = read_inv()
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    # print("index items", idxs_items)
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        print("idxs_items[0][0], idxs_items[0][1]: ", idxs_items[0][0], " item in list, value:", idxs_items[0][1])
        del items[i]
        write_inv(items)
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t delete "{}" because it\'s not stored'.format(name))


def main():
    my_items = [
        {'name': 'bread', 'price': 2.5, 'quantity': 20},
        {'name': 'milk', 'price': 4.0, 'quantity': 10},
        {'name': 'eggs', 'price': 4.0, 'quantity': 5},
        {'name': 'juice', 'price': 5.75, 'quantity': 10},
        {'name': 'cake', 'price': 10.0, 'quantity': 2},
    ]

    ########################################################
    ## Statements to show functionality of program ##

    # Insert/create new item to the file #
    # create_item('apples', 1.55, 13)

    # Update item in the file #
    # update_item('apples', 1.0, 5)

    # Delete item from the file #
    # delete_item('apples')

    ########################################################

    # # CREATE #
    create_items(my_items)
    # create_item('eggs', price=10.0, quantity=15)

    # # if we try to re-create an object we get an ItemAlreadyStored exception
    # try:
    #     create_item('wine', price=10.0, quantity=10)
    # except Exception as e:
    #     print(e)
    #     exit()

    # # READ
    # print('READ items')
    # print(read_items())
    # # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ meat')
    # print(read_item('meat'))
    # print('READ bread')
    # print(read_item('bread'))

    # # UPDATE
    # print('UPDATE bread')
    # update_item('bread', price=2.0, quantity=30)
    # update_item('milk',price=20.0, quantity=24)
    # print(read_item('bread'))
    # # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # # DELETE
    # print('DELETE wine')
    # delete_item('eggs')
    # # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    # print('READ items')
    # print(read_items())


if __name__ == '__main__':
    main()