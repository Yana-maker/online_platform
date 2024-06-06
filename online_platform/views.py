from django.shortcuts import render
from rest_framework import generics

from online_platform.models import Product, Supplier
from online_platform.serializers import ProductSerializer, SupplierSerializer


# Create your views here.
class ProductCreateApiView(generics.CreateAPIView):
    """Создание продукта"""
    serializer_class = ProductSerializer


class ProductUpdateApiView(generics.UpdateAPIView):
    """Редактирование продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyApiView(generics.DestroyAPIView):
    """Удаление продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SupplierCreateApiView(generics.CreateAPIView):
    """Создание поставщика"""
    serializer_class = SupplierSerializer


class SupplierUpdateApiView(generics.UpdateAPIView):
    """Редактирование поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


class SupplierDestroyApiView(generics.DestroyAPIView):
    """Удаление поставщика"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
