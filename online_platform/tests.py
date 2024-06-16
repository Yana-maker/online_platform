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

        self.supplier = Supplier.objects.create(
            id=5,
            title='test-supplier',
            level='розничная сеть',
            email='test-supplier@gmail.com',
            country='test-country',
            city='test-city',
            street=3,
            house_number=3,
        )
        self.supplier.products.add(self.product)

        self.contact = Contact.objects.create(
            id=5,
            email='test-contact@gmail.com',
            country='test-contact',
            city='test-contact',
            street='test street',
            house_number=1231,
        )

        self.network = Network.objects.create(
            name='test-network',
            supplier=self.supplier,
            supplier_debt=150.12,
            contact=self.contact
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
        print(f"ответ по тесту test_product_create - {response.data['title']}")

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

        print(f"ответ по тесту test_product_update- {response.data['title']}")

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

        print(f"ответ по тесту test_product_retrieve- {response.data['id']}")

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


    def test_supplier_create(self):
        """Тест на создание supplier"""

        self.client.force_authenticate(user=self.user)

        data = {
            'id': 3,
            'title': 'test-supplier',
            'level': 'розничная сеть',
            'email': 'test-supplier1@gmail.com',
            'country': 'test-country',
            'city': 'test-city',
            'street': 3,
            'house_number': 3,
            'products': [3]

        }

        response = self.client.post(
            '/supplier/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        print(f"ответ по тесту test_supplier_create- {response.data}")

        self.assertEquals(
            response.data['title'],
            data['title']
        )

    def test_supplier_update(self):
        """Тест на редактирование supplier"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:supplier_update', args=[self.supplier.id])
        data = {
            'id': 3,
            'title': 'test-supplier update',
            'level': 'розничная сеть',
            'email': 'test-supplier@gmail.com',
            'country': 'test-country update',
            'city': 'test-city',
            'street': 3,
            'house_number': 3,
            'products': [3]
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
            Supplier.objects.filter(id=self.supplier.id).exists()
        )

        self.assertEquals(
            response.data['title'],
            data['title']
        )

        print(f"ответ по тесту test_supplier_update- {response.data['title']}")

    def test_supplier_retrieve(self):
        """Тест на просмотр определенного supplier"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:supplier_retrieve', args=[self.supplier.id])
        data = {
            'id': self.supplier.id,
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
            Supplier.objects.filter(id=self.supplier.id).exists()
        )

        self.assertEquals(
            response.data['id'],
            data['id']
        )

        print(f"ответ по тесту test_supplier_retrieve - {response.data['id']}")

    def test_supplier_destroy(self):
        """Тест на удаление supplier"""

        self.client.force_authenticate(user=self.user)
        url = reverse('online_platform:supplier_destroy', args=[self.supplier.id])

        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Supplier.objects.filter(id=self.supplier.id).exists()
        )

    def test_contact_create(self):
        """Тест на создание contact"""

        self.client.force_authenticate(user=self.user)

        data = {
            'email': 'test-contact1@gmail.com',
            'country': 'test-country',
            'city': 'test-city',
            'street': 3,
            'house_number': 3,
        }

        response = self.client.post(
            '/contact/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        print(f"ответ по тесту test_contact_create - {response.data}")

        self.assertEquals(
            response.data['email'],
            data['email']
        )

    def test_contact_update(self):
        """Тест на редактирование contact"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:contact_update', args=[self.contact.id])
        data = {

            'email': 'test-contact_update@gmail.com',
            'country': 'test-country update',
            'city': 'test-city',
            'street': 3,
            'house_number': 3,
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
            Contact.objects.filter(id=self.contact.id).exists()
        )

        self.assertEquals(
            response.data['email'],
            data['email']
        )

        print(f"ответ тесту test_contact_update - {response.data['email']}")

    def test_contact_retrieve(self):
        """Тест на просмотр определенного contact"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:contact_retrieve', args=[self.contact.id])
        data = {
            'id': self.contact.id,
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
            Contact.objects.filter(id=self.contact.id).exists()
        )

        self.assertEquals(
            response.data['id'],
            data['id']
        )

        print(f"ответ по тесту test_contact_retrieve- {response.data['id']}")

    def test_contact_destroy(self):
        """Тест на удаление contact"""

        self.client.force_authenticate(user=self.user)
        url = reverse('online_platform:contact_destroy', args=[self.contact.id])

        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Contact.objects.filter(id=self.contact.id).exists()
        )

    def test_network_create(self):
        """Тест на создание network"""

        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'test-name',
            'supplier': [5],
            'supplier_debt': 125.13,
            'contact': [5],

        }

        response = self.client.post(
            '/network/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )
        print(f"ответ по тесту test_network_create - {response.data}")

        self.assertEquals(
            response.data['name'],
            data['name']
        )

    def test_network_update(self):
        """Тест на редактирование network"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:network_update', args=[self.network.id])
        data = data = {
            'name': 'test-name update',
            'supplier': [5],
            'supplier_debt': 125.13,
            'contact': [5],

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
            Network.objects.filter(id=self.network.id).exists()
        )

        self.assertEquals(
            response.data['name'],
            data['name']
        )

        print(f"ответ тесту test_contact_update - {response.data['name']}")

    def test_network_retrieve(self):
        """Тест на просмотр определенного network"""

        self.client.force_authenticate(user=self.user)

        url = reverse('online_platform:network_retrieve', args=[self.network.id])
        data = {
            'id': self.network.id,
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
            Network.objects.filter(id=self.network.id).exists()
        )

        self.assertEquals(
            response.data['id'],
            data['id']
        )

        print(f"ответ по тесту test_network_retrieve - {response.data['id']}")

    def test_network_destroy(self):
        """Тест на удаление network"""

        self.client.force_authenticate(user=self.user)
        url = reverse('online_platform:network_destroy', args=[self.network.id])

        response = self.client.delete(
            url
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Network.objects.filter(id=self.network.id).exists()
        )
