import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import unit_of_work


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        uow = unit_of_work.MongoUnitOfWork()
        collection = uow.get_all('posts')
        result = dumps(collection)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)

        # url = "localhost"  # TODO: Update with appropriate MongoDB connection information
        # client = pymongo.MongoClient(url)
        # database = client['azure']
        # collection = database['posts']

        # result = collection.find({})
        # result = dumps(result)

        # return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)