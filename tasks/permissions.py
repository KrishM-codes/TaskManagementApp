from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admin users to
    access it.
    """

    def has_permission(self, request, view):
        """
        Allows viewing all tasks only for admin users.
        """
        if request.method == "GET" and request.user.is_staff:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Allows access if the task belongs to the user or if the user is an
        admin.
        """
        return request.user == obj.user or request.user.is_staff
