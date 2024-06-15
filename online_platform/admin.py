from django.contrib import admin
from django.utils.html import format_html

from online_platform.models import Supplier, Product, Network, Contact


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'email', 'country', 'city', 'street',
                    'house_number', 'created_at',)
    # фильтр по городам
    list_filter = ('city',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('email', 'country', 'city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_data',)
    list_filter = ('title',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'supplier', 'supplier_debt', 'view_link',)
    list_filter = ('contact__country', 'contact__city',)
    actions = ['debt_delete']

    def view_link(self, obj):
        """Ссылка на поставщика"""
        return format_html('<a href="{}">Просмотр поставщика</a>', obj.get_absolute_url())

    view_link.allow_tags = True
    view_link.short_description = 'Ссылка на поставщика'

    @admin.action(description='Удалить задолженность поставщика')
    def debt_delete(self, request, queryset):
        """Удаление задолженности поставщика"""
        selected_objects = queryset.update(supplier_debt=0)
