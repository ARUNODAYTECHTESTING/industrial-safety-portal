import os,json
from account import models as account_models
def update_user_bulk_password_from_json(file_path = None):
    if file_path is None:
        file_path = 'shared/dummy/users.json'
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    with open(file_path, 'r') as file:
        users = json.load(file)

    for user in users:
        try:
            user_obj = account_models.User.objects.get(email=user['email'])
            user_obj.plain_password = user['password']
            user_obj.save()
        except account_models.User.DoesNotExist:
            print(f"User with ID {user['id']} not found.")