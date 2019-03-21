from flask import Flask, jsonify, request, abort
import json
app = Flask(__name__)

entries = []
filename = 'library_data.json'

@app.route('/', methods=['GET'])
def send_libr():
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
    if not request.json:
        abort(400)
    entries = request.json
    with open(filename, 'w') as libfile:
        json.dump(entries, libfile, indent=4)
        libfile.close()
   
   #print(entries)
    return jsonify(entries), 201
if __name__ == '__main__':
    app.run(debug=True)
