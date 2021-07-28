#!/usr/bin/env python3

import sys
import time
import json

import mariadb

import logger

#load our config file
with open("config.json") as json_data_file:
	config = json.load(json_data_file)

# Connect to MariaDB Platform
try:
	conn = mariadb.connect(
		user=config["recipeDB"]["user"],
		password=config["recipeDB"]["password"],
		host=config["recipeDB"]["host"],
		port=config["recipeDB"]["port"],
		database=config["recipeDB"]["database"]

	)
except mariadb.Error as e:
	logger.print_error(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

# Get Cursor
cur = conn.cursor(buffered=True)


def sql_textify(text, comma=True):
	"""Makes an input into a MYSQL format.\n
	int's will not have quotes\n
	str's will have quotes added\n
	commas are also added by default

	Args:
		text (int/str): the text or int to surrounded in quotes
		comma (bool, optional): should a comma be added? Defaults to True.

	Returns:
		str: the string for you sql insert
	"""
	if type(text) == int and comma:
		return str(text) + ', '
	elif type(text) == int and not comma:
		return str(text) + ')'

	elif str(text) == '' and comma:
		return 'null, '
	elif str(text) == '' and not comma:
		return 'null)'

	elif comma:
		return "'" + str(text).replace("'", "''") + "', "
	else:
		return "'" + str(text).replace("'", "''") + "')"


def run_sql(statement):
	"""Runs a MYSQL insert/update/delete statement\n
	Logs the statement run and the run time

	Args:
		statement (str): the SQL script  to run

	Returns:
		mariadb.connect.cursor: the cursor object with your results
	"""	
	logger.log_sql_statement(statement)
	start_time = time.time()
	try:
		cur.execute(statement)
		conn.commit()
	except mariadb.Error as e:
		logger.print_error(f"Error: {e}")

	end_time = time.time()
	logger.log_sql_result(cur.rowcount,  end_time - start_time)
	return cur


def run_sql_select(statement):
	"""Runs a MYSQL select statement\n
	Logs the statement run and the run time

	Args:
		statement (str): the SQL select string to run

	Returns:
		mariadb.connect.cursor: the cursor object with your results
	"""	
	logger.log_sql_statement(statement)
	start_time = time.time()
	try:
		cur.execute(statement)
	except mariadb.Error as e:
		logger.print_error(f"Error: {e}")

	end_time = time.time()
	logger.log_sql_result(cur.rowcount,  end_time - start_time)
	return cur


def insert_recipe(recipe):
	insert_recipe = "call sp_upsert_recipe("\
		+ sql_textify(recipe['id'])\
		+ sql_textify(recipe['recipe'])\
		+ sql_textify(recipe['category1'])\
		+ sql_textify(recipe['category2'])\
		+ sql_textify(recipe['category3'])\
		+ sql_textify(recipe['author'])\
		+ sql_textify(recipe['rating'])\
		+ sql_textify(recipe['reviews'])\
		+ sql_textify(recipe['prep Time'])\
		+ sql_textify(recipe['cook Time'])\
		+ sql_textify(recipe['servings'])\
		+ sql_textify(recipe['yield'], False)
	return run_sql(insert_recipe)


def insert_directions(recipe):
	for d in recipe["directions"]:
		insert_direction = "call sp_insert_direction("\
			+ sql_textify(recipe['id'])\
			+ sql_textify(d)\
			+ sql_textify(recipe['Directions'][d], False)
		run_sql(insert_direction)


def insert_ingredient(recipe):
	for i in recipe["ingredients"]:
		insert_ingredient = "call sp_insert_ingredient("\
			+ sql_textify(recipe['id'])\
			+ sql_textify(i['amount'])\
			+ sql_textify(i['unit_name'])\
			+ sql_textify(i['ingredient_name'], False)
		run_sql(insert_ingredient)


def insert_nutrition(recipe):
	for n in recipe["nutrition"]:
		insert_nutrition = "call sp_insert_nutrition("\
			+ sql_textify(recipe['id'])\
			+ sql_textify(n['amount'])\
			+ sql_textify(n['name'])\
			+ sql_textify(n['daily_value'], False)
		run_sql(insert_nutrition)


def get_recipes():
	return run_sql_select("call sp_get_all_recipes")


def get_recipe(recipe_id):
	return run_sql_select("call sp_get_recipe_by_id (" + str(recipe_id) + ")")


def get_directions(recipe_id):
	return run_sql_select("call sp_get_directions_by_id (" + str(recipe_id) + ")")


def get_ingredients(recipe_id):
	return run_sql_select("call sp_get_ingredients_by_id (" + str(recipe_id) + ")")


def get_nutrition(recipe_id):
	return run_sql_select("call sp_get_nutrition_by_id (" + str(recipe_id) + ")")
