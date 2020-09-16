from django.urls import path

from users.views import UserCreateView, ObtainTokenView

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", ObtainTokenView.as_view(), name="login")
]
