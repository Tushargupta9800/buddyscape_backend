from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import uuid 

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://buddyscape:buddyscape@buddyscape.es3qbjh.mongodb.net/?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.errorhandler(404)
def page_not_found(error):
    return {"error" : "Page Not Found"}

@app.route('/', methods = ['GET'])
def getImage(filename):
    return "hello"

if __name__ == '__main__':
    app.run(debug = True)
