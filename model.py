from flask import Flask
from flask_mongoalchemy import MongoAlchemy, BaseQuery
from server import app 

app.config['MONGOALCHEMY_DATABASE'] = 'easypay'
db = MongoAlchemy(app)

class MyCustomizedQuery(BaseQuery):

    def get_user(self,username):
        return self.filter(self.type.username == username)

class User(db.Document):
	name = db.StringField()
	synapse_id = db.StringField()
	email = db.StringField()
	password = db.StringField()
	phone_number = db.StringField()
	refresh = db.StringField()
	query_class = MyCustomizedQuery

def connect_to_db(app):
    """Connect the database to our Flask app."""
   
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")