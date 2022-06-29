from pprint import pprint
from task_2 import group_by_year
from task_1 import scrape_top_list
def group_by_decade(movies):
    # pprint(movies)
    listyear = []
    for obj in movies:
        listyear.append(int(obj))    
    a = min(listyear)
    b = max(listyear)
    a =a-int(str(a)[-1])
    b = b-int(str(b)[-1])
    y_list = range(a,b+10,10)
    dict1={}

    for i in y_list:
        for key in movies:
            if int(key)>i and int(key)<i+10:
                if i in dict1:
                    dict1[i].extend(movies[key])
                else:
                    dict1[i] = movies[key]
    pprint(dict1)
    return dict1
# group_by_decade(group_by_year(scrape_top_list()))