from yaml import scan
from task_1 import scrape_top_list
from task_12 import actor_analyse
import pprint
import os
import json
from task_4 import scrape_movie_details

def get_all_cast():
    allmovie = scrape_top_list()
    if os.path.exists("top_updated_list.json"):
        return json.loads(open("top_updated_list.json").read())
    emplist = []
    for m in allmovie:
        moviedetail = scrape_movie_details(m['Link'])
        casts = actor_analyse(m["Link"])
        # pprint.pprint(casts)
        # pprint.pprint(moviedetail)
        moviedetail['Cast'] = casts
        # print(moviedetail)
        emplist.append(moviedetail)
    with open('top_updated_list.json', 'w') as f:
            json.dump(emplist, f, indent=4)
    return emplist

# get_all_cast()