from flask import Flask, jsonify
from flask_cors import CORS
import json
import requests

app = Flask(__name__)
CORS(app)

@app.get("/taxa/<int:id>")
def get_taxon(id):
    iNaturalist_request = requests.get(f"https://api.inaturalist.org/v2/taxa/{id}?fields=name")
    iNaturalist_data = iNaturalist_request.json()

    if "results" in iNaturalist_data and len(iNaturalist_data["results"]) > 0:
        # # Debugging: directly print iNaturalist response
        # return json.dumps(results)

        taxon = iNaturalist_data["results"][0]
        dnr_matches = filter_by_scientific_name(taxon)

        response = dict(
            taxonId=taxon["id"],
            total_results=len(dnr_matches),
            results=dnr_matches
        )

        return jsonify(response)

    else:
        return f"Error 404: taxon {id} not found", 404


def names_match(a, b):
    return a in b or b in a

def is_name_of(name):
    return lambda dnr_species: (
        sum(1 for dnr_name in dnr_species["scientificNames"]
            if names_match(name, dnr_name))
        > 0
    )

def filter_by_scientific_name(taxon):
    if "id" not in taxon or "name" not in taxon:
        return []

    with open("dnr_regulated_species.json") as dnr_file:
        dnr_data = json.load(dnr_file)
        return list(filter(is_name_of(taxon["name"]), dnr_data))
