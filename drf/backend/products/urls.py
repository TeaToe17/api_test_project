from django.urls import path

from .views import ProductDetailAPIView
from .views import ProductDeleteAPIView
from .views import ProductListCreateAPIView
from .views import ProductUpdateAPIView
from .views import ProductMixinView
from .views import product_alt_view

urlpatterns = [
    path("",ProductListCreateAPIView.as_view(),name="product-list"),
    path("<int:pk>/",ProductDetailAPIView.as_view(),name="product-detail"),
    path("<int:pk>/update/",ProductUpdateAPIView.as_view(),name="product-edit"),
    path("<int:pk>/delete/",ProductDeleteAPIView.as_view()),
    # path("<int:pk>/",product_alt_view),
    # path("",ProductMixinView.as_view()),
    # path("<int:pk>/",ProductMixinView.as_view()),
    # path("",product_alt_view),
] 