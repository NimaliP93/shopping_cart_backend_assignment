from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Product, ShoppingCartItem, ShoppingCart, OrderDetails, CustomerDetails, OrderItem
from .serializers import ProductSerializer, ShoppingCartItemSerializer, ShoppingCartSerializer, OrderDetailsSerializer, \
    OrderItemSerializer, CustomerDetailsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ShoppingCartViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer
    queryset = ShoppingCart.objects.all()


class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingCartItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        return all the added items a cart if cart id is provided or
        return relevant item in the cart if cart item id is provided
        """
        cart_id = self.request.query_params.get('cart_id')
        if cart_id is not None:
            self.queryset = ShoppingCartItem.objects.filter(cart__id=cart_id)
            return self.queryset
        else:
            self.queryset = ShoppingCartItem.objects.filter(id=self.kwargs.get('pk'))
            return self.queryset

    def create(self, request, *args, **kwargs):
        try:
            cart = ShoppingCart.objects.get(id=self.request.query_params.get('cart_id'))
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(cart=cart)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ShoppingCart.DoesNotExist:
            return Response({'error': 'Shopping Cart does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            cart_item = self.get_object()
            cart_item.delete()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDetailsSerializer
    queryset = CustomerDetails.objects.all()


class OrderDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
