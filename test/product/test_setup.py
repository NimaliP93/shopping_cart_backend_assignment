from rest_framework.test import APITestCase


class TestApiSetup(APITestCase):
    product_url = 'http://127.0.0.1:8000/product/'
    shopping_cart_url = 'http://127.0.0.1:8000/shopping_cart/'
    shopping_cart_items_url = 'ttp://127.0.0.1:8000/shopping_cart_item/'

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
