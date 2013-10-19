from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/login', methods=['POST'])
#def login():
#    pass
    
if __name__ == '__main__':
    app.run(port=8080)
