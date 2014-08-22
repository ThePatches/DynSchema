from flask import Flask
import varies

app = Flask(__name__, static_url_path='')

@app.route("/")
def root():
	return app.send_static_file("index.html")
	#return "Hello world!"

if __name__ == "__main__":
	app.run()
