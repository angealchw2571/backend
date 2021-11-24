from rest_framework import permissions


class ReviewUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #Check permision for read only request
            return True
        else:
            # Check permisson for write request
            # only if logged in user has the same username as this instance, 
            # which means this instance belongs to the user, then he/she can edit
            # or delete this profile.
            return obj.username == request.user.username