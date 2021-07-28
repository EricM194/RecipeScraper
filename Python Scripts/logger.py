#!/usr/bin/env python3


from datetime import datetime

# special color codes
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
RED = '\u001b[31m'
CYAN = '\u001B[36m'
RESET = '\u001b[0m'


fmt = "%Y-%m-%d %H:%M:%S"


def log_sql_statement(statement):
	"""Print the given string to the console with "[SQL]  " prefixed
	Parameters:
		statement (String): The statement to log
	"""

	print(str(datetime.now().strftime(fmt)) + CYAN + ' [SQL]   ' + RESET + statement)


def log_sql_result(count, time):
	"""Print the given string to the console with "[SQL]  " prefixed
	Parameters:
		statement (String): The statement to log
	"""

	print(str(datetime.now().strftime(fmt)) + CYAN + ' [SQL]       ' + RESET + str(count) + ' Rows(s) affected in ' + str(round(time,3)) + ' s')
 
 
def print_info(info_message):
	"""Print the given string to the console with "[INFO]  " prefixed
	Parameters:
		info_message (String): The string to print to console
	"""

	print(str(datetime.now().strftime(fmt)) + ' [INFO]  ' + info_message)


def print_warn(warn_message):
	"""Print the given string to the console with a yellow "[WARN]  " prefixed
	Parameters:
		warn_message (String): The string to print to console
	"""

	print(str(datetime.now().strftime(fmt)) + YELLOW + ' [WARN]  ' + RESET + warn_message)


def print_error(error_message):
	"""Print the given string to the console with a red "[ERROR] " prefixed
	Parameters:
		error_message (String): The string to print to console
	"""

	print(str(datetime.now().strftime(fmt)) + RED + ' [ERROR] ' + RESET + error_message)
