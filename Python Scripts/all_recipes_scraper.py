#!/usr/bin/env python3

import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

import logger


def timeToMinutes(time):
	minutes = 0

	# days
	try:
		minutes = minutes + \
			int(re.search('(\d*)(?=\sdays)', time).group(0)) * 60 * 24
	except AttributeError:
		minutes = minutes + 0

	# hours
	try:
		minutes = minutes + \
			int(re.search('(\d*)(?=\shrs)', time).group(0)) * 60
	except AttributeError:
		minutes = minutes + 0

	# minutes
	try:
		minutes = minutes + int(re.search('(\d*)(?=\smins)', time).group(0))
	except AttributeError:
		minutes = minutes + 0

	return minutes


recipe = {}


def scrape_recipes(url):
	data = requests.get(url)

	if data.status_code == 404:
		return 404

	try:
		soup = BeautifulSoup(data.text, 'html.parser')

		breadcrumb_html = soup.find_all('span', {'class': 'breadcrumbs__title'})
		breadcrumb = []

		count = 0
		for bc in enumerate(breadcrumb_html):
			breadcrumb.append(breadcrumb_html[count].text.strip())
			count = count + 1

		try:
			recipe['category1'] = breadcrumb[2]
		except:
			recipe['category1'] = ''

		try:
			recipe['category2'] = breadcrumb[3]
		except:
			recipe['category2'] = ''

		try:
			recipe['category3'] = breadcrumb[4]
		except:
			recipe['category3'] = ''

		recipe['id'] = int(url.split('/')[-1])
  
		recipe['recipe'] = soup.find('h1', {'class': 'headline heading-content'}).text.strip()
		recipe['author'] = soup.find('span', {'class': 'author-name authorName'}).text.strip()
		recipe['rating'] = soup.find_all('span', {'class': 'review-star-text'})[0].text.strip().split(': ')[1].split(' ')[0]
		recipe['reviews'] = int(soup.find('span', {'class': 'ugc-ratings-item'}).text.strip().split(' ')[0].replace(',', ''))

		meta_data_html = soup.find_all('div', {'class': 'recipe-meta-item'})
		meta_data = {}

		for md in meta_data_html:
			meta_data[md.find('div', {'class': 'recipe-meta-item-header'}).text.strip().split(':')[0]] = md.find('div',
																												 {'class': 'recipe-meta-item-body'}).text.strip()

		try:
			recipe['prep Time'] = timeToMinutes(meta_data['prep'])
		except KeyError:
			recipe['prep Time'] = 0

		try:
			recipe['cook Time'] = timeToMinutes(meta_data['cook'])
		except KeyError:
			recipe['cook Time'] = 0

		try:
			recipe['servings'] = meta_data['Servings']
		except KeyError:
			recipe['servings'] = 0

		try:
			recipe['Yield'] = meta_data['Yield']
		except KeyError:
			recipe['yield'] = 0

		ingredients = []
		directions = {}
		nutrition = []


		# directions
		directions_html = soup.find('ul', {'class': 'instructions-section'}).find_all('li')
		step_number = 0
		for li in directions_html:
			directions[step_number + 1] = li.find('div', {'class': 'paragraph'}).find('p').text
			step_number = step_number + 1
		recipe['directions'] = directions
		
		# ingredients
		ingredients_html = soup.find('ul', {'class': 'ingredients-section'}).find_all('li')
		for li in ingredients_html:
			ingredient = {'amount': li.find('input')['data-init-quantity'],
							'unit_name': li.find('input')['data-unit'],
							'ingredient_name': li.find('input')['data-ingredient']}
			ingredients.append(ingredient)
		recipe['ingredients'] = ingredients

		# nutrition
		nutrition_rows = soup.find('div', {'class': 'nutrition-body'}).find_all('div', {'class': 'nutrition-row'})
		for nr in nutrition_rows:
			nutrition_item = {'name': nr.find('span', {'class': 'nutrient-name'}).text.strip().split(':')[0],
								'amount': nr.find('span', {'class': 'nutrient-value'}).text.strip()}
			try:
				nutrition_item['daily_value'] = nr.find('span', {'class': 'daily-value'}).text.strip().split(' ')[0]
			except AttributeError:
				nutrition_item['daily_value'] = ''
			nutrition.append(nutrition_item)
		recipe['nutrition'] = nutrition

		logger.print_info(str(recipe))
		return recipe
	except AttributeError:
		return 'some other issue'




