from rest_framework.permissions import BasePermission


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

class PermissionManager(RoleManager):
    def __init__(self,user = None):
        super().__init__(user)
   
    def has_permission(self,permission):
        if permission == 'create':
            return self.is_admin() or self.is_super_admin() or self.is_portal_admin()

class IsPortalAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_portal_admin()
        else:
            return True
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_super_admin()
        else:
            return True
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return RoleManager(request.user).is_admin()
        else:
            return True
class IsAuditor(BasePermission):
    def has_permission(self, request, view):
        return RoleManager(request.user).is_auditor()

