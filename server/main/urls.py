from django.urls import path

from .views import index, about, contacts


app_name = 'main'

urlpatterns = [
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('', index, name='main'),
]
