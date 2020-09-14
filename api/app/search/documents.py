import os
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, fields, Index
from elasticsearch_dsl import analyzer

from news.models import News


news_index = Index(os.environ["ELASTIC_INDEX"])

news_index.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@news_index.doc_type
class NewsDocument(Document):
    id = fields.TextField(attr="_id")
    title = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        }
    )
    link = fields.TextField()
    published = fields.TextField(
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        },
        fielddata=True
    )
    description = fields.TextField(
        analyzer=html_strip,
        fields={
            "raw": fields.TextField(analyzer="keyword"),
        }
    )
    author = fields.TextField(
        fielddata=True
    )
    language = fields.TextField(
        fielddata=True
    )

    class Django:
        model = News
