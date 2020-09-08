from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend, SearchFilterBackend, FacetedSearchFilterBackend,
)

from news.documents import NewsDocument
from news.serializers import NewsDocumentSerializer
from news.models import News
from news.serializers import NewsSerializer
from core.permissions import IsStaffOrReadOnly


class NewsDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        SearchFilterBackend,
        FilteringFilterBackend,
    ]

    search_fields = (
        "title",
        "description"
    )

    filter_fields = {
        "language": "language"
    }



class DeleteNews(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "title"

    permission_classes = (
        IsStaffOrReadOnly, IsAuthenticated
    )