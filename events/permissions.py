from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.role) == 'ADMIN'

class IsOrganizer(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.role) == 'ORGANIZER'

class IsAttendee(permissions.BasePermission):
    def has_permission(self, request, view):
        return str(request.user.role) == 'ATTENDEE'
