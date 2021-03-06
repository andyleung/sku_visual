from flask import Flask
from flask import render_template,url_for
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'srxsales'
COLLECTION_NAME = 'projects'
FIELDS = {'Product': True, 'Country': True, 'Partner_Name': True, 'Achievement_Date': True, 'Achievement_Net': True, '_id': False}

@app.route("/test1")
def test1():
    return render_template("test1.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/apac_sales")
def apac_sales():
    pipeline = [{"$group":{"_id":"$Country",
                 "Total":{"$sum":"$Achievement_Net"}}},
                {"$sort":{"Total":-1}}]
                ## {"$limit":10}]
    client = MongoClient('localhost:27017')
    ## print "Connection OK!!"
    db = client[DBS_NAME]
    ## print "Collections.works !!"
    cursor = db.projects.aggregate(pipeline)
    ## print "Done with cursor"
    import pprint
    ## print "This is the cursor/result:"
    ## pprint.pprint(cursor)
    output = json.dumps(cursor["result"])
    return (output)

## apac_pie looks for data from /apac_sales
@app.route('/pie')
def apac_pie():
    return render_template('pie.html')

@app.route('/srx5K_diff')
def srx5K_diff():
    q3_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
                               "Product_Series":{"$eq":"SRX5000"}}},
                    {"$group":{"_id":"$Country",
                               ## "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    q4_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
                               "Product_Series":{"$eq":"SRX5000"}}},
                    {"$group":{"_id":"$Country",
                               ## "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    client = MongoClient('localhost:27017')
    db = client[DBS_NAME]
    ## Find Result List #1
    cursor1 = db.projects.aggregate(q3_pipeline)
    output1 = cursor1["result"]
    for i in output1:
      i["quarter"] = "Q3-2016"
    ## Find Result List #2
    cursor2 = db.projects.aggregate(q4_pipeline)    
    output2 = cursor2["result"]
    for j in output2:
      j["quarter"] = "Q4-2016"
    output = output1 + output2
    return json.dumps(output)

## compare5K reads data from srx5K_diff
@app.route('/compare5K')
def compare5K():
    return render_template('compare5K.html')

@app.route('/newbranchq3')
def newbranchq3():
    q3_300_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
                               "Product_Series":{"$eq":"SRX300"}}},
                    {"$group":{"_id":"$Country",
                       ##        "products":{"$addToSet":"$Product_Series"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    q3_100200_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
                               "Product_Series":{"$in":["SRX100","SRX200"]}}},
                    {"$group":{"_id":"$Country",
                         ##      "products":{"$addToSet":"$Product_Series"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    client = MongoClient('localhost:27017')
    db = client[DBS_NAME]
    cursor1 = db.projects.aggregate(q3_300_pipeline)
    output1 = cursor1["result"]
    for i in output1:
      i["products"] = "SRX300"
    cursor2 = db.projects.aggregate(q3_100200_pipeline)
    output2 = cursor2["result"]
    for j in output2:
      j["products"] = "SRX100-SRX200"
    output = output1 + output2
    return json.dumps(output)

## compareQ3branch reads data from newbranchq3
@app.route('/compareQ3branch')
def compareQ3branch():
    return render_template('compareQ3branch.html')

@app.route('/newbranchq4')
def newbranchq4():
    q4_300_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
                               "Product_Series":{"$eq":"SRX300"}}},
                    {"$group":{"_id":"$Country",
                       ##        "products":{"$addToSet":"$Product_Series"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    q4_100200_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
                               "Product_Series":{"$in":["SRX100","SRX200"]}}},
                    {"$group":{"_id":"$Country",
                       ##        "products":{"$addToSet":"$Product_Series"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    client = MongoClient('localhost:27017')
    db = client[DBS_NAME]
    cursor1 = db.projects.aggregate(q4_300_pipeline)
    output1 = cursor1["result"]
    for i in output1:
        i["products"] = "SRX300"
    cursor2 = db.projects.aggregate(q4_100200_pipeline)
    output2 = cursor2["result"]
    for j in output2:
        j["products"] = "SRX100-SRX200"
    output = output1 + output2
    return json.dumps(output)

## compareQ4branch reads data from newbranchq4
@app.route('/compareQ4branch')
def compareQ4branch():
    return render_template('compareQ4branch.html')

@app.route('/srx1500growth')
def srx1500growth():
    q3_1500_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
                               "Product_Series":{"$eq":"SRX1500"}}},
                    {"$group":{"_id":"$Country",
                    ###           "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    q4_1500_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
                               "Product_Series":{"$eq":"SRX1500"}}},
                    {"$group":{"_id":"$Country",
                    ###           "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    client = MongoClient('localhost:27017')
    db = client[DBS_NAME]
    cursor1 = db.projects.aggregate(q3_1500_pipeline)
    output1 = cursor1["result"]
    for i in output1:
      i["quarter"] = "Q3-2016"
    cursor2 = db.projects.aggregate(q4_1500_pipeline)
    output2 = cursor2["result"]
    for i in output2:
      i["quarter"] = "Q4-2016"
    output = output1 + output2
    return json.dumps(output)

## compareSRX1500 reads data from srx 1500 growth
@app.route('/compare1500')
def compare1500():
    return render_template('compare1500.html')

@app.route('/srx_mid_growth')
def srx_mid_growth():
    q3_midrange_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q3"},
                               "Product_Series":{"$in":["SRX1000","SRX3000"]}}},
                    {"$group":{"_id":"$Country",
                        ##       "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    q4_midrange_pipeline = [ {"$match":{"Achievement_Quarter":{"$eq":"2016-Q4"},
                               "Product_Series":{"$in":["SRX1000","SRX3000"]}}},
                    {"$group":{"_id":"$Country",
                        ##     "quarter":{"$addToSet":"$Achievement_Quarter"},
                               "Total":{"$sum":"$Achievement_Net"}}},
                    {"$sort":{"Total":-1}}]
    client = MongoClient('localhost:27017')
    db = client[DBS_NAME]
    cursor1 = db.projects.aggregate(q3_midrange_pipeline)
    output1 = cursor1["result"]
    for i in output1:
      i["quarter"] = "Q3-2016"
    cursor2 = db.projects.aggregate(q4_midrange_pipeline)
    output2 = cursor2["result"]
    for j in output2:
      j["quarter"] = "Q4-2016"
    output = output1 + output2
    return json.dumps(output)

## compare midrange reads data from srx_mid_growth
@app.route('/compare_midrange')
def compare_midrange():
    return render_template('compare_midrange.html')

@app.route("/srxsales/2016")
def donorschoose_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    one_project = collection.find_one(projection=FIELDS)
    print ("Degbug: one_project %s", one_project)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    print ("Degbug: projects %s",project)
    connection.close()
    return json_projects

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
