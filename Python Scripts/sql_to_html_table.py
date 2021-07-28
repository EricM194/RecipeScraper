#!/usr/bin/env python3

def sql_to_html_table(cursor):
	"""converts a mysql cursor into a html table as a str

	Args:
		cursor (mariadb.connect.cursor): The cursor object with a select result

	Returns:
		str: a string contain you html table with headers
	"""
	html_table = ''
	html_table = html_table + \
		'<link rel="stylesheet" type="text/css" media=screen href="/static/materialize.css" />'
	html_table = html_table + '<table>\n'

	html_table = html_table + '<tr>\n'  # headers
	for h in cursor.description:
		html_table = html_table + '<th>' + h[0] + '</th>\n'
	html_table = html_table + '</tr>\n'  # end headers

	for r in cursor:
		html_table = html_table + '<tr>\n'
		html_table = html_table + '<td><a href="/recipe/' + \
			str(r[0]) + '">' + str(r[0]) + '</a></td>\n'
		for d in r[1:]:
			html_table = html_table + '<td>' + str(d) + '</td>\n'
		html_table = html_table + '</tr>\n'  #

	html_table = html_table + '</table>'

	return html_table
