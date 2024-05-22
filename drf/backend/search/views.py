from rest_framework import generics
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerializer


from .client import perform_search

class SearchListView(generics.GenericAPIView):
    def get(self,request):
        query = request.GET.get("q")
        tag = request.GET.get("tag")
        if not query:
            return Response("",status=400)
        results  = perform_search(query,tags=tag)
        return Response(results)


class SearchOldListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get("q")
        results = Products.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q,user = user)
        return results