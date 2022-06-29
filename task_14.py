from pprint import pprint
from task_13 import get_all_cast
moves_with_cast = get_all_cast()

actorlist = []
for mv in moves_with_cast:
    for c in mv["Cast"]:
        actorlist.append(c['imdb_id'])
actorlist = list(set(actorlist))
maindict = {}

for i in actorlist:
    for m in moves_with_cast:
        pprint(m)
        for c in m['Cast']:
            if c['imdb_id'] == i:
                maindict[i] = {"name": c['name'],"frequent_co_actors": []}
            else:
                maindict[i] = {"name": c['name'],"frequent_co_actors": [m['Cast']]}

# pprint(maindict)