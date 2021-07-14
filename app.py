#!/usr/bin/env python3

import json

from flask import Flask
from flask import request as flask_request
from requests.api import request

import sql_to_recipe_json
from all_recipes_scraper import scrape_recipes
from recipe_db_connector import (get_directions, get_ingredients,
								 get_nutrition, get_recipe, get_recipes)
from sql_to_html_table import sql_to_html_table

app = Flask(__name__)


@app.route('/')
def index():
	"""Print 'Hello, world!' as the response body."""
	return 'Hello, world!'


@app.route('/recipes')
def recipes():
	cur = get_recipes()
	return sql_to_html_table(cur)


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):

	if(flask_request.headers.get('Content-Type')):
		type = flask_request.headers.get('Content-Type')
	else:
		type = flask_request.headers.get('Accept')


	if 'text/html' in type:

		cur = get_recipe(recipe_id)

		if cur.rowcount:
			html = '<title>Recipe ' + recipe_id + '</title>'
			html = html + sql_to_html_table(cur) + '<br><hr><br>'

			cur = get_ingredients(recipe_id)
			html = html + sql_to_html_table(cur) + '<br><hr><br>'

			cur = get_directions(recipe_id)
			html = html + sql_to_html_table(cur) + '<br><hr><br>'

			cur = get_nutrition(recipe_id)
			html = html + sql_to_html_table(cur)

			response = app.response_class(
				response=html,
				status=200,
				mimetype='text/html'
			)

		else:
			response = app.response_class(
				response='<link rel="stylesheet" type="text/css" media=screen href="/static/materialize.css" /><title>404 Not Found</title><p>recipe with ID: ' + recipe_id + ' was not found in the database</p>',
				status=404,
				mimetype='text/html'
			)
		return response

	elif 'application/json' in type:

		j = sql_to_recipe_json.sql_to_whole_recipe_json(recipe_id)

		if j:
			response = app.response_class(
				response=j,
				status=200,
				mimetype='application/json'
			)
		else:
			response = app.response_class(
				response=json.dumps(
				{"error": 'recipe with ID: ' + recipe_id + ' was not found in the database'}, indent=4),
				status=404,
				mimetype='application/json'
			)

		return response

	else:
		response = app.response_class(
			response=json.dumps(
				{"error": "'Accept' or 'Content-Type' header must be either 'application/json' or 'text/html', got " + type}, indent=4),
			status=400,
			mimetype='application/json'
		)
		return response


@app.route('/recipe/<recipe_id>/directions')
def directions(recipe_id):
	cur = get_directions(recipe_id)
	return sql_to_html_table(cur)


@app.route('/recipe/<recipe_id>/ingredients')
def ingredient(recipe_id):
	cur = get_ingredients(recipe_id)
	return sql_to_html_table(cur)


@app.route('/recipe/<recipe_id>/nutrition')
def nutrition(recipe_id):
	cur = get_nutrition(recipe_id)
	return sql_to_html_table(cur)


@app.route('/scrape/<recipe_id>/live')
def scrape(recipe_id):
	gather = scrape_recipes(
		'https://www.allrecipes.com/recipe/' + str(recipe_id))
	return gather


@app.errorhandler(404)
def page_not_found(e):
	# note that we set the 404 status explicitly
	return open('static/404.html').read(), 404


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
