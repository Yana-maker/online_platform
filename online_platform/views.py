from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from online_platform.models import Product, Supplier, Network, Contact
from online_platform.serializers import ProductSerializer, SupplierSerializer, NetworkSerializer, ContactSerializer
from users.permissions import IsActiveUser


# Create your views here.
class ProductCreateApiView(generics.CreateAPIView):
    """Создание продукта"""
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]


class ProductUpdateApiView(generics.UpdateAPIView):
    """Редактирование продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductListApiView(generics.ListAPIView):
    """Список продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductDestroyApiView(generics.DestroyAPIView):
    """Удаление продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class SupplierCreateApiView(generics.CreateAPIView):
    """Создание поставщика"""
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveUser]


class SupplierUpdateApiView(generics.UpdateAPIView):
    """Редактирование поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]


class SupplierRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser | AllowAny]


class SupplierListApiView(generics.ListAPIView):
    """Список поставщиков"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]

    # фильтр по полю страна
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)


class SupplierDestroyApiView(generics.DestroyAPIView):
    """Удаление поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveUser]


class NetworkCreateApiView(generics.CreateAPIView):
    """Создание Network"""
    serializer_class = NetworkSerializer
    permission_classes = [IsActiveUser]


class NetworkUpdateApiView(generics.UpdateAPIView):
    """Редактирование Network"""
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveUser]


class NetworkRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр Network"""
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveUser]


class NetworkListApiView(generics.ListAPIView):
    """Список Network"""
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveUser]

    # фильтр по полю страна
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contact__country',)


class NetworkDestroyApiView(generics.DestroyAPIView):
    """Удаление Network"""
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    permission_classes = [IsActiveUser]


class ContactCreateApiView(generics.CreateAPIView):
    """Создание Contact"""
    serializer_class = ContactSerializer
    permission_classes = [IsActiveUser]


class ContactUpdateApiView(generics.UpdateAPIView):
    """Редактирование Contact"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveUser]


class ContactRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр Contact"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveUser]


class ContactListApiView(generics.ListAPIView):
    """Список Contact"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveUser]


class ContactDestroyApiView(generics.DestroyAPIView):
    """Удаление Contact"""
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsActiveUser]
