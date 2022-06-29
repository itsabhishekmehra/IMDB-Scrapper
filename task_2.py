from pprint import pprint
from task_1 import scrape_top_list

def group_by_year(movies):
    groupbyyear = {}
    for obj in movies:
        if obj['Year'] not in groupbyyear:
            groupbyyear[obj['Year']]=[obj]
        else:
            groupbyyear[obj['Year']].append(obj)
    # pprint(groupbyyear)
    return(groupbyyear)

variable = scrape_top_list()
# group_by_year(variable)