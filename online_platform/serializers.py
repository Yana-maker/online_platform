from rest_framework import serializers
from online_platform.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""
    class Meta:
        model = Product
        exclude = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор поставщика"""
    class Meta:
        model = Supplier
        exclude = "__all__"
