from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'offersdb'
app.config['MONGO_URI'] = 'mongodb://iram:iram2018@ds157799.mlab.com:57799/offersdb'


mongo = PyMongo(app)

@app.route('/',methods=["GET"])
def status():
    return "Welcome to Iram's site"

@app.route('/framework', methods=['GET'])
def get_all_frameworks():
    framework = mongo.db.offers 

    output = []

    for q in framework.find():
        
        output.append({"_id": q["_id"], "preco_change":q["preco_change"],
    "faixa_id":q["faixa_id"],
    "seller":q["seller"],
    "categoria_id":q["categoria_id"] ,
    "date":q["date"],
    "supermarket":q["supermarket"] ,
    "preco":q["preco"],
    "product":q["product"] ,
    "supermarket_id":q["supermarket_id"]})
        #print(type(q["product"]))
    return jsonify({'result':output})
        #output.append()
##        output.append({'name' : q['name'], 'language' : q['language']})
##
##    return jsonify({'result' : output})

@app.route('/product/<name>', methods=['GET'])
def get_one_framework(name):
    framework = mongo.db.offers
    
    #for q in framework.find({"product": {"$regex": '/*'+name+'*/'}}):
    result=[]
    for q in framework.find({"product": {'$regex':name,'$options':'i'}}):
       # print(type(q))
        #   print(q)
        result.append(q)
    if len(result)!=0:
        return jsonify({"result":result})
    else:
        return "no matching results"

@app.route('/seller/<name>',methods=["GET"])
def seller_record(name):
    framework=mongo.db.offers
    q=framework.find_one({'seller':name})
    print(type(q))
    your_keys=["_id", "preco_change","faixa_id","seller","categoria_id" ,"date","supermarket" ,"preco","product","supermarket_id"]
    out_dict = { your_key: q[your_key] for your_key in your_keys }
    if out_dict:
        return jsonify(out_dict)
    else:
        return "No seller found for {}".format(name)

