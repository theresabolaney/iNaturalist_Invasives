from flask import Flask
from flask_cors import CORS
import json
import requests

# https://learning.postman.com/docs/design-apis/mock-apis/tutorials/mock-with-api
# https://dev.to/terieyenike/creating-apis-with-flask-and-testing-in-postman-2ojn
# https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

# Project setup:
# https://flask.palletsprojects.com/en/stable/installation/
# https://flask.palletsprojects.com/en/stable/quickstart/

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/taxa/<int:id>")
def get_taxon(id):
    iNaturalist_request = requests.get(f"https://api.inaturalist.org/v2/taxa/{id}?fields=name")
    iNaturalist_data = iNaturalist_request.json()
    if "results" in iNaturalist_data and len(results := iNaturalist_data["results"]) > 0:
        # # Debugging: directly print iNaturalist response
        # return json.dumps(results)

        responses = []
        with open("dnr_regulated_species.json") as dnr_file:
            dnr_data = json.load(dnr_file)

            for result in results:
                if "id" in result and "name" in result:
                    responses.append(f"iNaturalist returned {result["id"]} = {result["name"]}")
                    # TODO: also get common name from iNaturalist
                    dnr_matches = []
                    for regulated_species in dnr_data:
                        for name in regulated_species["scientificNames"]:
                            if result["name"] in name or name in result["name"]:
                                dnr_matches.append(regulated_species)
                                break

                    if len(dnr_matches) > 0:
                        for dnr_match in dnr_matches:
                            responses.append(
                                             f" * Found match in DNR list:\n"
                                             f"   * Common names: {", ".join(dnr_match["commonNames"])}\n"
                                             f"   * Scientific names: {", ".join(dnr_match["scientificNames"])}\n"
                                             f"   * Status: {dnr_match["regulated"]}"
                                         )
                    else:
                        responses.append(" * Did not find match in DNR list")

        return "<pre>" + "\n".join(responses) + "</pre>"

    else:
        return f"iNaturalist returned no results for {id}"
