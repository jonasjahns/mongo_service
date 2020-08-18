from pymongo import MongoClient
from bson import json_util

# MongoDB Address, bellow you can see the default local MongoDB port and IP
mongo_client = 'mongodb://127.0.0.1:27017'
# MongoDB DataBase to be used.
data_base = 'control'


def client_start():
    client = MongoClient(mongo_client)
    return client


def database_start(db_name: str):
    client = client_start()
    return client[db_name]


def collection_start(col_name: str):
    client = database_start(data_base)
    return client[col_name]


def object_save(objetc, client):
    db = collection_start(client)
    print(db.insert_one(objetc).inserted_id)


def objects_save(objects, client):
    db = collection_start(client)
    db.insert_many(objects)


def return_data(data):
    return json_util.loads(json_util.dumps(data))


def find_all(client):
    db = collection_start(client)
    return return_data(db.find())


def find_many(client, query):
    db = collection_start(client)
    return return_data(db.find(query))


def delete(client, query):
    db = collection_start(client)
    print(db.delete_one(query))


def find_one(client):
    db = collection_start(client)
    return return_data(db.find_one())
