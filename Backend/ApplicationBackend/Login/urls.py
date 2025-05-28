from django.urls import include, path
from .views import CreateUserAccount, create_user_form

urlpatterns = [
    path('add/', CreateUserAccount.as_view(), name='create_user'),
    path('register/', create_user_form, name='create_user_form')
]