# from django.shortcuts import render
import json
from products.models import Products

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request,*args,**kwargs):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
        # print(serializer.data)
        # data = serializer.data
        # return Response(data)