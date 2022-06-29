import requests
from bs4 import BeautifulSoup
import json
import pprint, os
def scrape_top_list():
    print("Scrapping.....")
    if os.path.exists("top_movies.json"):
        return json.loads(open("top_movies.json").read())
    page_content = requests.get("https://www.imdb.com/india/top-rated-indian-movies/").text
    soup = BeautifulSoup(page_content, "html.parser")
    # print(soup.title.text)

    main_table = soup.find('div', class_='lister')
    table = main_table.find('tbody', class_='lister-list')
    trs = table.find_all('tr')
    # print(trs)

    Top_250_Movies=[]
    p=0
    for tr in trs:
        # print(tr.text.replace('\n','').get_txt().a)
        title= tr.find('td', class_='titleColumn').a.get_text().strip()
        rating= tr.find('td', class_='ratingColumn').get_text().strip()
        year= tr.find('td', class_='titleColumn').span.get_text().strip()[1:5]
        link= tr.find('td', class_='titleColumn').a.get('href')
        p+=1

        Movie={'Name':title,'Rating':rating,'Year':year,'Link':'https://www.imdb.com'+link,'Position':p}  

        Top_250_Movies.append(Movie)

        with open('top_movies.json', 'w') as f:
            json.dump(Top_250_Movies, f, indent=4)
    
    # pprint.pprint(Top_250_Movies)
    return Top_250_Movies
# scrape_top_list()