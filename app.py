from flask import Flask, render_template, redirect, request, session, flash
import simplejson as JSON
import mysql_service

app = Flask(__name__)

# set the secret key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/', methods=['GET'])
def index():
	if 'username' in session:
		return render_template('dashboard.html')
	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	user = mysql_service.get_user(JSON.loads(request.data))
	print "hello"
	print user
	if user:
		session['username'] = user
		return 'User Logged In', 200
	else:
		return 'Log In Unsuccessful', 201

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/register', methods=['POST'])
def register():
	mysql_service.add_user(JSON.loads(request.data))
	user = mysql_service.get_user(JSON.loads(request.data))
	if user:
		session['username'] = user
		return 'User Logged In', 200
	else:
		return 'Log In Unsuccessful', 201
    
if __name__ == '__main__':
    app.run(port=8080)

