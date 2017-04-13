from bs4 import BeautifulSoup
import requests as r


base_url = "https://translatewiki.net/w/i.php?title=Special:MessageGroupStats&language=pl&group={}"
projects = ["osm-potlatch2-main",
            "out-waymarked-trails-0-all",
            "out-osm-potlatch2-help",
            "out-osm-site"]
results = []

for project in projects:
    url = base_url.format(project)
    html_doc = r.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    lang = [a for a in soup.find_all("a") if a.get_text() == "pl: Polish"][0]
    row = lang.find_parent("tr")
    value = row.find_all("td")[3].get_text().replace("%", "")
    result = [project, int(value)]
    results.append(result)

print(results)
