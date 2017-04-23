from bs4 import BeautifulSoup
import requests as r


def run(projects, language):
    base_url = "https://hosted.weblate.org/projects/{0}/{1}/#overview"
    results = []

    for project in projects:
        url = base_url.format(project, language)
        html_doc = r.get(url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        value = soup.find(attrs={'class': "percent"}).get_text().replace(",", ".").replace("%", "")
        result = [project, float(value)]
        results.append(result)
    return results
