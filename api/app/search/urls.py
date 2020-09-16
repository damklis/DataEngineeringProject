from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from search.views import NewsDocumentView

app_name = "search"

router = DefaultRouter()

router.register(r"", viewset=NewsDocumentView, basename="search")

urlpatterns = [
    path("", include(router.urls)),
]