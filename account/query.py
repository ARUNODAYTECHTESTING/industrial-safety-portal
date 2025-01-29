from account import interface as account_interface
from account import models as account_models
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token


class DepartmentRepository(account_interface.IDepartment):
    def get_all_departments(self):
        return account_models.Department.objects.all()
    
    def add_department(self, department: str):
        return account_models.Department.objects.create(name = department)

class UserQuery(account_interface.IUser):
    def add_user(self):
        pass
    
    def get_user_by_token_id(self, token_id: str):
        return account_models.User.objects.filter(token_id=token_id).first()

class TokenQuery(account_interface.ITokenizer):

    def generate_token(self,user:account_models.User) -> str:
        token,status = Token.objects.get_or_create(user=user)
        return token.key