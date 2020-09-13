from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from search.views import NewsDocumentView


router = DefaultRouter()

router.register(r"", viewset=NewsDocumentView, basename="news")

urlpatterns = [
    url(r"^", include(router.urls)),
]