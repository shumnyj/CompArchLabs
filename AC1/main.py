import os


def new_entry():
    en = dict.fromkeys(['title', 'author', 'barcode', 'pages', 'read'])
    print("enter book title")
    en["title"] = input()
    print("enter book author")
    en["author"] = input()
    print("enter book barcode")
    while en["barcode"] is None:
        try:
            en["barcode"] = int(input())
        except ValueError:
            print("Please enter a number")
            en["barcode"] = None
    print("enter number of pages in book")
    while en["pages"] is None:
        try:
            en["pages"] = int(input())
        except ValueError:
            print("Please enter a number")
            en["pages"] = None
    print("have you read this book Y/N?")
    en["read"] = input()
    if en["read"] == 'Y':
        en["read"] = True
    elif en["read"] == 'N':
        en["read"] = False
    else:
        print("Bad value")  # no cycle because field is not that important
        en["read"] = None
    #    os.system('cls' if os.name == 'nt' else 'clear')
    return en


def entry_out(en):
    # for val in en.values():
    #    print(val)
    print('{title:<20}|{author:<20}|{barcode:<14d}|{pages:<5d}|{read!s:<}'.format(**en))  # TODO add indexes?
    return


def library_out():
    if len(entries) != 0:
        print('{:<20}|{:<20}|{:<14}|{:<5}|{:<}'.format('Book title', 'Author', 'Barcode', 'Pages', 'Is read'))
        print('_'*70)
        for en in entries:
            entry_out(en)
    else:
        print('No entries in this library at the time')
    return


def find_entries():
    print('Search by:', end=' ')
    print('1: title;  2:author;  3: barcode;  Enter 0 to cancel')
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
    count = 0
    if key is not None:
        print('Enter search value')
        value = input()
        if key == 'barcode':
            while not value.isdecimal():
                print("Please enter only digits")
                value = input()
            value = int(value)
        for en in entries:
            if en[key] == value:
                entry_out(en)
                count += 1
        print(str(count) + ' entries found in current library')
    else:   # quit to menu
        return
    # TODO Maybe partial search
    return


def remove_entry():
    # TODO Remove with index shifting
    return


i = 0
entries = []

print("Welcome to home library")
# TODO Read JSON
while True:
    print('\n0: Quit;  1: Show book list;  2: Add new book;  3: Find books;  4: Remove book')
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
    enumerate(entries)
    # TODO add file update
print("Terminating program....")


