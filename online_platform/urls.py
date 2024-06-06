from django.urls import path
from online_platform.apps import OnlinePlatformConfig
from online_platform.views import ProductCreateApiView, ProductUpdateApiView, \
    ProductRetrieveApiView, ProductDestroyApiView, SupplierCreateApiView, \
    SupplierUpdateApiView, SupplierRetrieveApiView, SupplierDestroyApiView

app_name = OnlinePlatformConfig.name

urlpatterns = [
    path('/product/create/', ProductCreateApiView.as_view(), name='product_create'),
    path('/product/update/<int:pk>/', ProductUpdateApiView.as_view(), name='product_update'),
    path('/product/retrieve/<int:pk>/', ProductRetrieveApiView.as_view(), name='product_retrieve'),
    path('/product/destroy/<int:pk>/', ProductDestroyApiView.as_view(), name='product_destroy'),

    path('/supplier/create/', SupplierCreateApiView.as_view(), name='supplier_create'),
    path('/supplier/update/<int:pk>/', SupplierUpdateApiView.as_view(), name='supplier_update'),
    path('/supplier/retrieve/<int:pk>/', SupplierRetrieveApiView.as_view(), name='supplier_retrieve'),
    path('/supplier/destroy/<int:pk>/', SupplierDestroyApiView.as_view(), name='supplier_destroy'),

]
