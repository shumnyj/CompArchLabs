# import json
import requests
from myManage import *
# from myOut import *

entries = []
connection = 'http://127.0.0.1:5000/'
# filename = 'library_data.json'

"""
try:
    with open(filename, 'r') as libfile:
        entries = json.load(libfile)
        libfile.close()
except FileNotFoundError:
    print('\n File not found, creating new empty one')
    entries = [] 
"""

try:
    entries = requests.get(connection).json()
    print("Welcome to home library")
    while True:
        print('\n0: Save and Quit;  1: Show book list;  2: Add new book;  3: Find books;  4: Remove book(s)')
        state = num_inp()
        if state == 0:
            break
        elif state == 1:
            library_out(entries)
        elif state == 2:
            entries.append(new_entry())
        elif state == 3:
            find_entries(entries)
        elif state == 4:
            remove_entry(entries)
    r = requests.post(url='http://127.0.0.1:5000/', json=entries)
    a = entries[1]
    if r.status_code == 201:
        print('Data sent to save successfully')
except requests.exceptions.ConnectionError:
    print('Connection Error, unable to connect to ' + connection)

"""
with open(filename, 'w') as libfile:
    json.dump(entries, libfile, indent=4)
    libfile.close() 
"""
print("Terminating program....")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
