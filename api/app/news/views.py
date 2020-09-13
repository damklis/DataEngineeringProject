from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from news.models import News
from news.serializers import NewsSerializer


class AdminNewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    permission_classes = (
        IsAdminUser,
    )


class AdminNewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "title"

    permission_classes = (
        IsAdminUser,
    )
