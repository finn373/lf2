import pymysql.cursors
import os
import sys
import pprint

def clear_console_window():
	os.system('cls' if os.name=='nt' else 'clear')

def create_connection_to_database(host, username, password, databasename, port, charset):
	return pymysql.connect(host=host,
						user=username,
						password=password,
						database=databasename,
						charset=charset,
						cursorclass=pymysql.cursors.DictCursor)

print("Hello Connecting to your Database :D")

try:
	connection = create_connection_to_database()#Hier kommen die Info der db rein als Argument

	with connection.cursor() as cursor:
		cursor.execute('SELECT * from test')
		rows = cursor.fetchall()
		connection.close()
		print(rows)

except pymysql.err.OperationalError:
	print('cant connect to db')