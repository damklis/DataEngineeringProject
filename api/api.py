from elasticsearch import Elasticsearch
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class NewsEntry(Resource):

    elastic = Elasticsearch(
        [{"host": "localhost", "port": 9200}]
    )

    def get(self, phrase):
        response = self.elastic.search(
            index="mongo.rss.rss",
            body={
                "query": {
                    "match": {
                        "title": phrase
                    }
                }
            } 
        )

        news_list = response.get("hits").get("hits")

        return {
            "results": [
                news["_source"] for news in news_list
            ]
        }


api.add_resource(NewsEntry, "/v1/api/<string:phrase>")


if __name__ == "__main__":
    app.run(port=8081, debug=True)
