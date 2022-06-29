import time
from task_1 import scrape_top_list
from task_4 import scrape_movie_details
import os
import json
import random

movies = scrape_top_list()
def refactor():
    ml=[]
    for movie in movies:
        # r1 = random.randint(0, 5)
        # time.sleep(r1)
        
        filename = "movies/"+movie['Link'].split("/")[-2]+".json"
        if not os.path.exists(filename):
            with open(filename, 'w+') as f:
                cdata = scrape_movie_details(movie['Link'])
                json.dump(cdata, f, indent=4)
                ml.append(cdata)
        else:
            try:
                with open(filename, "r") as f:
                    ml.append(json.loads(f.read()))
            except:
                os.remove(filename)
                print(filename, "is invalid...")
                continue
    return ml
# refactor()