from django.urls import include, path
from rest_framework import routers

from news.views import AdminNewsViewSet


router = routers.DefaultRouter()
router.register(r"news", AdminNewsViewSet)

urlpatterns = [
    path("api/", include(router.urls), name="news")
]