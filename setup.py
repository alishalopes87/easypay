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


def createUser(email,phone_number,name):
	print(dir(client))
	print(client.client_id, client.client_secret)
	ip = "98.210.168.175"
	fingerprint = "e7261db4f6f1751399bbbf5f01401866"
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

def get_oauth(user):

	body = {
		"refresh_token":"refresh_Y5beJdBLtgvply3KIzrh72UxWMEqiTNoVAfDs98G",
		 "validation_pin":"123456",
		"scope":[
		"USER|PATCH",
		"USER|GET",
		]
	}

	oauth = user.oauth(body)
	print(oauth)
	return oauth
