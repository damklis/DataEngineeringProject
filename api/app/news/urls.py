from django.urls import path
from rest_framework.authtoken import views

from .views import UserCreate, NewsList, NewsDetail, SwaggerSchemaView


urlpatterns = [
    path("user/register/", UserCreate.as_view(), name="register"),
    path("user/login/", views.obtain_auth_token, name="login"),
    path("news/", NewsList.as_view(), name="news_list"),
    path("news/<title>/", NewsDetail.as_view(), name="news_detail"),
    path("", SwaggerSchemaView.as_view(), name="api_docs")
]
