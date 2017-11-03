from passlib.hash import pbkdf2_sha256  # from the passlib docs
from myapp.models.user import User


class Dashboard:
    def __init__(self):
        self.registry = dict()
        self.is_logged_in = False

    def signup(self, name, email, password):
        has_been_registered = False
        user = User(name, email, pbkdf2_sha256.hash(password))
        if user and user.email not in self.registry:
            self.registry[user.email] = user
            has_been_registered = True
        return has_been_registered

    def login(self, email, password):
        if email not in self.registry:  # if user is not yet registered...
            return False

        if pbkdf2_sha256.verify(password, self.registry[email].password):
            self.is_logged_in = True
            return True
        return False

    def logout(self):
        is_logged_out = False
        if self.is_logged_in:  # for a user to logout, they must be logged in
            is_logged_out = True
        return is_logged_out