def scrape_recipes2(url):
	data = requests.get(url)

	if data.status_code == 404:
		return 404

	try:
		soup = BeautifulSoup(data.text, 'html.parser')

		breadcrumb_html = soup.find_all('span', {'class': 'breadcrumbs__title'})
		breadcrumb = []

		count = 0
		for bc in enumerate(breadcrumb_html):
			breadcrumb.append(breadcrumb_html[count].text.strip())
			count = count + 1

		try:
			recipe['category1'] = breadcrumb[2]
		except:
			recipe['category1'] = ''

		try:
			recipe['category2'] = breadcrumb[3]
		except:
			recipe['category2'] = ''

		try:
			recipe['category3'] = breadcrumb[4]
		except:
			recipe['category3'] = ''

		recipe['id'] = int(url.split('/')[-1])
  
		recipe['recipe'] = soup.find('h1', {'class': 'recipe-summary__h1'}).text.strip()
		recipe['author'] = soup.find('span', {'class': 'submitter__name'}).text.strip()
		recipe['rating'] = soup.find_all('div', {'class': 'rating-stars'})[0].attrs['data-ratingstars']
		recipe['reviews'] = int(soup.find('span', {'class': 'review-count'}).text.strip().split(' ')[0])

		meta_data_html = soup.find_all('div', {'class': 'prepTime__item'})
		meta_data = {}

		for md in meta_data_html:
			meta_data[md.find('div', {'class': 'recipe-meta-item-header'}).text.strip().split(':')[0]] = md.find('div',
																												 {'class': 'recipe-meta-item-body'}).text.strip()

		try:
			recipe['prep Time'] = timeToMinutes(meta_data['prep'])
		except KeyError:
			recipe['prep Time'] = 0

		try:
			recipe['cook Time'] = timeToMinutes(meta_data['cook'])
		except KeyError:
			recipe['cook Time'] = 0

		try:
			recipe['servings'] = meta_data['Servings']
		except KeyError:
			recipe['servings'] = 0

		try:
			recipe['Yield'] = meta_data['Yield']
		except KeyError:
			recipe['yield'] = 0

		ingredients = []
		directions = {}
		nutrition = []


		# directions
		directions_html = soup.find('ul', {'class': 'instructions-section'}).find_all('li')
		step_number = 0
		for li in directions_html:
			directions[step_number + 1] = li.find('div', {'class': 'paragraph'}).find('p').text
			step_number = step_number + 1
		recipe['directions'] = directions
		
		# ingredients
		ingredients_html = soup.find('ul', {'class': 'ingredients-section'}).find_all('li')
		for li in ingredients_html:
			ingredient = {'amount': li.find('input')['data-init-quantity'],
							'unit_name': li.find('input')['data-unit'],
							'ingredient_name': li.find('input')['data-ingredient']}
			ingredients.append(ingredient)
		recipe['ingredients'] = ingredients

		# nutrition
		nutrition_rows = soup.find('div', {'class': 'nutrition-body'}).find_all('div', {'class': 'nutrition-row'})
		for nr in nutrition_rows:
			nutrition_item = {'name': nr.find('span', {'class': 'nutrient-name'}).text.strip().split(':')[0],
								'amount': nr.find('span', {'class': 'nutrient-value'}).text.strip()}
			try:
				nutrition_item['daily_value'] = nr.find('span', {'class': 'daily-value'}).text.strip().split(' ')[0]
			except AttributeError:
				nutrition_item['daily_value'] = ''
			nutrition.append(nutrition_item)
		recipe['nutrition'] = nutrition

		logger.print_info(str(recipe))
		return recipe
	except AttributeError:
		return 'some other issue'