var conn = new Mongo();
var db = conn.getDB("verSchema");

db.SchemaUser.insert({userId: "someUser", SchemaKeys: ["firstschema"]});
db.Schemas.insert({key: "firstschema", schema: "{name: string, complaint: string, compDate: Date}"});
