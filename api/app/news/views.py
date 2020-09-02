from django.shortcuts import render
from rest_framework import generics

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from .models import News
from .serializers import NewsSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from elasticsearch import Elasticsearch
from rest_framework.response import Response

from .permissions import IsStaffOrReadOnly


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer

    permission_classes = ()


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    permission_classes = (
        IsStaffOrReadOnly, IsAuthenticated
    )


class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    permission_classes = (
        IsStaffOrReadOnly, IsAuthenticated
    )

    lookup_field = "title"

    elastic = Elasticsearch(
        host="elasticsearch", port=9200)

    def get(self, request, *args, **kwargs):
        title = kwargs.get('title', None)
        response = self.elastic.search(
            index="unique.rss_news.rss_news",
            body={
                "query": {
                    "match": {
                        "title": title
                    }
                }
            }
        )
        news_list = response.get("hits").get("hits")
        
        return Response(
            {
                "results": [
                    {k: v for k, v in news["_source"].items() if k != "id"}
                    for news in news_list
                ]
            }
        )
