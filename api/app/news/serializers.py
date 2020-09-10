from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from news.documents import NewsDocument
from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = [
            "title",
            "link",
            "published",
            "description",
            "author",
            "language"
        ]


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