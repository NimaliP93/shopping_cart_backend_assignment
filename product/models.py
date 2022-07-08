from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(unique=True, max_length=250)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', unique=True, max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    brand_name = models.CharField(max_length=250)
    manufacture_number = models.CharField(max_length=100)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    token_id = models.IntegerField(null=False, unique=True)


class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, related_name='shopping_cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CustomerDetails(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True)
    address_line1 = models.CharField(max_length=100, null=False)
    address_line2 = models.CharField(max_length=100, null=True)
    address_line3 = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=40, null=False)
    mobile = models.CharField(max_length=12, null=False)


class OrderDetails(models.Model):
    customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    delivery_date = models.DateField(default=None)
    created_ts = models.DateTimeField(auto_now_add=True)
    updated_ts = models.DateTimeField(auto_now_add=True)
    delivery_status = models.BooleanField(default=False)


class OrderItem(models.Model):
    order_details = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)





