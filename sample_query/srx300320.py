#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
   pipeline = [ {"$match":{"Product":{"$in":["SRX300","SRX320"]}}},
		{"$group":{"_id":{"$concat":["$Company_Name","-","$Country"]},
			   "units":{"$sum":1},
                           "Total_Sales":{"$sum":"$Achievement_Net"}}},
                {"$sort":{"Total_Sales":-1}},
		{"$limit":50}
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

#    assert len(result["result"]) == 1
#    assert result["result"][0]["followers"] == 17209


