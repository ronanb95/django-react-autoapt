from rest_framework.permissions import SAFE_METHODS, BasePermission

class ListingEditPermission(BasePermission):
    
    message = 'Editing listings is restricted to the authoring landlord only.'
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        return obj.landlord == request.user or request.user.is_superuser