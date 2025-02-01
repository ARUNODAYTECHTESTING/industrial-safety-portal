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
