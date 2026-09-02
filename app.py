import os
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

API_DATA = {"status": "sucess", "version": "1.0", "data": "JSON Content"}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api', methods['GET'])
def get_api():
	return jsonify(API_DATA)

if __name__== '__main__':
	app.run(debug=True, port=5000)
