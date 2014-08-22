from pymongo import MongoClient
import json
from datetime import date

# First version: Let's establish some constants

dbName = "verSchema"
SchemaUsers = "SchemaUsers"
SchemaColl = "Schemas"

class VarSchema:
	__host = "localost"
	__port = 27017
	__client = None
	__db = None

	def __init__(self, host="localhost", port=27017):
		self.__host = host
		self.__port = port
	
	def getPort(self):
		return self.__port

	def getHost(self):
		return self.__host

	def connect(self):
		try:
			self.__client = MongoClient(self.__host, self.__port)
			self.__db = self.__client[dbName]  
		except:
			print "Failed to connect!"
			self.__cliet = None
			self.__db = None

	def getSchema(self, inKey):
		""" Gets a schema that matches the provided key """
		if inKey is None or inKey == "":
			return None # TODO: Make this the generic case 
		else:
			collection = self.__db[SchemaColl]
			schObj = collection.find_one({"key": inKey})
			if schObj is None:
				return None
			else:
				return schObj["schema"]

	def addSchema(self, inKey, inSchema):
		""" Adds a schema to the database """
		# TODO: Add error handling here
		collection = self.__db[SchemaColl]
		collection.insert({"key": inKey, "schema": inSchema})

def makeObject(inSchema):
	""" Makes an Object from a Unicode String """
	outValue = {}
	inJSON = json.loads(inSchema)
	for key in inJSON:
		nKey = str(key)
		if inJSON[key] == "string":
			outValue[nKey] = "empty"
		elif inJSON[key] == "date": 
			outValue[nKey] = date.today().isoformat()
		elif inJSON[key] == "integer":
			outValue[nKey] = 0
		elif inJSON[key] == "decimal":
			outValue[nKey] = 0.0
		else:
			pass

	return outValue #str(outValue) 

def convertToString(inObject): # actually, we can probably do this in JavaScript
	""" Converts the passed in Object into a unicode string """	
	pass	


if __name__ == "__main__":
	nSchema = VarSchema()
	#print nSchema.getSchema(None)
	#nSchema.connect()
	#print nSchema.getSchema("firstschema")
	#nSchema.addSchema("thirdschema", "{name: string, comment: string, target: string}")
	#print nSchema.getSchema(None)
	#anObject = makeObject(u"{\"name\": \"string\", \"comment\": \"string\", \"amount\": \"date\"}")
	nSchema.connect()
	aSchema = nSchema.getSchema("myschema")
	#anObject = makeObject(aSchema["schema"])
	print aSchema
	
