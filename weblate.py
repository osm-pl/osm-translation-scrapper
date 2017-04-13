from bs4 import BeautifulSoup
import requests as r

projects = ["osmand/main", "osmand/phrases"]
base_url = "https://hosted.weblate.org/projects/{0}/pl/#overview"
results = []

for project in projects:
    url = base_url.format(project)
    html_doc = r.get(url).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    value = soup.find(attrs={'class': "percent"}).get_text().replace(",", ".").replace("%", "")
    result = [project, float(value)]
    results.append(result)

print(results)
