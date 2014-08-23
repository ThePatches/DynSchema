Variable Schema Proof of Concept
================================

This project is about implementing user-defined schemas using mongodb and either python or NodeJS.

#Setup
You must install mongodb and python 2.7 (should be installed already if you're running OSX), and then you have to perform database setup. Simply run `mongo dbsetup.js` on your local installation (assuming that you've got no permissions restrictions in place) to preconfigure the database.

##Python

The python project has the following dependencies (installed via pip):
+ pymongo
+ flask

Once you've installed the proper packages, you can run the application using `python app.py`

###About the Python Implementation

Most of the real stuff is in varies.py and app.py. **varies.py** contains an interface for mongodb and arranges the construction of the database objects. **app.py** uses routing to determine which operation is being performed.

###Testing
1. Run the app
1. Go to http://localhost:5000/ and add a new schema
1. Browse to http://localhost:5000/new/<schema_name> and fill out the form
1. Click the _Add Entry_ Button on the Entry adding page
1. Check the mongo database for the added item

Note: I am going to flesh out the back half (which is loading the records based on the associated schema, but more on that later)
