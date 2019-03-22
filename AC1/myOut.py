def entry_out(en):
    """
    Функція entry_out виводить в консоль дані про книгу з домашньої бібліотеки;
    :param en: single entry from library
    :return: None

    >>> entry_out({'author': 'aaa2', 'barcode': 457574654, 'pages': 34, 'read': True, 'title': 'erer'})
    erer                |aaa2                |457574654     |34   |True
    >>> entry_out(dict.fromkeys(['title', 'author', 'barcode', 'pages', 'read']));
    Traceback (most recent call last):
     ...
    TypeError: unsupported format string passed to NoneType.__format__
    >>> entry_out(1);
    Traceback (most recent call last):
      ...
    TypeError: format() argument after ** must be a mapping, not int
    >>> entry_out();
    Traceback (most recent call last):
      ...
    TypeError: entry_out() missing 1 required positional argument: 'en'
    >>> entry_out({'ttt': 2, 'bbb': 'a', 'title': 'aw'})
    Traceback (most recent call last):
      ...
    KeyError: 'author'
    """
    # for val in en.values():
    #    print(val)
    print('{title:<20}|{author:<20}|{barcode:<14d}|{pages:<5d}|{read!s:<}'.format(**en))
    return


#
def library_out(entries):
    """
    функція library_out виводить всю поточну домашню бібліотеку в вікно консолі як таблицю
    :param entries: list of entry dicts
    :return: None

    >>> library_out([])
    No entries in this library at the time
    >>> library_out([{'author': 'aaa2', 'barcode': 457574654, 'pages': 34, 'read': True, 'title': 'erer'}])
    №  |Book title          |Author              |Barcode       |Pages|Is read
    _________________________________________________________________________
    0  | erer                |aaa2                |457574654     |34   |True
    >>> library_out(4)
    Traceback (most recent call last):
     ...
    TypeError: object of type 'int' has no len()
    >>> library_out()
    Traceback (most recent call last):
     ...
    TypeError: library_out() missing 1 required positional argument: 'entries'
    """
    if len(entries) != 0:
        print('{:<3}|{:<20}|{:<20}|{:<14}|{:<5}|{:<}'.format('№', 'Book title', 'Author', 'Barcode', 'Pages', 'Is read'))
        print('_'*73)
        for ind, en in enumerate(entries):
            print('{:<3}|'.format(ind), end=' ')
            entry_out(en)
    else:
        print('No entries in this library at the time')
    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()
