from flask import Flask, jsonify, request, make_response
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
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/article_by_name')
def api_get_article_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Articles)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/sites_by_name')
def api_get_sites_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Sites)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/authors_by_name')
def api_get_authors_by_name():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByNames(title, typeData.Authors)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/books_by_theme')
def api_get_books_by_theme():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByTheme(title, typeData.Books)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/article_by_theme')
def api_get_article_by_theme():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByTheme(title, typeData.Articles)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/sites_by_theme')
def api_get_sites_by_theme():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByTheme(title, typeData.Sites)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response

@app.get('/api/pollen/authors_by_theme')
def api_get_authors_by_theme():
    title = request.args.get('search', '').replace(' ', '_')
    print(title)
    ont = SparqlQueries()
    data = ont.getDataByTheme(title, typeData.Authors)
    response = make_response(json.dumps({
        'statusCode': 200,
        'data': data
    })), 200
    print(response)
    return response




app.env = 'development'

app.run(port=5000, host='0.0.0.0', debug=True)