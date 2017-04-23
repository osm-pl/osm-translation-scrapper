import json
import requests as r


def run(projects, language):
    base_url = "https://www.transifex.com/_/userspace/ajax/widgets/languages/{}/{}/?all=1"
    result = []
    for project in projects:
        url = base_url.format(project[0], project[1])
        request = r.get(url)
        data = json.loads(request.text, encoding="utf-8")
        language_data = [l for l in data["languages"] if l["language_code"] == language]
        if len(language_data) != 0:
            entry = [project[1], language_data[0]["translated_perc"]]
        else:
            entry = [project[1], 0]
        result.append(entry)
    return result
