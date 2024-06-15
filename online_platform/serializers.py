from rest_framework import serializers
from online_platform.models import Product, Supplier, Network, Contact


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""
    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(serializers.ModelSerializer):
    """Сериализатор поставщика"""
    level = serializers.CharField(read_only=True)

    class Meta:
        model = Supplier
        fields = "__all__"


class NetworkSerializer(serializers.ModelSerializer):
    """Сериализатор Network"""
    supplier_debt = serializers.CharField(read_only=True)

    class Meta:
        model = Network
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор контактов"""
    class Meta:
        model = Contact
        fields = "__all__"
