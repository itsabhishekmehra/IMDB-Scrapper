from task_1 import scrape_top_list
from task_4 import scrape_movie_details
import pprint
def get_movie_list_details():
    movies = scrape_top_list()
    movie_list = []
    for movie in movies[:50]:
        var = scrape_movie_details(movie['Link'])
        movie_list.append(var)

    # pprint.pprint(movie_list)
    return movie_list

# get_movie_list_details()