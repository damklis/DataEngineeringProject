from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend, 
    CompoundSearchFilterBackend, 
    DefaultOrderingFilterBackend,
    OrderingFilterBackend
)

from search.documents import NewsDocument
from search.serializers import NewsDocumentSerializer


class NewsDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = "id"
    filter_backends = [
        CompoundSearchFilterBackend,
        FilteringFilterBackend,
        DefaultOrderingFilterBackend,
        OrderingFilterBackend
    ]

    search_fields = (
        "title",
        "description"
    )

    filter_fields = {
        "language": "language"
    }
    
    ordering_fields = {
        "published": "published",
        "author": "author",
        "language": "language"
    }

    ordering = (
        "published",
    )
