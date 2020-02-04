import os
import time
from flask import render_template, request
from arielApps import app

@app.route("/")
def hello():
    return render_template('index.html')