import json
import requests as r


def run(projects, language):
    base_url = "https://www.transifex.com/_/userspace/ajax/widgets/languages/{}/{}/?all=1"
    result = []
    for project in projects:
        url = base_url.format( project[0], project[1])
        request = r.get(url)
        data = json.loads(request.text, encoding="utf-8")
        polish = [l for l in data["languages"] if l["language_code"] == language][0]
        entry = [project[1], polish["translated_perc"]]
        result.append(entry)
    return result
