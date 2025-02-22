from rest_framework.permissions import BasePermission

from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class RoleManager:
    def __init__(self,user = None):
        self.user = user

    def is_admin(self):
        return self.user.groups.filter(name='Admin').exists()
    def is_auditor(self):
        return self.user.groups.filter(name='Auditor').exists()
    def is_super_admin(self):
        return self.user.groups.filter(name='Super Admin').exists()
    def is_portal_admin(self):
        return self.user.groups.filter(name='Portal Admin').exists()


class IsPortalAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_portal_admin()
       
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_super_admin()
       
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_admin()
        else:
            return True
class IsAuditor(BasePermission):
    def has_permission(self, request, view):
        return RoleManager(request.user).is_auditor()





class PermissionManager:
    def __init__(self, user=None):
        self.user = user
        self.user_permissions = self._get_user_permissions()
        print(f"user belongs to group: {self.user_permissions}")

    def _get_user_permissions(self):
        if not self.user:
            return []
        return Permission.objects.filter(group__user=self.user).select_related('content_type')

    def has_model_permission(self, model, action):
        content_type = ContentType.objects.get_for_model(model)
        permission_codename = f"{action}_{model._meta.model_name}"
        print(f"check permissions for {permission_codename}")
        return self.user_permissions.filter(
            content_type=content_type,
            codename=permission_codename
        ).exists()

    def has_object_permission(self, obj, action):
        """Check if user has permission to perform action on specific object"""
        # First check if user has model-level permission
        if not self.has_model_permission(obj.__class__, action):
            return False
        
        # Check if user is owner of the object
        if hasattr(obj, 'user'):
            return obj.user == self.user
        elif hasattr(obj, 'created_by'):
            return obj.created_by == self.user
        elif hasattr(obj, 'owner'):
            return obj.owner == self.user
            
        # If no ownership field found, fallback to model-level permission
        return True

    def check_permission(self, model, action, obj=None):
        # Check model-level permission first
        if not self.has_model_permission(model, action):
            raise PermissionDenied(f"No {action} permission for {model._meta.model_name}")
        
        # If object is provided, check object-level permission
        # if obj is not None and not self.has_object_permission(obj, action):
        #     raise PermissionDenied(f"No {action} permission for this specific {model._meta.model_name}")
            
        return True

class DynamicModelPermission(BasePermission):
    def has_permission(self, request, view):
        action_map = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete'
        }
        model = view.queryset.model
        action = action_map.get(request.method, '')
        
        permission_manager = PermissionManager(request.user)
        return permission_manager.check_permission(model, action)

    def has_object_permission(self, request, view, obj):
        action_map = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete'
        }
        action = action_map.get(request.method, '')
        
        permission_manager = PermissionManager(request.user)
        return permission_manager.check_permission(obj.__class__, action, obj)

