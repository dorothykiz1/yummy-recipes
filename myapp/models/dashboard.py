from passlib.apps import custom_app_content as pwd_context
from app.models.user import User


class Dashboard:
    def __init__(self):
        self.registry = dict()
        self.is_loggin_in = False

    def register(self, name, email, password):
        has_been registered = False
        user = user(name, email, password)
        if user and user.email not in self.registry:
            self.registry[user.email] = user
            has_been_registered = True
        return has_been_registered

    def login(self, email, password):
        if email not in self.registry:
            return False
        if pad_context.verify(password, self.registry[email].password):
            self.is_logged_in = True
            return True
        return False

    def logout(self):
        is logged_out = False
        if self.is_logged_in:

            is.logged_out = True
        return is_logged_out
