import os
import time
from flask import render_template, request
from arielApps import app

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/store")
def store():
    return render_template('store.html')

def refresh_token():
	refresh_token = '5Aep861j70kdjF1ZXOlJprYw7Hgh4jIXtx9hzgnunGvtgs_dsl.oAQbUsYB.vbwun4wRLz1BoJs7EPD55JBAT8t'
	URL = 'https://login.salesforce.com/services/oauth2/token'
	PARAMS = {
	'client_id':'3MVG9KsVczVNcM8y7u697HlH_iclV50xS8TAylDWAoNQbEfUDqcPTZbjB8KSRly8Z8HaWILcPeWtcz5vhk3R5',
	'client_secret':'11468928533351650',
	'grant_type':'refresh_token',
	'refresh_token':refresh_token
	}
	r = requests.post(url = URL, params = PARAMS)
	data = json.loads(r.text)
	return data