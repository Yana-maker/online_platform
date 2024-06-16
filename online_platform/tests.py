from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from online_platform.models import Product, Supplier, Network, Contact
from users.models import User


class SetUpTests(APITestCase):
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
            'title': 'test',
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
        print(f"ответ по первому тесту - {response.data['title']}")

        self.assertEquals(
            response.data['title'],
            data['title']
        )

    def test_product_update(self):
        """Тест на редактирование product"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:product_update', args=[self.product.id])
        data = {
            'id': self.product.id,
            'title': 'test update',
            'model': 'model test update'
        }
        response = self.client.put(
            url,
            data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(
            Product.objects.filter(id=self.product.id).exists()
        )

        self.assertEquals(
            response.data['title'],
            data['title']
        )

        print(f"ответ по второму тесту - {response.data['title']}")

    def test_product_retrieve(self):
        """Тест на просмотр определенного product"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:product_retrieve', args=[self.product.id])
        data = {
            'id': self.product.id,
        }
        response = self.client.get(
            url,
            data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(
            Product.objects.filter(id=self.product.id).exists()
        )

        self.assertEquals(
            response.data['id'],
            data['id']
        )

        print(f"ответ по третьему тесту - {response.data['id']}")

    def test_product_destroy(self):
        """Тест на удаление product"""

        self.client.force_authenticate(user=self.user)
        url = reverse('online_platform:product_destroy', args=[self.product.id])

        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Product.objects.filter(id=self.product.id).exists()
        )

