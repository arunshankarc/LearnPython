from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


# Boiler plate
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'run'
jwt = JWT(app, authenticate, identity) # /auth
api = Api(app)

items = []

# Each class is a resource to be returned back to user
class Item(Resource):
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'message': f"Item '{name}' not found"}, 404

    @jwt_required()
    def post(self, name):
        # Inside request.get_json() we can set to force=True or silent=True
        # but that will silence any issues like no input fields like input_data['price']
        # or if input header does not have Content-type to application/json
        for item in items:
            if item['name'] == name:
                return {'message': f'An item with name {name} already exists.'}, 400
        input_data = Item.req_parser.parse_args()
        item = {'name': name, 'price': input_data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
        if items and len(items) > 0:
            for item in items:
                if item['name'] == name:
                    items.remove(item)
                    return {'message': f'Item {name} removed'}
            return {'message': f'Item {name} does not exists'}
        return {'message': 'No items present/added yet.'}

    @jwt_required()
    def put(self, name):
        input_data = Item.req_parser.parse_args()
        for item in items:
            if item['name'] == name:
                item['price'] = input_data['price']
                return {'message': f"Item '{name}' updated with new price"}
        item = {'name': name, 'price': input_data['price']}
        items.append(item)
        return {'message': f"Item '{name}' added to item list."}


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'item': items}


api.add_resource(Item, '/item/<string:name>') # /item/chair
api.add_resource(ItemList, '/items') # /items
app.run(port=5000, debug=True)
