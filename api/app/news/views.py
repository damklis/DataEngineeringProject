import os
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from elasticsearch import Elasticsearch

from .models import News
from .permissions import IsStaffOrReadOnly
from .serializers import NewsSerializer, UserSerializer


class SwaggerSchemaView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)


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
        host=os.environ["ELASTIC_HOST"],
        port=os.environ["ELASTIC_PORT"]
    )

    def get(self, request, *args, **kwargs):
        title = kwargs.get('title', None)
        response = self.elastic.search(
            index=os.environ["ELASTIC_INDEX"],
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
