from django.urls import path
from .views import CategoryCreateView, CategoriesListView, CategoryUpdateView, update_category_ajax, get_categories, delete_category


urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name = 'create_category'),
    path('', CategoriesListView.as_view(), name='list_category'),
    path('categories/', get_categories, name='get_categories'),
    path('update/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('update-ajax/<int:pk>/', update_category_ajax, name='update_category_ajax'),
    path('delete/<int:category_id>/', delete_category, name='delete_category'),
]