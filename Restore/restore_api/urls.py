from django.urls import include, path
from .views import (
    ProductListApiView,
    ShoppingCartListApiView,
    ShoppingCartItemListApiView,
)

app_name = "restore"

urlpatterns = [
    path("products", ProductListApiView.as_view()),
    path("shoppingcarts", ShoppingCartListApiView.as_view()),
    path("shoppingcartitem", ShoppingCartItemListApiView.as_view()),
]
