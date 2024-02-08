from rest_framework.permissions import IsAdminUser

class isAdminOrreadonly(IsAdminUser):
    def has_permission(self, request, view):
        admin = bool(request.user and request.user.is_staff)
        return request.method in ['GET', 'HEAD', 'OPTIONS'] or admin