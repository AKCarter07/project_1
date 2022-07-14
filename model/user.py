class User:
    def __init__(self, username, password, fname, lname, email, role):
        self.user_id = 0
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.role = role

    def set_user_id(self, uid):
        self.user_id = uid

    def to_dict(self):
        return {
            'user id': self.user_id,
            'username': self.username,
            'first name': self.fname,
            'last name': self.lname,
            'email': self.email,
            'role': self.role
        }




    