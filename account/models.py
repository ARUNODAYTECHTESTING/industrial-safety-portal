from django.db import models
from shared import models as shared_models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from equipment import models as equipment_models
import random
# Create your models here.


class Department(shared_models.TimeStamp):
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return f"{self.id}-{self.name}"
  
    def save(self, *args, **kwargs):
        obj = Department.objects.filter().last()
        if obj:
            self.id = obj.id + 1
        super().save(*args, **kwargs)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=16,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token_id = models.PositiveBigIntegerField(null=True,max_length=5,unique=True)
    name = models.CharField(max_length=64)
    plant = models.ForeignKey(equipment_models.Plant, on_delete=models.SET_NULL, null = True,blank=True,related_name="user")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null =True,blank=True,related_name="user")
    manage_by = models.ForeignKey('self', on_delete=models.SET_NULL, null =True,blank=True,related_name="user")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.id}-{self.email}"
    
    class Meta:
        permissions = [
            ('can_add_portal_admin', 'Can add portal admin'),
            ('can_delete_portal_admin', 'Can delete portal admin'),
            ('can_view_portal_admin', 'Can view portal admin'),
            ('can_change_portal_admin', 'Can chnage portal admin'),

            ('can_add_super_admin', 'Can add super admin'),
            ('can_delete_super_admin', 'Can delete super admin'),
            ('can_view_super_admin', 'Can view super admin'),
            ('can_change_super_admin', 'Can chnage super admin'),

            ('can_add_admin', 'Can add admin'),
            ('can_delete_admin', 'Can delete admin'),
            ('can_view_admin', 'Can view admin'),
            ('can_change_admin', 'Can chnage admin'),

            ('can_add_auditor', 'Can add auditor'),
            ('can_delete_auditor', 'Can delete auditor'),
            ('can_view_auditor', 'Can view auditor'),
            ('can_change_auditor', 'Can chnage auditor'),

        ]

    def save(self, *args, **kwargs):
        # obj = User.objects.filter().last()
        # if obj:
        #     self.id = obj.id + 1
        if not self.token_id:
            self.token_id = random.randint(100000, 999999)
        super().save(*args, **kwargs)