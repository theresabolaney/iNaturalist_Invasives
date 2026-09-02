from flask import Flask
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.get("/taxa/<int:id>")
def get_taxon(id):
    iNaturalist_request = requests.get(f"https://api.inaturalist.org/v2/taxa/{id}?fields=name")
    iNaturalist_data = iNaturalist_request.json()

    if "results" in iNaturalist_data and len(results := iNaturalist_data["results"]) > 0:
        # # Debugging: directly print iNaturalist response
        # return json.dumps(results)

        taxon = results[0]
        dnr_matches = match_scientific_names(taxon)

        responses = []
        responses.append(f"iNaturalist returned {taxon["id"]} = {taxon["name"]}")
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

def equivalent(name, other):
    return name in other or other in name

def match_scientific_names(taxon):
    if "id" not in taxon or "name" not in taxon:
        return []

    with open("dnr_regulated_species.json") as dnr_file:
        dnr_data = json.load(dnr_file)

        return [ species for species in dnr_data
                 if len([ name for name in species["scientificNames"]
                          if equivalent(name, taxon["name"]) ])
                    > 0 ]
