from rest_framework import status

from test.product.test_setup import TestApiSetup


class TestProductAPIViews(TestApiSetup):

    def test_get_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_product(self):
        data = {
            "name": "product with test",
            "price": 100.00,
            "quantity": 20,
            "brand_name": "brand name with test",
            "manufacture_number": "1234XYZ",
            "category": None
        }

        response = self.client.post(self.product_url, data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'product with test')
