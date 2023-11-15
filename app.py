from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
# db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        return redirect(url_for('dashboard.html'))
    
    return render_template('login.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(debug=True) 