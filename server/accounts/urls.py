from django.urls import path

from .views import (
    login_view , registration_view,
)


app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('registration', registration_view, name='registration')
]
