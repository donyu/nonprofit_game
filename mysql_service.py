#!/usr/bin/python 
import MySQLdb
import json
import sys
connection = MySQLdb.connect(host="us-cdbr-east-04.cleardb.com",
user="b2699bab0d03bc",
passwd="92c968bb",
db="heroku_62b297a4786cfb1")
cursor = connection.cursor()

def get_user(user_data):
	username = user_data['username']
	password = user_data['password']
	result = cursor.execute("SELECT name FROM users WHERE name=%s && password=%s", (username, password))
	if result:
		return username 
	return None

def add_user(user_data):
	username = user_data['username']
	password = user_data['password']
	email = user_data['email']
	result = cursor.execute("SELECT email FROM users WHERE email=%s", (email))
	if result:
		return False
	else:
		print user_data
		cursor.execute("INSERT INTO users (name, password, email) VALUES(%s, %s, %s)", (username, password, email))
		connection.commit()
		return True

def increment_points(user_data, pointAmount):
	username = user_data['username']
	password = user_data['password']
	email = user_data['email']
	result = cursor.execute("UPDATA users SET points + " + pointAmount + " WHERE email = '" + email + "'")
	if !result:
		return False
	else:
		return True
