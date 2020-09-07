from django.urls import path
from rest_framework.authtoken import views

from news.views import NewsList, NewsDetail


urlpatterns = [
    path("", NewsList.as_view(), name="news_list"),
    path("<title>/", NewsDetail.as_view(), name="news_detail")
]
