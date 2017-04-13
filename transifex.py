import json
import requests as r

projects = [
    ["nguillaumin", "osmtracker-android"],
    ["overpass-turbo", "overpass-turbo"],
    ["ideditor", "id-editor"],
    ["openstreetmap", "presets"],
    ["openstreetmap", "historic-objects-preset"],
    ["openstreetmap", "vespucci"],
    ["yohanboniface", "umap"],
    ["openstreetmap-france", "osmose"],
    ["osm-catala", "osmbot"],
    ["fieldpapers", "fieldpapers"]
            ]
url = "https://www.transifex.com/_/userspace/ajax/widgets/languages/{}/{}/?all=1"
result = []
for project in projects:
    request = r.get(url.format(project[0], project[1]))
    data = json.loads(request.text, encoding="utf-8")
    polish = [l for l in data["languages"] if l["language_code"] == "pl"][0]
    entry = [project[1], polish["translated_perc"]]
    result.append(entry)

print(result)