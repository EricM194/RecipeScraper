#!/usr/bin/env python3

import json

import recipe_db_connector


def sql_to_json(cursor):
	columns = [column[0] for column in cursor.description]
	results = []
	for row in cursor.fetchall():
		results.append(dict(zip(columns, row)))
		del results[-1]['ID']
	return results


def sql_to_recipe_object(recipe_id):
	cursor = recipe_db_connector.get_recipe(recipe_id)
	results ={}
	columns = [column[0] for column in cursor.description]
	for row in cursor.fetchall():
		results = dict(zip(columns, row))
		results['Created Date'] = results['Created Date'].strftime('%Y-%m-%d %H:%M:%S')
		results['Last Modified Date'] = results['Last Modified Date'].strftime('%Y-%m-%d %H:%M:%S')
	return results


def sql_to_directions_list(recipe_id):
	return sql_to_json(recipe_db_connector.get_directions(recipe_id))


def sql_to_ingredients_list(recipe_id):
	return sql_to_json(recipe_db_connector.get_ingredients(recipe_id))

def sql_to_nutrition_list(recipe_id):
	return sql_to_json(recipe_db_connector.get_nutrition(recipe_id))


def sql_to_whole_recipe_json(recipe_id):
	r = sql_to_recipe_object(recipe_id)

	if r:
		r['directions'] = sql_to_directions_list(recipe_id)
		r['ingredients'] = sql_to_ingredients_list(recipe_id)
		r['nutrition'] = sql_to_nutrition_list(recipe_id)
		return json.dumps(r, indent=4)
		
	else:
		return None
