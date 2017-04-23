from bs4 import BeautifulSoup
import requests as r


def run(projects, language):
    base_url = "https://hosted.weblate.org/projects/{0}/{1}/#overview"
    results = []

    for project in projects:
        url = base_url.format(project, language)
        html_doc = r.get(url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        findings = soup.find(attrs={'class': "percent"})
        if findings is not None:
            value = findings.get_text().replace(",", ".").replace("%", "")
            result = [project, float(value)]
        else:
            result = [project, 0.0]
        results.append(result)
    return results
