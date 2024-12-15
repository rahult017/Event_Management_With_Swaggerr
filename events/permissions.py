from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN'

class IsOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ORGANIZER'

class IsAttendee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ATTENDEE'
