# iNaturalist_Invasives

## Project setup
In the `iNaturalist_Invasives` folder:
```
python3 -m venv .venv
. .venv/bin/activate
pip install flask
pip install requests
```

Run API:
```
flask --app api run
```

Run UI:
```
flask --app ui run --port 5001
```

## Routes
### `GET /taxa/{id}`

1. Queries the iNaturalist API to get the scientific name from the taxon ID
2. Searches the DNR JSON for entries matching that scientific name
3. Prints common names, scientific names, and regulation status of matches

#### Examples:
> http://127.0.0.1:5000/taxa/166636
> ```json
> {
>   "results": [
>     {
>       "category": "Plant",
>       "commonNames": [
>         "Amur cork tree"
>       ],
>       "regulated": "Prohibited",
>       "scientificNames": [
>         "Phellodendron amurense"
>       ],
>       "uri": "https://dnr.wi.gov/topic/Invasives/fact/AmurCorkTree.html"
>     }
>   ],
>   "taxonId": 166636,
>   "total_results": 1
> }
> ```

> http://127.0.0.1:5000/taxa/47802
> ```json
> {
>   "results": [
>     {
>       "category": "Animal",
>       "commonNames": [
>         "Spongy moth"
>       ],
>       "regulated": "Restricted",
>       "scientificNames": [
>         "Lymantria dispar dispar"
>       ],
>       "uri": "https://spongymoth.wi.gov/"
>     },
>     {
>       "category": "Animal",
>       "commonNames": [
>         "Spongy moth",
>         "Spongy moth subspecies with flight-capable females"
>       ],
>       "regulated": "Prohibited",
>       "scientificNames": [
>         "Lymantria dispar asiatica",
>         "Lymantria dispar japonica"
>       ],
>       "uri": "https://spongymoth.wi.gov/"
>     }
>   ],
>   "taxonId": 47802,
>   "total_results": 2
> }
> ```

> http://127.0.0.1:5000/taxa/126583
> ```json
> {
>   "results": [],
>   "taxonId": 126583,
>   "total_results": 0
> }
> ```

## Data
[dnr_regulated_species.json](/dnr_regulated_species.json) is a JSON version of the regulated species table from the [Wisconsin Department of Natural Resources](https://dnr.wisconsin.gov/topic/Invasives/RegulatedSpecies), with these notes:
- It includes the information from the first four columns (Category, Common name(s), Scientific name(s), URL, and NR40 status)
- The common and scientific names have been cleaned up and converted to arrays, for example, `Fiveleaf akebia or Chocolate vine` becomes `["Fiveleaf akebia", "Chocolate vine"]`
- It does not include information that can only be found by following the URL, such as:
  - Additional alternate names
  - Detailed locations for species that are Prohibited in some areas and Restricted in others
