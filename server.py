import os
from synapsepy import Client
from flask import (Flask, render_template, redirect, request, flash, session,jsonify, abort)
from setup import createUser, client, get_oauth, issue_public_key, get_user, post_credentials
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

	new_user,synapse_id,refresh = createUser(email, phone_number, name)
	oauth = get_oauth(new_user,refresh)
	pubkey = issue_public_key()

	user = User(
				email=email,name=name, refresh=refresh,
				password=password, synapse_id=synapse_id,
				phone_number=phone_number
				)
	user.save()
	# session["user"] = user
	return render_template('success.html', user=user)


@app.route('/login', methods=['POST'])
def login_process():
    """Process user login"""


    email = request.form["email"]
    password = request.form["password"]
    #dont store passwords

    user = User.query.filter(User.email==email).first()
    print(dir(user.mongo_id))
    if not user:
        flash("No such user")
        return redirect("/register")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.synapse_id

    flash("Logged in")
    return render_template('success.html', user=user)

@app.route('/bank-login')
def bank_login():

	return render_template('bank_login.html')

@app.route('/bank-success',methods=["POST"])
def submit_bank():
	username = request.form["username"]
	password = request.form["password"]
	bank_name = request.form["bank_name"]

	user_id = session.get("user_id")
	user = get_user(user_id)

	credentials = post_credentials(user)

	print(credentials)

	return render_template("bank.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar


    app.run(port=5000, host='0.0.0.0')