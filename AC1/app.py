from flask import Flask, jsonify, request, abort
import json
app = Flask(__name__)


@app.route('/', methods=['GET'])
def send_libr():
    """
    Функція що відправляє всі дані бібліотеки на клієнт при запиті
    :return: list of dictionaries with library
    """
    try:
        with open(filename, 'r') as libfile:
            entries = json.load(libfile)
            libfile.close()
    except FileNotFoundError:
        print('\n File not found, creating new empty one')
        entries = []
    return jsonify(entries)


@app.route('/', methods=['POST'])
def update_libr():
    """
    Функція що отримує запит з даними на запис оновленої бібліотеки і записує її в json
    :return: list of updated data and response code
    """
    if not request.json:
        abort(400)
    entries = request.json
    with open(filename, 'w') as libfile:
        json.dump(entries, libfile, indent=4)
        libfile.close()
    # print(entries)
    return jsonify(entries), 201


entries = []
filename = 'library_data.json'
if __name__ == '__main__':
    app.run(debug=True)
