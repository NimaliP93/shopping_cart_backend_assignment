from rest_framework import status
from test.product.test_setup import TestApiSetup


class TestProductAPIViews(TestApiSetup):
    fixtures = ['test/fixtures/category.json',
                'test/fixtures/product.json',
                'test/fixtures/cart.json',
                'test/fixtures/cart_item.json']

    def test_get_shopping_cart_items(self):
        response = self.client.get(self.shopping_cart_items_url + "?cart_id=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_shopping_cart_item(self):
        data = {
            "cart": 1, "product": 1, "quantity": 2
        }

        response = self.client.post(self.shopping_cart_items_url + "?cart_id=1", data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['quantity'], 2)

    def test_post_shopping_cart_item_with_no_cart(self):
        data = {
            "cart": 2, "product": 1, "quantity": 2
        }

        response = self.client.post(self.shopping_cart_items_url + "?cart_id=2", data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_shopping_cart_item(self):
        response = self.client.delete(self.shopping_cart_items_url + "1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
