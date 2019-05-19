from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from server import app 

app.config['MONGOALCHEMY_DATABASE'] = 'easypay'
db = MongoAlchemy(app)

class User(db.Document):
	name = db.StringField()
	synapse_id = db.StringField()
	email = db.StringField()
	password = db.StringField()
	phone_number = db.StringField()
	refresh = db.StringField()

	def get_oauth(self):
		body = {
		"refresh_token":"refresh_Y5beJdBLtgvply3KIzrh72UxWMEqiTNoVAfDs98G",
		"scope":[
		    "USER|PATCH",
		    "USER|GET",
		    ...
			]
		}

		return user.oauth(body)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
   
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")