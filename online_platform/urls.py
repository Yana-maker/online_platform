from django.urls import path
from online_platform.apps import OnlinePlatformConfig
from online_platform.views import ProductCreateApiView, ProductUpdateApiView, \
    ProductRetrieveApiView, ProductDestroyApiView, SupplierCreateApiView, \
    SupplierUpdateApiView, SupplierRetrieveApiView, SupplierDestroyApiView, SupplierListApiView, NetworkUpdateApiView, \
    NetworkCreateApiView, NetworkRetrieveApiView, NetworkDestroyApiView, NetworkListApiView, \
    ContactUpdateApiView, ContactRetrieveApiView, ContactDestroyApiView, ContactListApiView, ContactCreateApiView, \
    ProductListApiView

app_name = OnlinePlatformConfig.name


urlpatterns = [
    # урлы для продукта
    path('product/create/', ProductCreateApiView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateApiView.as_view(), name='product_update'),
    path('product/retrieve/<int:pk>/', ProductRetrieveApiView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>/', ProductDestroyApiView.as_view(), name='product_destroy'),
    path('product/list/', ProductListApiView.as_view(), name='product_list'),
    # урлы для поставщика
    path('supplier/create/', SupplierCreateApiView.as_view(), name='supplier_create'),
    path('supplier/update/<int:pk>/', SupplierUpdateApiView.as_view(), name='supplier_update'),
    path('supplier/retrieve/<int:pk>/', SupplierRetrieveApiView.as_view(), name='supplier_retrieve'),
    path('supplier/destroy/<int:pk>/', SupplierDestroyApiView.as_view(), name='supplier_destroy'),
    path('supplier/list/', SupplierListApiView.as_view(), name='supplier_list'),
    # урлы для сети
    path('network/create/', NetworkCreateApiView.as_view(), name='network_create'),
    path('network/update/<int:pk>/', NetworkUpdateApiView.as_view(), name='network_update'),
    path('network/retrieve/<int:pk>/', NetworkRetrieveApiView.as_view(), name='network_retrieve'),
    path('network/destroy/<int:pk>/', NetworkDestroyApiView.as_view(), name='network_destroy'),
    path('network/list/', NetworkListApiView.as_view(), name='network_list'),
    # урлы для контактов
    path('contact/create/', ContactCreateApiView.as_view(), name='contact_create'),
    path('contact/update/<int:pk>/', ContactUpdateApiView.as_view(), name='contact_update'),
    path('contact/retrieve/<int:pk>/', ContactRetrieveApiView.as_view(), name='contact_retrieve'),
    path('contact/destroy/<int:pk>/', ContactDestroyApiView.as_view(), name='contact_destroy'),
    path('contact/list/', ContactListApiView.as_view(), name='contact_list')
]
