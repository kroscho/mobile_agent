from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
import json
import os, sys

path_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(path_dir)


from services.spqrqlQueries.main import SparqlQueries
from src.utils import typeData

app = Flask(__name__)
CORS(app)

@app.get('/api/pollen/books_by_name')
def api_get_books_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Books)
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return data

@app.get('/api/pollen/article_by_name')
def api_get_article_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Articles)
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return data

@app.get('/api/pollen/sites_by_name')
def api_get_sites_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Sites)
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return data

@app.get('/api/pollen/authors_by_name')
def api_get_authors_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Authors)
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return data




app.env = 'development'

app.run(port=5000, host='0.0.0.0', debug=True)