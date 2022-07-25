import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import unit_of_work

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            uow = unit_of_work.MongoUnitOfWork()
            collection_name = 'advertisements'
            results = uow.delete_by_id(collection_name, id)

            return func.HttpResponse('Advert Deleted')

        # try:
        #     url = "localhost"  # TODO: Update with appropriate MongoDB connection information
        #     client = pymongo.MongoClient(url)
        #     database = client['azure']
        #     collection = database['advertisements']
            
        #     query = {'_id': ObjectId(id)}
        #     result = collection.delete_one(query)
        #     return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
