from flask import Flask, jsonify, request


app = Flask(__name__)
stores = [
    {
        "name": "My wonderful store",
        "items": [
            {
                'name': 'My item', 
                'price': 15.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data.get('name'),
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store.get('name') == name:
            return jsonify(store)
    return {'message': f"store {name} not found"}


@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store.get('name') == name:
            new_item = {
                'name': request_data.get('name'),
                'price': request_data.get('price'),
            }
            store['items'].append(new_item)
            return jsonify({'message': 'New items added'})
    return jsonify({'message': f'Store {name} not found.'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
