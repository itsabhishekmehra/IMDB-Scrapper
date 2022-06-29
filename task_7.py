from task_5 import get_movie_list_details

list_movies = get_movie_list_details()

def analyse_movies_directors(movielist):
    total_Director = {}
    Director_list = []
    for movie in movielist:
        if movie["Director"] not in Director_list:
            Director_list.extend(movie["Director"])
        else:
            continue
        
    for Director in Director_list:
        l = 0
        for movie in movielist:
            if Director in movie["Director"]:
                l = l + 1

        total_Director[Director] = l
    return total_Director
    print(total_Director)        

# analyse_movies_directors(list_movies)