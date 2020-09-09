from django.urls import path
from rest_framework.authtoken import views

from users.views import UserCreate


urlpatterns = [
    path("register/", UserCreate.as_view(), name="register"),
    path("login/", views.obtain_auth_token, name="login")
]
