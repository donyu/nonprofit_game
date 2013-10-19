#!/usr/bin/python 
import MySQLdb #MySQL interfacing library

#Init connection to DB on Heroku server
connection = MySQLdb.connect(host="us-cdbr-east-04.cleardb.com",
user="b2699bab0d03bc",
passwd="92c968bb",
db="heroku_62b297a4786cfb1")
cursor = connection.cursor()

# Function: get_user
# Input: User object containing all information relating to what will be stored in the DB
# Output: Returns the username indicating if one exists by returning something
def get_user(user_data):
	username = user_data['username']
	password = user_data['password']
	result = cursor.execute("SELECT name FROM users WHERE name=%s && password=%s", (username, password))
	if result:
		return username 
	return None

# Function: add_user
# Input: User object as described above
# Output: Adds user to database when registered given a unique email and username
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

# Function: inc_points
# Input: User object and point amount by which to increment the user's point total
# Output: Modified database to reflect the increase in point total of users entry 

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

# Function: inc_level
# Input: User object
# Output: Auto-increments the user's level by one given the username/email

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

# Function: get_question
# Input: User Object
# Output: Returns a Question Dictionary containing all data corresponding to each type of question

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

# Function: check_answer
# Input: Question object and an answer in String format
# Output: Boolean representing if the answer was correct or not

def check_answer(question, answer):
	query = "SELECT answer FROM questions WHERE id = '" + str(question['id']) + "'"
	result = cursor.execute(query)
	realAnswer = cursor.fetchall()
	return answer == realAnswer[0][0]

# Function: rankByPts
# Input: No arguments. 
# Output: Returns a list of the top scoring users to represent in the leaderboard

def rankByPts():
	query = "SELECT * FROM users ORDER BY points DESC LIMIT 0, 101"
	result = cursor.execute(query)
	rankings = cursor.fetchall()
	userStats = dict()
	for users in rankings:
		userStats[users[1]] = users[4]

	return userStats
