from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
# db = SQLAlchemy(app)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(debug=True) 