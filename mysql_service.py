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
	result = cursor.execute("SELECT name FROM users WHERE name='" + username + "' && password='" + password + "'")
	if result:
		return username 
	return None

def register_user(user_data):
	username = user_data['username']
	password = user_data['password']
	email = user_data["email"]
	result = cursor.execute("SELECT email FROM users WHERE email='" + email + "'")
	if result:
		return False

	else:
		cursor.execute("INSERT INTO users (name, password, email) VALUES('" + username 
		+ "', '" + password + "', '" + email +"')")
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
