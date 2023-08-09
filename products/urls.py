from django.urls import path
from .views import ProductsCreateView, ProductsListView, get_products, ProductUpdateView, update_category_ajax, delete_product, get_price
urlpatterns = [
    path('create/', ProductsCreateView.as_view(), name='create_product'),
    path('', ProductsListView.as_view(), name='list_product'),
    path('get-products/', get_products, name='get_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('update-ajax/<int:pk>/', update_category_ajax, name='update_product_ajax'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('get-price/<int:id_product>/', get_price, name='get-price'),
]