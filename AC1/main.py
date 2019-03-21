# import os
import json
import requests

# функція num_inp заповнює поле, вимагаючи введення числових даних
def num_inp(field):
    while field is None:
        try:
            field = int(input())
        except ValueError:
            print("Please enter a number")
            field = None
    return field


# функція new_entry додає книгу у домашню бібліотеку
def new_entry():
    en = dict.fromkeys(['title', 'author', 'barcode', 'pages', 'read'])
    print("enter book title")
    en["title"] = input()
    print("enter book author")
    en["author"] = input()
    print("enter book barcode")
    en['barcode'] = num_inp(en['barcode'])
    print("enter number of pages in book")
    en['pages'] = num_inp(en['pages'])
    print("have you read this book Y/N?")
    en["read"] = input().lower()
    if en["read"] == 'y' or en["read"] == 'yes':
        en["read"] = True
    elif en["read"] == 'n' or en["read"] == 'no':
        en["read"] = False
    else:
        print("Bad value")  # no check because field is not that important
        en["read"] = None
    #    os.system('cls' if os.name == 'nt' else 'clear')
    return en


# функція entry_out виводить книгу з домашньої бібліотеки; параметр en - це елемент списку котрий виводиться
def entry_out(en):
    # for val in en.values():
    #    print(val)
    print('{title:<20}|{author:<20}|{barcode:<14d}|{pages:<5d}|{read!s:<}'.format(**en))  # TODO add indexes?
    return


# функція library_out виводить домашню бібліотеку
def library_out():
    if len(entries) != 0:
        print('{:<3}|{:<20}|{:<20}|{:<14}|{:<5}|{:<}'.format('№', 'Book title', 'Author', 'Barcode', 'Pages', 'Is read'))
        print('_'*73)
        for ind, en in enumerate(entries):
            print('{:<3}|'.format(ind), end=' ')
            entry_out(en)
    else:
        print('No entries in this library at the time')
    return


# функція find_entries шукає книгу у списку домашньої бібліотеки за вхідними ключами (назва, автор або штрих-код)
def find_entries():
    print('Search by: 1: title;  2:author;  3: barcode;  Enter 0 to cancel')
    key = input()
    if key == '1' or key.lower() == 'title':
        key = 'title'
    elif key == '2' or key.lower() == 'author':
        key = 'author'
    elif key == '3' or key.lower() == 'barcode':
        key = 'barcode'
    elif key == '0':
        key = None
    else:
        print('Wrong search parameter')
        key = None
    if key is not None:
        found = entry_search(key)
        for en in found:
            entry_out(en)
        print(str(len(found)) + ' entries found in current library')
    else:   # quit to menu
        return
    # TODO Maybe partial search
    return


# функція entry_search приймає ключ key за яким ведеться пошук та повертає список знайдених по введеному значенню книг
def entry_search(key):
    if key is not None:
        found = []
        print('Enter search value')
        value = input()
        if key == 'barcode':
            while not value.isdecimal():
                print("Please enter only digits")
                value = input()
            value = int(value)
        for en in entries:
            if en[key] == value:
                found.append(en)
        if not found:  # мда
            return []
        return found
    else:   # quit to menu
        print('Error: Invalid Key')  # не викликається окремо, тому в теорії гілка не спрацює
        return []


# функція remove_entry анігілює книгу з списку домашньої бібліотеки за вхідними ключами (назва або штрих-код)
def remove_entry():
    print('Delete by: 1: title;  2: barcode;  Enter 0 to cancel')
    key = input()							# key choose
    if key == '1' or key.lower() == 'title':
        key = 'title'
    elif key == '2' or key.lower() == 'barcode':
        key = 'barcode'
    elif key == '0':
        key = None
    else:
        print('Wrong search parameter')
        key = None
    if key is not None:
        found = entry_search(key)
        if not found:
            print('No such books found')
        else:
            for en in found:
                entries.remove(en)
            print(str(len(found)) + ' entry(s) removed')


entries = []
filename = 'library_data.json'
print("Welcome to home library")

"""
try:
    with open(filename, 'r') as libfile:
        entries = json.load(libfile)
        libfile.close()
except FileNotFoundError:
    print('\n File not found, creating new empty one')
    entries = [] 
"""

entries = requests.get('http://127.0.0.1:5000/').json()


while True:
    print('\n0: Save and Quit;  1: Show book list;  2: Add new book;  3: Fi1d books;  4: Remove book')
    state = None
    while state is None:
        try:
            state = int(input())
        except ValueError:
            print("Please enter a number")
            state = None
    if state == 0:
        break
    elif state == 1:
        library_out()
    elif state == 2:
        entries.append(new_entry())
    elif state == 3:
        find_entries()
    elif state == 4:
        remove_entry()
r = requests.post(url='http://127.0.0.1:5000/', json=entries)

"""
with open(filename, 'w') as libfile:
    json.dump(entries, libfile, indent=4)
    libfile.close() 
"""

print("Terminating program....")
