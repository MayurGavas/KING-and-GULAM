from django.urls import include, path
from . import views

Urlpatterns = [
    path('add/', views.UserAccount.create_account, name='create_user')
]