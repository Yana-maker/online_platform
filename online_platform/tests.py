from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from online_platform.models import Product, Supplier, Network, Contact
from users.models import User
from online_platform.serializers import ProductSerializer, SupplierSerializer, NetworkSerializer, ContactSerializer


class ProductTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            id=1,
            username='admin',
            password=1234
        )

        self.product = Product.objects.create(
            id=3,
            title='test-title',
            model='test-model'
        )

    def test_product_create(self):
        """Тест на создание product"""

        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'test 3',
            'model': 'model test'
        }

        response = self.client.post(
            '/product/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.data['title'],
            data['title']
        )

