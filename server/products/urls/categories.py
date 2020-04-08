from django.urls import path

from products.views import (
    category_create_view, category_update_view,
    CategoryCreateView, CategoryUpdateView,
    CategoryDeleteView, CategoryListView,
    CategoryDetailView
    )

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/delete', CategoryDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', CategoryUpdateView.as_view(), name='update'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='detail'),
]