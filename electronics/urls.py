from django.urls import path

from electronics.views import SupplierCreateAPIView, SupplierRetrieveAPIView, SupplierListAPIView, \
    SupplierUpdateAPIView, SupplierDestroyAPIView, SuppliersContactUpdateAPIView, SuppliersProductUpdateAPIView

urlpatterns = [
    path('create_suppliers/', SupplierCreateAPIView.as_view()),
    path('retrive_suppliers/<int:pk>/', SupplierRetrieveAPIView.as_view()),
    path('update_suppliers/<int:pk>/', SupplierUpdateAPIView.as_view()),
    path('update_contact_suppliers/<int:pk>/', SuppliersContactUpdateAPIView.as_view()),
    path('update_product_suppliers/<int:pk>/', SuppliersProductUpdateAPIView.as_view()),
    path('destroy_suppliers/<int:pk>/', SupplierDestroyAPIView.as_view()),
    path('list_suppliers/', SupplierListAPIView.as_view()),

]