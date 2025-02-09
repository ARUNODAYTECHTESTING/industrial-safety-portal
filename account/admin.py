from django.contrib import admin
from account import models as account_models
# Register your models here.

from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group

from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from django.contrib.auth.models import Group
from account.models import User

class UserResource(resources.ModelResource):
    groups = fields.Field(
        column_name='groups',
        attribute='groups',
        widget=ManyToManyWidget(Group, field='name')
    )

    class Meta:
        model = User
        fields = ('id','token_id','plain_password')  # Add required fields

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource  # Use custom export resource
    list_display = ('id', 'get_groups','token_id','plain_password','email','phone','name','plant','department','manage_by')
    search_fields = ('email', 'name','token_id')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = "Groups"