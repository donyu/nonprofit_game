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
		cursor.execute("INSERT INTO users (name, password, email) VALUES(%s, %s, %s)", (username, password, email))
		connection.commit()
		return True

def inc_points(user_data, pointAmount):
	username = user_data['username']
	password = user_data['password']
	email = user_data['email']
	query = "UPDATE users SET points = points + " + str(pointAmount) + " WHERE email = '" + email + "'"
	result = cursor.execute(query)
	if not result:
		return False
	else:
		connection.commit()
		return True

def inc_level(user_data):
	email = user_data['email']
	query = "UPDATE users SET level = level + 1 WHERE email = '" + email + "'"
	print query
	result = cursor.execute(query)
	if not result:
		return False
	else:
		connection.commit()
		return True

def get_question(user_data):
	questionNumber = user_data['qcomplete']
	query = "SELECT * FROM questions WHERE id = '" + questionNumber + "'"
	result = cursor.execute(query)
	question = cursor.fetchall()
	if not result:
		return None

	query = "SHOW COLUMNS FROM questions"
	result = cursor.execute(query)
	columnNames = cursor.fetchall()
	columns = [] 
	for arrays in columnNames:
		columns.append(str(arrays[0]))

	question_dict = dict()
	i = 0
	for values in columns:
		question_dict[values] = question[0][i]
		i += 1
	
	return question_dict

def check_answer(question, answer):
	query = "SELECT answer FROM questions WHERE id = '" + str(question['id']) + "'"
	result = cursor.execute(query)
	realAnswer = cursor.fetchall()
	return answer == realAnswer[0][0]
	
def rankByPts():
	query = "SELECT * FROM users ORDER BY points DESC LIMIT 0, 101"
	result = cursor.execute(query)
	rankings = cursor.fetchall()
	userStats = dict()
	for users in rankings:
		userStats[users[1]] = users[4]

	return userStats

user_data = {'username': 'b', 'password': 'asdf', 'email': 'b@b.com', 'qcomplete': '0'}
question_dict = get_question(user_data)
questionObj = {'answer': 'the world is cool', 'question_text': 'welcome to the world', 'type': 'tf', 'id': 0L, 'point_value': 100L}
answer = 'the world is cool'
right = check_answer(questionObj, answer)
rankByPts()
