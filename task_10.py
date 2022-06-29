from os import DirEntry
from re import L
from task_8_9 import refactor
import pprint

movie__list = refactor()

Director_list = []
Language_list = []

Dir_lang_dict = {}

for movie in movie__list:
    for i in movie["Director"]:
        if i not in Director_list:
            Director_list.append(i)
    for j in movie["Language"]:
        if j not in Language_list:
            Language_list.append(j)

for p in Director_list:
    dl={}
    for r in  Language_list:
        l = 0
        for movie in movie__list:
            if p in movie["Director"]:
                if r in movie["Language"]:
                    l+=1
        if l != 0:
            dl[r]=l
    Dir_lang_dict[p]=dl
                    
# print(Dir_lang_dict)