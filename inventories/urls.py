from django.urls import path
from .views import InventoriesCreateView, InventoriesListView, get_inventories, InventoryUpdateView, update_inventory_ajax, delete_inventory

urlpatterns = [
    path('create/', InventoriesCreateView.as_view(), name = 'create_inventory'),
    path('', InventoriesListView.as_view(), name="list_inventory"),
    path('inventories/', get_inventories, name='get_inventories'),
    path('update/<int:pk>', InventoryUpdateView.as_view(), name='update_inventory'),
    path('update-ajax/<int:pk>/', update_inventory_ajax, name='update_inventory_ajax'),
    path('delete/<int:inventory_id>',delete_inventory, name='delete-inventory'),
]