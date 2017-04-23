from bs4 import BeautifulSoup
import requests as r


def run(projects, language):
    base_url = "https://translatewiki.net/w/i.php?title=Special:MessageGroupStats&language=pl&group={}"
    results = []

    prefix_length = len(language)+1

    for project in projects:
        url = base_url.format(project)
        html_doc = r.get(url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = [a for a in soup.find_all("a") if ":" in a.get_text()]
        lang = [a for a in links if a.get_text()[:prefix_length] == language + ":"][0]
        row = lang.find_parent("tr")
        value = row.find_all("td")[3].get_text().replace("%", "")
        result = [project, int(value)]
        results.append(result)
    return results
