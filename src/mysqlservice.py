#!/usr/bin/python 
import MySQLdb
import json
import sys
connection = MySQLdb.connect(host="us-cdbr-east-04.cleardb.com",
user="b2699bab0d03bc",
passwd="92c968bb",
db="heroku_62b297a4786cfb1")
cursor = connection.cursor()

def userValidate(cursor, user_data):
	username = user_data["username"]
	password = user_data["password"]
	result = cursor.execute("SELECT name FROM users WHERE name='" + username + "' && password='" + password + "'")
	return password 

hashmap = {'username': 'don', 'password': 'passwerd'}
password = userValidate(cursor, hashmap)
print password
