from django.urls import path
from rest_framework.authtoken import views

from .views import UserCreate, NewsList, NewsDetail


urlpatterns = [
    path("register/", UserCreate.as_view(), name="register"),
    path("login/", views.obtain_auth_token, name="login"),
    path("news/", NewsList.as_view(), name="news_list"),
    path("news/<title>/", NewsDetail.as_view(), name="news_detail")
]
