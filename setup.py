from synapsepy import Client
from flask import (Flask, render_template, redirect, request,session)

ip = '98.210.168.175'

client = Client(
    'client_id_vWMQ8S0IYduxPObKUBl4f1Xm9oaNyj6pH0r5T7Lt', # your client id
    'client_secret_JzVMFQwf0r65EAUk7nm2HPsc1bZgNT8viLCI9Kq4', # your client secret
    'e7261db4f6f1751399bbbf5f01401866"',
    '98.210.168.175',
    True,
    True
)

# env = {
#   client_id: 'client_id_vWMQ8S0IYduxPObKUBl4f1Xm9oaNyj6pH0r5T7Lt',
#   client_secret: 'client_secret_ANdhYJx3lm0Fy4kgBs7jCc6EtLvUi1ru5oeMWPDI',
#   fingerprint: '5cddb17e14ddee0064a165a3',
#   ip_address: '127.0.0.1',
#   #isProduction boolean determines if production (true) or sandbox (false) endpoint is used
#   isProduction: false
# }

# client = Client(env)

#"e7261db4f6f1751399bbbf5f01401866"
def createUser(email,phone_number,name):
	print(dir(client))
	print(client.client_id, client.client_secret)
	ip = "98.210.168.175"
	fingerprint = "static_pin"
	body = {
  	"logins": [
    {
      "email": email
	    }
	  ],
	  "phone_numbers": [
	    phone_number
	  ],
	  "legal_names": [
	    name
	  ],
	}
	new_user = client.create_user(body, ip)

	print(dir(new_user))
	refresh = new_user.refresh()
	return new_user, new_user.id, refresh

def get_oauth(user,refresh):

	body = {
		"refresh_token": refresh,
		 "validation_pin":"123456",
		"scope":[
		"USER|PATCH",
		"USER|GET",
		"NODES|GET",
		"NODES|POST",

		]
	}

	oauth = user.oauth(body)
	print(oauth)
	return oauth

def issue_public_key():
	scope = [
	  "USERS|POST",
	  "USER|PATCH",
	  "NODES|POST",
	]
	pubkey = client.issue_public_key(scope)
	return pubkey

def create_url(oauth_key, pubkey):
	 "https://uat-uiaas.synapsefi.com/link?oauth_key={}&public_key=&success_uri=SUCCESS&failure_uri=FAILURE".format(OAUTH_KEY,PUBLIC_KEY,)

def post_credentials(user):
	body = {
	  "type": "ACH-US",
	  "info":{
	    "bank_id":"synapse_good",
	    "bank_pw":"test1234",
	    "bank_name":"fake"
	  }
	}
	# user = session.get("user")
	return user.create_node(body)

def get_user(user_id):

	user = client.get_user(user_id, full_dehydrate=True)
	return user
# 594e606212e17a002f2e3251
# 5ce0cf99c9f52d006691eda3
def create_transaction(user):
	# node_id = '594e606212e17a002f2e3251'
	body = {
	  "to": {
	    "type": "ACH-US",
	    "id": "594e6e6c12e17a002f2e39e4"
	  },
	  "amount": {
	    "amount": 20.1,
	    "currency": "USD"
	  },
	  "extra": {
	    "ip": "192.168.0.1"
	  }
	}

	return user.create_trans(body)
def verifyMFA(user):

	body = {
    "access_token":"fake_cd60680b9addc013ca7fb25b2b704ba82d3",
    "mfa_answer":"test_answer"
	}

	return user.ach_mfa(body)

