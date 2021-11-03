# safer way of comparing string considering encoding
from werkzeug.security import safe_str_cmp
from user import User


users = [User(1, "bob", 'asdf')]
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user is not None and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    userid = payload.get('identity')
    print(payload)
    return userid_mapping.get(userid, None)
