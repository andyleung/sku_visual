#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_q3_pipeline():
   q3_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
		 	   "Product_Series":{"$eq":"SRX5000"}}},
		{"$group":{"_id":"$Country",
                 "quarter":{"$addToSet":"$Achievement_Quarter"},
                 "Total":{"$sum":"$Achievement_Net"}}},
                {"$sort":{"Total":-1}},
		{"$limit":10}
               ]
   return q3_pipeline

def make_q4_pipeline():
   q4_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
		 	   "Product_Series":{"$eq":"SRX5000"}}},
		{"$group":{"_id":"$Country",
                 "quarter":{"$addToSet":"$Achievement_Quarter"},
                 "Total":{"$sum":"$Achievement_Net"}}},
                {"$sort":{"Total":-1}},
		{"$limit":10}
               ]
   return q4_pipeline

def aggregate(db, pipeline):
    result = db.projects.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('srxsales')
    q3_pipeline = make_q3_pipeline()
    q4_pipeline = make_q4_pipeline()
    q3_cursor = aggregate(db, q3_pipeline)
    q4_cursor = aggregate(db, q4_pipeline)
    import pprint
    print ("Q3 Results: \n")
    pprint.pprint(q3_cursor["result"])
    print ("Q4 Results: \n")
    pprint.pprint(q4_cursor["result"])

