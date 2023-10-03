# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name = models.TextField(
        db_column="Name", blank=True, null=True
    )  # Field name made lowercase.
    description = models.TextField(
        db_column="Description", blank=True, null=True
    )  # Field name made lowercase.
    price = models.IntegerField(db_column="Price")  # Field name made lowercase.
    picture_url = models.TextField(
        db_column="PictureUrl", blank=True, null=True
    )  # Field name made lowercase.
    type = models.TextField(
        db_column="Type", blank=True, null=True
    )  # Field name made lowercase.
    brand = models.TextField(
        db_column="Brand", blank=True, null=True
    )  # Field name made lowercase.
    quantity_in_stock = models.IntegerField(
        db_column="QuantityInStock"
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Products"


class ShoppingCarts(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    buyer_id = models.TextField(
        db_column="BuyerId", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "ShoppingCarts"


class ShoppingCartItems(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    quantity = models.IntegerField(db_column="Quantity")  # Field name made lowercase.
    product_id = models.ForeignKey(
        Products, db_column="ProductId", on_delete=models.CASCADE
    )  # Field name made lowercase.
    shoppingcart_id = models.ForeignKey(
        ShoppingCarts, db_column="ShoppingCartId", on_delete=models.CASCADE
    )

    class Meta:
        managed = False
        db_table = "ShoppingCartItems"
