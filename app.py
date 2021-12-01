from flask import Flask, render_template, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_utils
from bson.objectId import ObjectId



app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/BD_netflix'
mongo = PyMongo(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def crear_usuario():
    # received Dato
    print(request.json)
    
    return {'message': 'received'}

@app.route("/account")
def account():
    return render_template('signIn.html')

if __name__ == '__main__':
    app.run(debug=True)