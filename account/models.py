from django.db import models
from shared import models as shared_models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from equipment import models as equipment_models
# Create your models here.


class Department(shared_models.TimeStamp):
    name = models.CharField(max_length=64,unique=True)


class UserType(shared_models.TimeStamp):
    name = models.CharField(max_length=64)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=16,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token_id = models.PositiveBigIntegerField(null=True,max_length=5,unique=True)
    name = models.CharField(max_length=64)
    user_type = models.ForeignKey(UserType,on_delete=models.SET_NULL, null = True, related_name="user")
    plant = models.ForeignKey(equipment_models.Plant, on_delete=models.SET_NULL, null = True, related_name="user")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null =True, related_name="user")
    manage_by = models.ForeignKey('self', on_delete=models.SET_NULL, null =True, related_name="user")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        permissions = [
            ('can_delete_super_admin', 'Can delete super admin'),
            ('can_delete_admin', 'Can delete admin'),
        ]