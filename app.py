from flask import Flask
import requests

# https://learning.postman.com/docs/design-apis/mock-apis/tutorials/mock-with-api
# https://dev.to/terieyenike/creating-apis-with-flask-and-testing-in-postman-2ojn
# https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

# Project setup:
# https://flask.palletsprojects.com/en/stable/installation/
# https://flask.palletsprojects.com/en/stable/quickstart/

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/taxa/<int:id>")
def get_taxon(id):
    r = requests.get(f"https://api.inaturalist.org/v2/taxa/{id}")
    return r.json()
