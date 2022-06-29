from unicodedata import name
import requests
from bs4 import BeautifulSoup
import json
import pprint
import os

def actor_analyse(movielink):
    url = movielink+"fullcredits?ref_=tt_cl_sm"
    filename = "actors/"+movielink.split("/")[-2]+"_cast.json"
    if os.path.exists(filename):
        return json.loads(open(filename).read())
    mainsite = requests.get(url).content
    soup = BeautifulSoup(mainsite, "html.parser")
    actor_list = []
    fullcredits_content = soup.find('table', class_='cast_list').find_all('tr')

    for tr in fullcredits_content:
        actors = tr.find_all("td")
        if len(actors) > 1:
            name = actors[1].text.strip()
            link = actors[1].a.attrs['href'].split("/")[-2]
            actor_list.append({"imdb_id": link,"name": name})
    with open(filename, "w+") as f:
        json.dump(actor_list, f, indent=4)
    return actor_list
# print(actor_analyse("https://www.imdb.com/title/tt15097216/"))
