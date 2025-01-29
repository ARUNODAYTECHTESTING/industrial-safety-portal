from django.contrib.auth.hashers import make_password, check_password

class PasswordManager:

    @staticmethod
    def hash_password(password):
        return make_password(password = password)