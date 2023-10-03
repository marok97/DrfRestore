from rest_framework import serializers
from .models import Products, ShoppingCarts, ShoppingCartItems


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCarts
        fields = "__all__"

class ShoppingCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCartItems
        fields = "__all__"
