import os
from flask import Flask, request
from flask_cors import CORS
import requests as req
from requests.auth import HTTPBasicAuth

MG_DOMAIN = os.getenv('MG_DOMAIN', "REPLACE_ME_YOUR_DOMAIN")
MG_TO = os.getenv('MG_TO', "REPLACE_ME_WITH_YOUR_EMAIL")
MG_KEY = os.getenv('MG_KEY', "REPLACE_ME_YOUR_KEY")

FRONTEND_URI = os.getenv('FRONTEND_URI', '')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": [FRONTEND_URI]}})

@app.route('/', methods=['POST'])
def contact_proxy():
    endpoint = 'https://api.mailgun.net/v3/{}/messages'.format(MG_DOMAIN)
    email = request.get_json()
    email['to'] = MG_TO
    email['text'] = "{0} says...\n {1}".format(email['name'], email['text'])
    success = req.post(endpoint, auth=('api', MG_KEY), data=email)
    return success.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
