import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import unit_of_work

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        uow = unit_of_work.MongoUnitOfWork()
        collection = uow.get_all('advertisements')

        result = dumps(collection)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')

    # try:
    #     url = "localhost"  # TODO: Update with appropriate MongoDB connection information
    #     client = pymongo.MongoClient(url)
    #     database = client['azure']
    #     collection = database['advertisements']


    #     result = collection.find({})
    #     result = dumps(result)

    #     return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

