# iNaturalist_Invasives

## Project setup
In the `iNaturalist_Invasives` folder:
```
python3 -m venv .venv
. .venv/bin/activate
pip install flask
pip install requests
flask run
```

## Routes
### `GET /taxa/{id}`

1. Queries the iNaturalist API to get the scientific name from the taxon ID
2. Searches the DNR JSON for entries matching that scientific name
3. Prints common names, scientific names, and regulation status of matches

#### Examples:
> http://127.0.0.1:5000/taxa/166636
> ```
> iNaturalist returned 166636 = Phellodendron amurense
>  * Found match in DNR list:
>    * Common names: Amur cork tree
>    * Scientific names: Phellodendron amurense
>    * Status: Prohibited
> ```

> http://127.0.0.1:5000/taxa/47802
> ```
> iNaturalist returned 47802 = Lymantria dispar
>  * Found match in DNR list:
>    * Common names: Spongy moth
>    * Scientific names: Lymantria dispar dispar
>    * Status: Restricted
>  * Found match in DNR list:
>    * Common names: Spongy moth, Spongy moth subspecies with flight-capable females
>    * Scientific names: Lymantria dispar asiatica, Lymantria dispar japonica
>    * Status: Prohibited
> ```

> http://127.0.0.1:5000/taxa/126583
> ```
> iNaturalist returned 126583 = Hemerocallis fulva
>  * Did not find match in DNR list
> ```

