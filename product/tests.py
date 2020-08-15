from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class ProductsTestCase(TestCase):
    def setUp(self):
        products_url = reverse("products")
        c = Client()
        self.response = c.get(products_url)
        self.products = Product.objects.all()

    def test_products_open_200_OK(self):
        self.assertEqual(self.response.status_code, 200)
        # print(self.response.content)
        self.assertContains(self.response, "Все товары")
        self.assertContains(self.response, "Все продавцы")