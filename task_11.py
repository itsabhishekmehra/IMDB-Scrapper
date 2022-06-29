from task_8_9 import refactor
# from task_5 import get_movie_list_details
from os import DirEntry
import pprint

datafactory = refactor()
def analyse_movies_genre(movielist):
    total_genre = {}
    
    genre_list = []
    for movie in movielist:
        if movie["Genre"] not in genre_list:
            genre_list.extend(movie["Genre"])
        else:
            continue
        
    for genre in genre_list:
        l = 0
        for movie in movielist:
            if genre in movie["Genre"] :
                l = l + 1

        total_genre[genre] = l
    print(total_genre)        
    return total_genre

# analyse_movies_genre(datafactory)