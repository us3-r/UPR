import pandas as p
import json

import classes as c
import titles  as t



# ------ code start ------ #

#file_path = input(c.Prompt.File_req) # get path to the file to convert


# append data to their core title
title = []
empty = ";"
obj   = {}

input__  = input(f"{c.Prompt.File_req}")
output__ = input(f"{c.Prompt.Output_file}")
rows__   = input(f"{c.Prompt.Rows}")

data = p.read_excel(input__)

for title_ in data:
    title.append(title_)                                # appends all titles in an excel document to a list
title = t.Title.missingTitle(title, t.Title.all_titles) # gets all titles added to one list
for t in range(len(title)):           # adds all titles as key to a dictionary named "obj"
    obj[title[t]]=[]


for r in range(int(rows__)):
    d = data.loc[r].values            # returns a list of all the values from that row
    for col in range(len(title)):
        try:
            obj[title[col]]+=[str(d[col])] # adds a value to a list in a dictionary at the specific key (title[col])
        except IndexError:
            obj[title[col]]+=[str(empty)]  # if there is more titles then values for every next key(title) the value will be ';'

panda_dataframe = p.DataFrame(obj)    # creates a Panda data frame
panda_dataframe.to_csv(output__)    # writes Pandas data frame as a cvs
print("Created csv\n", panda_dataframe) # prints created csv

