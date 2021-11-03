# safer way of comparing string considering encoding
from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user is not None and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    userid = payload.get('identity')
    print(payload)
    return User.find_by_id(userid)
