from django.contrib import admin

from online_platform.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'email', 'country', 'city', 'street',
                    'house_number', 'debt', 'created_at',)
    list_filter = ('city',)
    actions = ['debt_delete']

    @admin.action(description='Удалить задолженность поставщика')
    def debt_delete(self, request, queryset):
        """Удаление задолженности поставщика"""
        selected_objects = queryset.update(debt=0)
        self.message_user(request, f"Действие выполнено над {selected_objects} объектами.")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_data',)
    list_filter = ('title',)
