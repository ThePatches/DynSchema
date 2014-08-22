from flask import Flask
import varies
import json

app = Flask(__name__, static_url_path='')
anObject = varies.makeObject(u"{\"name\": \"string\", \"comment\": \"string\", \"target\": \"date\", \"amount\": \"decimal\"}")
	

@app.route("/")
def root():
	return app.send_static_file("index.html")
	#return "Hello world!"

import os
@app.route("/js/<path:path>")
def static_proxy(path):
	return app.send_static_file(os.path.join('js', path))


@app.route("/schema/<inKey>")
def get_object(inKey): #gets a basic schema
	#return "arrived!"
	interface = varies.VarSchema()
	interface.connect()
	theSchema = interface.getSchema(inKey)
	if theSchema is None:
		return "No schema found!"
	else:
		print theSchema
		return theSchema


if __name__ == "__main__":
	app.run()
