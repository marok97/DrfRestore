from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products, ShoppingCarts, ShoppingCartItems
from .serializers import (
    ProductSerializer,
    ShoppingCartSerializer,
    ShoppingCartItemSerializer,
)


# Create your views here.
class ProductListApiView(APIView):
    def get(self, request, *args, **kwargs):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ShoppingCartListApiView(APIView):
    def get(self, request, *args, **kwargs):
        carts = ShoppingCarts.objects.all()
        serializer = ShoppingCartSerializer(carts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ShoppingCartItemListApiView(APIView):
    def get(self, request, *args, **kwargs):
        items = ShoppingCartItems.objects.all()
        serializer = ShoppingCartItemSerializer(items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
