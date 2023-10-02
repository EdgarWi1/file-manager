from flask import Flask, render_template

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

@app.route("/")
@app.route("/login")
def index():
	return render_template("sidebar.html")

if __name__ == '__main__':
	app.run(debug=True)