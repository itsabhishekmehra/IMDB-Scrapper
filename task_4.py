import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import pprint

def inmin(time):
    letter1 = []
    number1 = []
    letter2 = []
    number2 = []
    strtime = str(time)
    a = strtime.split(' ')

    if len(time) == 6 or len(time) == 5:
        for k in a[0]:
            if k.isalpha() == True:
                letter1.append(k)
            elif k.isdigit() == True:
                number1.append(k)
        alpha1 = ''.join(letter1)
        num1 = ''.join(number1)

        for i in a[1]:
            if i.isalpha() == True:
                letter2.append(i)
            elif i.isdigit() == True:
                number2.append(i)
        alpha2 = ''.join(letter2)
        num2 = ''.join(number2)
        if len(num1) == 1:
            a = int(num1)*60
        else:
            a = int(num1)
        
        if len(num2) == 2:
            b = int(num2)
        else:
            b = int(num2)
        timeinminutes = a+b
        return timeinminutes
    elif len(time) == 2 or len(time) == 3:
        for k in a[0]:
            if k.isalpha() == True:
                letter1.append(k)
            elif k.isdigit() == True:
                number1.append(k)
        alpha1 = ''.join(letter1)
        num1 = ''.join(number1)
        if alpha1 == "h":
            c = int(num1)*60
            return c
        else:
            return num1


def scrape_movie_details(link):
    link_content = requests.get(link).text
    soup = BeautifulSoup(link_content, "html.parser")
    h1_name = soup.find("div", class_="sc-94726ce4-1 iNShGo")
    name = h1_name.find("h1").text
    director = soup.find("div", class_= "ipc-metadata-list-item__content-container").find_all('li')
    dr=[]
    for i in director:
        dr.append(i.text)
    country_main = soup.find_all("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    if len(country_main) == 2:
        country_name=country_main[0].find_all("li")[3]
    else:
        country_name=country_main[1].find_all("li")[3]
    lan = []
    language = soup.find_all('li')
    for l in language:
        if "data-testid" in l.attrs:
            if l.attrs['data-testid'] == "title-details-languages":
                language = l.find_all("li", class_="ipc-inline-list__item")
                break
    for i in language:
        lan.append(i.text)
    link= soup.find("img", class_="ipc-image").get("src")
    duration = soup.find("ul", class_="ipc-inline-list ipc-inline-list--show-dividers sc-8c396aa2-0 kqWovI baseAlt").find_all("li")[-1].text
    genre = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-all sc-388740f9-1 IjgYL ipc-metadata-list--base").find_all("li")[2].find_all("li", class_="ipc-inline-list__item")
    gr=[]
    for i in genre:
        gr.append(i.text)
    Movie = {"Name":name,"Director":dr,"Country":country_name.text,"Language":lan,"Poster_Image_Url":link, "Runtime in Minutes":inmin(duration), "Genre": gr}  
    return Movie
    
# print(scrape_movie_details(scrape_top_list()[0]['Link']))