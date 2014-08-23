from flask import Flask, request, render_template
import varies
import json

app = Flask(__name__, static_url_path='')
anObject = varies.makeObject(u"{\"name\": \"string\", \"comment\": \"string\", \"target\": \"date\", \"amount\": \"decimal\"}")
mongoTunnel = varies.VarSchema()
mongoTunnel.connect()
	

@app.route("/")
def root():
	return app.send_static_file("index.html")

import os
@app.route("/js/<path:path>")
def static_proxy(path):
	return app.send_static_file(os.path.join('js', path))


@app.route("/new/<inKey>")
def get_object(inKey): #gets a basic schema
	print inKey
	theSchema = mongoTunnel.getSchema(inKey)
	if theSchema is None:
		return "No schema found!"
	else:
		print theSchema
		schema = "someSchema"
		fullObject = {}
		fullObject["key"] = inKey
		fullObject["schema"] = json.loads(theSchema)
		fullObject["object"] = varies.makeObject(theSchema)
		return render_template("schema.html", schema=fullObject) 

@app.route("/add/schema", methods=["POST"])
def add_schema():
	formData = request.form
	nKey = formData["key"]
	mongoTunnel.addSchema(nKey, formData["schema"])	
	return True

@app.route("/add/object", methods=['POST'])
def add_object():
	#print "Got there!"
	formData = request.form;
	print formData
	nKey = formData["key"]
	print nKey
	return "Something" 

@app.route("/Temp")
def temp_func():
	return render_template("temp.html")

if __name__ == "__main__":
	app.run(debug=True)
