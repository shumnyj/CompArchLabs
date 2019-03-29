from myOut import *


def num_inp():
    """
    Функція num_inp заповнює поле, вимагаючи введення числових даних

    :return: integer number converted from input
    """
    field = None
    while field is None:
        try:
            field = int(input())
        except ValueError:
            print("Please enter a number")
            field = None
    return field


def new_entry():
    """
    Функція new_entry додає книгу у домашню бібліотеку

    :return: new entry formed with respective keys
    """
    en = dict.fromkeys(['title', 'author', 'barcode', 'pages', 'read'])
    print("enter book title")
    en["title"] = input()
    print("enter book author")
    en["author"] = input()
    print("enter book barcode")
    en['barcode'] = num_inp()
    print("enter number of pages in book")
    en['pages'] = num_inp()
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


def entry_search(key, entries):
    """
    Функція entry_search приймає ключ key за яким ведеться пошук та повертає список знайдених по введеному значенню книг
    :param key: key by which search in library will be conducted
    :param entries: library
    :return: list of entries with value in key field that equals entered one (value)

    >>> entries = [ {'title': 'a'} ]
    >>> entry_search(None, entries)
    Error: Invalid Key
    []
    >>> entry_search("title", [])
    Current library is empty
    []
    """
    if not entries:
        print('Current library is empty')
        return []
    if key is not None:
        found = []
        print('Enter search value')
        if key == 'barcode':
            value = num_inp()
        else:
            value = input()
        for en in entries:
            if en[key] == value:
                found.append(en)
        if not found:  # мда
            return []
        return found
    else:   # quit to menu
        print('Error: Invalid Key')  # не викликається окремо, тому в теорії гілка не спрацює
        return []


def find_entries(entries):
    """
    Функція find_entries шукає книгу у списку домашньої бібліотеки за вхідними ключами (назва, автор або штрих-код)
    :param entries: list of library entries
    :return: list of found entries (just in case)

    >>> find_entries([])
    Current library is empty
    []
    >>> find_entries(1231)
    Traceback (most recent call last):
      ...
    TypeError: Parameter is not list
    """
    if entries and entries != [] and type(entries) == list:
        print('Search by: 1: title;  2:author;'
              '  3: barcode;  Enter 0 to cancel')
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
            found = entry_search(key, entries)
            for en in found:
                entry_out(en)
            print(str(len(found)) + ' entries found in current library')
        else:   # quit to menu
            return []
    elif type(entries) != list:
        raise TypeError("Parameter is not list")
    else:
        print("Current library is empty")
        return []
    return found


def remove_entry(entries):
    """
    Функція remove_entry анігілює книгу з списку домашньої бібліотеки за вхідними ключами (назва або штрих-код)
    :param entries: list of library entries
    :return: None

    >>> remove_entry([])
    Current library is empty
    []
    >>> remove_entry()
    Traceback (most recent call last):
      ...
    TypeError: remove_entry() missing 1 required positional argument: 'entries'
    >>> remove_entry(15243)
    Traceback (most recent call last):
      ...
    TypeError: Parameter is not list
    """
    if entries and entries != [] and type(entries) == list:
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
            found = entry_search(key, entries)
            if not found:
                print('No such books found')
            else:
                for en in found:
                    entries.remove(en)
                print(str(len(found)) + ' entry(s) removed')
    elif type(entries) != list:
        raise TypeError("Parameter is not list")
    else:
        print("Current library is empty")
        return []
    return found


if __name__ == "__main__":
    import doctest
    doctest.testmod()
