from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    login_view , registration_view,
    AccountRegistrationView, AccountLoginView,
    AccointLogoutView
)


app_name = 'accounts'

urlpatterns = [
    # path('', login_view, name='login'),
    path('', AccountLoginView.as_view(), name='login'),
    #path('registration', registration_view, name='registration')
    path('registration', AccountRegistrationView.as_view(), name='registration'),
    path('logout/', AccointLogoutView.as_view(), name='logout')
]
