from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask import jsonify
from flask_jwt import JWT

from user import UserRegister
from security import authenticate, identity
from item import Item, ItemList


app = Flask(__name__)
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.secret_key = 'run'
# Below line of code is added to change the default end point from
# auth to login
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity) # /auth

@jwt.error_handler
def customized_error_handler(error):
    return jsonify({
    'message': error.description,
    'code': error.status_code
 }), error.status_code

app.run(port=5000, debug=True)

api = Api(app)

api.add_resource(Item, '/item/<string:name>') # /item/chair
api.add_resource(ItemList, '/items') # /items
api.add_resource(UserRegister, '/register') # /register
