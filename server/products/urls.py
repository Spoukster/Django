from django.urls import path

from .views import (
    product_list_view,
    product_detail_view,
    category_create_view,
    category_update_view,
    product_create_view,
    product_update_view
    )

urlpatterns = [
    path('', product_list_view, name='list'),
    path('categories/create/', category_create_view, name='create_cat'),
    path('categories/<int:pk>/update', category_update_view, name='update_cat'),
    path('products/create/', product_create_view, name='create_prod'),
    path('products/<int:pk>/update', product_update_view, name='update_prod'),
    path('<int:pk>/', product_detail_view, name='detail')
]
