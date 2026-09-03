from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html.jinja", taxon_to_status="http://127.0.0.1:5000/taxa")
