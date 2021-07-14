#!/usr/bin/env python3

import json
from time import sleep

import logger
import recipe_db_connector
from all_recipes_scraper import scrape_recipes

base_url = 'https://www.allrecipes.com/recipe/'
max_id = 0
url_number = 0
result = {}

with open('data.json', 'r') as json_file:
	data = json.load(json_file)
	for i in data:
		if max_id < i['id']:
			max_id = i['id']

url_number = max_id + 1

for i in range(1):

	scraped_recipe = scrape_recipes(base_url + str(url_number))

	if scraped_recipe == 404:
		result = {"id": url_number, "result": '404'}
		logger.print_info('recipe id:' +  str(url_number) + '404')

	elif scraped_recipe == 'some other issue':
		result = {"id": url_number, "result": 'some other issue'}
		logger.print_info('recipe id:' + str(url_number) + 'some other issue')

	else:
		if recipe_db_connector.insert_recipe(scraped_recipe).rowcount != 2: #insert returns 1, update returns 2
			recipe_db_connector.insert_directions(scraped_recipe)
			recipe_db_connector.insert_ingredient(scraped_recipe)
			recipe_db_connector.insert_nutrition(scraped_recipe)

		result = {"id": url_number, "result": 'added'}
		logger.print_info('recipe id: ' + str(scraped_recipe['Id']) +
							' added with name: ' + scraped_recipe['Recipe'])         

	with open('data.json', 'r+') as json_file:
		data.append(result)
		json_file.write(json.dumps(data, indent=4))

	url_number = url_number + 1
	sleep(5)
