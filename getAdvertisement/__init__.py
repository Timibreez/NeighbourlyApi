import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import unit_of_work

def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    print("--------------->", id)
    
    if id:
        try:
            uow = unit_of_work.MongoUnitOfWork()
            collection_name = 'advertisements'
            result = uow. get_one(collection_name, id)

            print("----------result--------")
            result = dumps(result)
            print(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')

        # try:
        #     url = "localhost"  # TODO: Update with appropriate MongoDB connection information
        #     client = pymongo.MongoClient(url)
        #     database = client['azure']
        #     collection = database['advertisements']
           
        #     query = {'_id': ObjectId(id)}
        #     result = collection.find_one(query)
        #     print("----------result--------")

        #     result = dumps(result)
        #     print(result)

        #     return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)