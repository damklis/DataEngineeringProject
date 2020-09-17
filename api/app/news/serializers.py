from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = [
            "_id",
            "title",
            "link",
            "published",
            "description",
            "author",
            "language"
        ]
