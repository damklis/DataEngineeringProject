from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from news.views import DeleteNews, NewsDocumentView


router = DefaultRouter()

router.register(
    r"",
    viewset=NewsDocumentView,
    basename="news"
)

urlpatterns = [
    url(r"<title>/", DeleteNews.as_view(), name="news_detail"),
    url(r"^", include(router.urls)),
]
