from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from news.models import News
from news.serializers import NewsSerializer


class AdminNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "_id"
    
    permission_classes = (
        IsAdminUser,
    )
