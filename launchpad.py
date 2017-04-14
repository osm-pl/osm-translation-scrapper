from bs4 import BeautifulSoup
import requests as r

projects = ["josm"]

def run(projects):
    base_url = "https://translations.launchpad.net/{0}"
    results = []

    for project in projects:
        url = base_url.format(project)
        html_doc = r.get(url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        row = soup.find(attrs={'class': "language-pl"})
        value = row.find_all("td")[1].find_all("span")[1].get_text()
        result = [project, 100-float(value)]
        results.append(result)
    return results

print(run(projects))
