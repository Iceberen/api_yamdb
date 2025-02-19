from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated
            and (request.user.role==MODERATOR or request.user.role==ADMIN)
        )  # не совсем понимаю как тут сделать проверку на модератора и админа
        # может быть можно сделать методы типа встроенного is_authenticated


class IsAdminModeratorOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role==MODERATOR
            or request.user.role==ADMIN
            or obj.author == request.user
        )
