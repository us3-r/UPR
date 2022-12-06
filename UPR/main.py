import os
import sys
import pandas as p

import classes as c
import titles  as t



# ------ code start ------ #

#file_path = input(c.Prompt.File_req) # get path to the file to convert


# append data to their core title
title = []
mainDic = {}
empty = ";"

obj = {}


data = p.read_excel("test_book.xlsx")
# print(data)
for title_ in data:
    title.append(title_)
title = t.Title.missingTitle(title, t.Title.all_titles)
for t in range(len(title)):
    obj[title[t]]=[]

# print(obj)
for r in range(7):
    d = data.loc[r].values # returns a list of all the values from that row
    for col in range(len(title)):
        try:
            obj[title[col]]+=[str(d[col])]
        except IndexError:
            obj[title[col]]+=[str(empty)]

panda_dataframe = p.DataFrame(obj)
panda_dataframe.to_csv("test.csv")
print("dataframe", panda_dataframe)
print(obj)
