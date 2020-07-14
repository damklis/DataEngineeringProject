from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.pymongo_test

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))


mongo_URI = 'mongodb://localhost:27017'

class NewsExporter:
    def __init__(self, mongo_uri):
        self.mongo_client = MongoClient(mongo_uri)

    def __enter__(self):
        return self

    def export_news_to_mongo(self, database, collection, record):
        mongo_db = self.mongo_client[database]
        db_collection = mongo_db[collection]
        db_collection.find_one_and_update(
            {
                "news_id": record["news_id"]
            },
            {
                "$set": record
            },
            upsert=True
        )

if __name__ == "__main__":
    exporter = NewsExporter(mongo_URI)
    record = {"news_id": "damianklis", "name": "damian", "surname": "cipek"}
    exporter.export_news_to_mongo("test", "test_damian", record)
    exporter.export_news_to_mongo("test", "test_damian", record)
    exporter.export_news_to_mongo("test", "test_damian", record)
    exporter.export_news_to_mongo("test", "test_damian", record)
    exporter.export_news_to_mongo("test", "test_damian", record)


