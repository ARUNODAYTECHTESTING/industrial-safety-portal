from rest_framework.permissions import BasePermission

class IsPortalAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.groups.filter(name='Portal Admin').exists()
        else:
            return True
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.groups.filter(name='Super Admin').exists()
        else:
            return True
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()

class IsAuditor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Auditor').exists()



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
    