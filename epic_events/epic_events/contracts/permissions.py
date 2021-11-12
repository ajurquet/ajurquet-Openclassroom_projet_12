from rest_framework import permissions


class IsSaleEmployeeConnectedToTheContractOrReadOnly(permissions.BasePermission):
    message = "You can update a contract only if you're assigned to it"

    def has_permission(self, request, view):

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.client.sales_contact == request.user
