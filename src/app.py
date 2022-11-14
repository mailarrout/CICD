from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	title = "The Scalper"
	return "Hello, World!"

if __name__ == "__main__":
	app.run()