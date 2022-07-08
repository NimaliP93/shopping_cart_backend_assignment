from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(OrderDetails)
admin.site.register(OrderItem)
admin.site.register(CustomerDetails)
