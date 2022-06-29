from task_5 import get_movie_list_details

list_movies = get_movie_list_details()

def analyse_movies_language(parameter):
    total_languages = {}
    lang_list = []
    for movie in parameter:
        if movie["Language"] not in lang_list:
            lang_list.extend(movie["Language"])
        else:
            continue
        
    for lang in lang_list:
        l = 0
        for movie in parameter:
            if lang in movie["Language"] :
                l = l + 1

        total_languages[lang] = l
        
    return total_languages
    print(total_languages) 

# analyse_movies_language(list_movies)



# def analyse_movies_language(movies_list):
#     print
#     Hindi_count = 0
#     English_count = 0
#     Malyalam_count = 0
#     print("crimsi...", Hindi_count)
#     for movie in movies_list:
#         if movie["Language"] == ["Hindi"]:
#             Hindi_count = Hindi_count + 1
#         elif movie["Language"] == ["English"]:
#             English_count = English_count + 1
#         elif movie["Language"] == ["Malyalam"]:
#             Malyalam_count = Malyalam_count + 1
    
#     Movie_by_language = {"Hindi": Hindi_count,"English": English_count,"Malyalam":Malyalam_count}
#     print(Movie_by_language)
# analyse_movies_language(list_movies)