#!/usr/bin/env python
from bson.json_util import dumps

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
   pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
		 	   "Product_Series":{"$in":["SRX300"]}}},
		{"$group":{"_id":"$Country",
                 "Total":{"$sum":"$Achievement_Net"}}},
                {"$sort":{"Total":-1}},
		{"$limit":10}
               ]
   return pipeline

def aggregate(db, pipeline):
    result = db.projects.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('srxsales')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    print("...........\n")
    my_new_page = dumps(result)
    print my_new_page

#    assert len(result["result"]) == 1
#    assert result["result"][0]["followers"] == 17209


