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
