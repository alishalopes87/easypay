from synapsepy import Client

ip = '98.210.168.175'

client = Client(
    'client_id_vWMQ8S0IYduxPObKUBl4f1Xm9oaNyj6pH0r5T7Lt', # your client id
    'client_secret_rn0GRehEtOBjJIPAYwXH4ZQS107DzbWU6LNgyfcm', # your client secret
    'e7261db4f6f1751399bbbf5f01401866"',
    '98.210.168.175',
    False,
    False
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
	session["user_id"] = new_user.user_id
	return new_user

def get_user():
	pass

