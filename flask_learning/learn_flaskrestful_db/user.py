import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, user_id, username, password):
        self._id = user_id
        self._username = username
        self._password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_user):
        self._username = new_user

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from users where username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from users where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user


class UserRegister(Resource):
    req_parser = reqparse.RequestParser()
    req_parser.add_argument(
        'username',
        type=str,
        required=True,
        help="username field mandatory!"
    )
    req_parser.add_argument(
        'password',
        type=str,
        required=True,
        help="password field mandatory!"
    )

    @classmethod
    def post(cls):
        input_data = UserRegister.req_parser.parse_args()
        if User.find_by_username(input_data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "insert into users values (NULL, ?, ?)"
        cursor.execute(query, (input_data['username'], input_data['password']))
        connection.commit()
        cursor.close()
        connection.close()
        return {'message': 'User created successfully'}, 201
