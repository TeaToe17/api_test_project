from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.has_perm("products.change_products"):
            print("obj below")
            print(obj)
            return True
        return False
    
class IsStaffListCreatePermission(permissions.DjangoModelPermissions):

    def has_permission(self,request,view):
        user = request.user
        if user.is_staff:
            if user.has_perm("products.add_products"):
                return super().has_permission(request,view)
            elif user.get_all_permissions()==set():
                return False
            elif request.method in SAFE_METHODS:
                return True
    
class IsStaffDeletePermission(permissions.DjangoModelPermissions):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.has_perm("products.delete_products"):
            return True
        return False




# class IsStaffViewPermission(permissions.DjangoModelPermissions):

#     def has_permission(self,request,view):
#         user = request.user
#         if user.is_staff:
#             if user.has_perm("products.view_products"):
#                 print(request.method)
#                 print("using view perm")
#                 return True
#         return False

    # def has_permission(self,request,add):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_products"):
    #             return super().has_permission(request,add)
    #         return False
    #     return False

        # perms_map = {
    #     'GET': ['%(app_label)s.view_%(model_name)s'],
    #     'OPTIONS': [],
    #     'HEAD': [],
    #     'POST': ['%(app_label)s.add_%(model_name)s'],
    #     'PUT': ['%(app_label)s.change_%(model_name)s'],
    #     'PATCH': ['%(app_label)s.change_%(model_name)s'],
    #     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    # }

    # def has_permission(self,request,view):
    #     if not request.user.username == "user":
    #         return False
    #     if not request.user.is_staff:
    #         return False
    #     if not request.user.has_perm("products.view_products"):
    #         return False
    #     return super().has_permission(request,view)