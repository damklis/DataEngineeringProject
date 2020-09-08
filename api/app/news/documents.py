import os
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, fields, Index

from news.models import News

news_index = Index(os.environ["ELASTIC_INDEX"])

news_index.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@news_index.doc_type
class NewsDocument(Document):
    id = fields.TextField(attr='_id')
    title = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    link = fields.TextField()
    published = fields.DateField()
    description = fields.TextField(
        fields={
            'raw': fields.TextField(analyzer='keyword'),
        }
    )
    author = fields.TextField()
    language = fields.TextField()

    class Django:
        model = News
