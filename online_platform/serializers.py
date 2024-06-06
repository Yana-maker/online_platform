from rest_framework import serializers
from online_platform.models import Product, Supplier


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор поставщика"""
    class Meta:
        model = Supplier
        fields = "__all__"
