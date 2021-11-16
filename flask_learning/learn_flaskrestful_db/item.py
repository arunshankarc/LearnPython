import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

# Each class is a resource to be returned back to user
class Item(Resource):
    TABLE_NAME = 'items'
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from items where name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        cursor.close()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': f"Item '{name}' not found"}, 404

    @jwt_required()
    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.req_parser.parse_args()

        item = {'name': name, 'price': data['price']}

        try:
            Item.insert(item)
        except Exception:
            return {"message": "An error occurred inserting the item."}

        return item

    @jwt_required()
    def delete(self, name):
        item = self.find_by_name(name)
        if item is None:
            return {'message': 'Item not found'}
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"DELETE FROM {self.TABLE_NAME} WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}

    @jwt_required()
    def put(self, name):
        data = Item.req_parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                Item.insert(updated_item)
            except Exception:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                Item.update(updated_item)
            except Exception:
                return {"message": "An error occurred updating the item."}
        return updated_item

    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"UPDATE {cls.TABLE_NAME} SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"INSERT INTO {cls.TABLE_NAME} VALUES(?, ?)"
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"SELECT * FROM {cls.TABLE_NAME} WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}


class ItemList(Resource):
    TABLE_NAME = 'items'
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = f"SELECT * FROM {self.TABLE_NAME}"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        cursor.close()
        connection.close()

        return {'items': items}
