from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from search.documents import NewsDocument


class NewsDocumentSerializer(DocumentSerializer):

    class Meta:
        document = NewsDocument
        fields = (
            "title",
            "link",
            "published",
            "description",
            "author",
            "language"
        )
