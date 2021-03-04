# app.py

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
###############################################

from flask import Flask, redirect, render_template, url_for
from flask_dance.contrib.google import google, make_google_blueprint
# https://flask-dance.readthedocs.io/en/v0.14.0/providers.html#module-flask_dance.contrib.google


app =Flask(__name__)

app.config['SECRET_KEY'] = 'myPassKey'

blueprint = make_google_blueprint(
	client_id="######.apps.googleusercontent.com",
    client_secret="####",
	offline=True,
	scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/welcome')
def welcome():
	# RETURN INTERNAL SERVER ERROR IF NOT LOGGED IN !!
	resp = google.get('/oauth2/v2/userinfo')
	assert resp.ok, resp.text
	email = resp.json()['email']

	return render_template('welcome.html', email=email)


@app.route('/login/google')
def login():
	if not google.authorized:
		return render_template(url_for('google.login'))

	resp = google.get('/oauth2/v2/userinfo')
	assert resp.ok, resp.text
	email = resp.json()['email']

	return render_template('welcome.html', email=email)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()