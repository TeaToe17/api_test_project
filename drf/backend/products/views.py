from rest_framework import generics , mixins ,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404

from api.permissions import IsStaffEditorPermission , IsStaffListCreatePermission , IsStaffDeletePermission 
from api.mixins import StaffEditorPermissionMixin , UserQuerySetMixin
from .models import Products
from .serializers import ProductSerializer

class ProductDetailAPIView(
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPIView(
    generics.DestroyAPIView,
    # StaffEditorPermissionMixin
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]
    lookup_field = "pk"

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

class ProductUpdateAPIView(
    generics.UpdateAPIView,
    # StaffEditorPermissionMixin
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffEditorPermission]
    lookup_field = "pk"

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductListCreateAPIView(
    #This permission was nullified for viewing purposes of unauthenticated users
    # UserQuerySetMixin,
    # StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
    ):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsStaffListCreatePermission]

    def perform_create(self,serializer):
        request = self.request
        # print(serializer.validated_data)
        serializer.save(user = request.user)
    
    # def get_queryset(self,*args,**kwargs):
    #     qs = Products.objects.all()
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Products.objects.none()
    #     return qs.filter(user=user)

@api_view(["POST","GET"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Products,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
        
        queryset = Products.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content =  title
            serializer.save(content=content)
            print(serializer.data)
            return Response(serializer.data)
        
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def perform_create(self,serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content="testing content"
        serializer.save(content=content)