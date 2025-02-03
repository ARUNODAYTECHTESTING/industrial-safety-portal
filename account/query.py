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
    def get_user_by_id(self, user_id: str):
        return account_models.User.objects.filter(id=user_id).first()
class TokenQuery(account_interface.ITokenizer):

    def generate_token(self,user:account_models.User) -> str:
        token,status = Token.objects.get_or_create(user=user)
        return token.key

class GroupQuery(account_interface.IGroup):
    def get_user_type_level(self,user,user_type=None):
        if user.groups.filter().first().name == 'Portal Admin':
            user_type = Group.objects.filter(name__in = ['Super Admin', 'Admin', 'Auditor']).values("id","name")
        elif user.groups.filter().first().name == 'Super Admin':
            user_type = Group.objects.filter(name__in = ['Admin', 'Auditor']).values("id","name")
        elif user.groups.filter().first().name == 'Admin':
            user_type = Group.objects.filter(name__in = ['Auditor']).values("id","name")
        else:
            user_type = "You are Auditor there is no sublevel"
        return user_type
    def get_user_role(self,user):
        return user.groups.filter().first().name