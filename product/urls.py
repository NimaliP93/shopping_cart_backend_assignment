from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, ShoppingCartItemViewSet, ShoppingCartViewSet, CustomerDetailsViewSet, \
    OrderDetailsViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'shopping_cart', ShoppingCartViewSet, basename='cart')
router.register(r'shopping_cart_item', ShoppingCartItemViewSet, basename='cart_item')
router.register(r'customer_details', CustomerDetailsViewSet, basename='customer_details')
router.register(r'order_details', OrderDetailsViewSet, basename='order_details')
router.register(r'order_item', OrderItemViewSet, basename='order_item')

urlpatterns = [
    path('', include(router.urls))
]
