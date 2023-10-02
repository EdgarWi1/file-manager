from flask import Flask, render_template

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

@app.route("/")
# @app.route("/login")
# def index():
# 	return render_template("login.html")

# @app.route("/sidebar")
# def index():
# 	return render_template("assets/sidebar.html")

@app.route("/dashboard")
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(debug=True)