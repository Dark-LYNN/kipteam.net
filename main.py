from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/downloads')
def downloads():
  return render_template('downloads.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

if __name__ == "__main__":
	app.run(
		host='0.0.0.0', 
		port=(8080),
    debug=True
	)