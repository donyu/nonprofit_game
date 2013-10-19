from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	if 'username' in session:
		return render_template('dashboard.html')
	else:
		return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	pass

@app.route('/register', methods=['POST'])
def register():
	pass
    
if __name__ == '__main__':
    app.run(port=8080)
