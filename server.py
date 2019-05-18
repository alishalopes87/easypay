import os
from synapsepy import Client
from flask import (Flask, render_template, redirect, request, flash, session,jsonify, abort)
from setup import *
from model import *
app = Flask(__name__)

app.secret_key = "ABC"


@app.route('/')
def index():
	"""Homepage"""


	return render_template('index.html')

@app.route('/register', methods=["POST"])
def register_process():
	email = request.form["email"]
	name = request.form["name"]
	phone_number = request.form["phone_number"]
	password = request.form["password"]

	new_user = createUser(email, phone_number, name)
	user = User(
				email=email,name=name, 
				password=password, synapse_id=new_user.user_id,
				phone_number=phone_number
				)
	user.save()

	#TODO: ADD USER TO DB
	#direct user to their page

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar


    app.run(port=5000, host='0.0.0.0')