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
final = []

input__  = "test_book.xlsx"#input(f"{c.Prompt.File_req}")
output__ = "test.csv"#input(f"{c.Prompt.Output_file}")
rows__   = 7 #input(f"{c.Prompt.Rows}")

data = p.read_excel(input__)

for title_ in data:
    title.append(title_)                                # appends all titles in an excel document to a list
title = t.TitleFormat.missingTitle(title) # gets all titles added to one list


with open("default.json","r") as file:
    default_data = json.loads(file.read())
print(title)

for r in range(int(rows__)):
    d = data.loc[r].values            # returns a list of all the values from that row
    for col in range(len(title)):
        try:
            print(title[col])
            if title[col] in default_data:
                if default_data[title[col]] == "":
                    final.append(str(d[col]))
                    print([str(d[col])])
                else:
                    final.append(default_data[title[col]])

        except IndexError as e:
            if title[col] in default_data:
                if default_data[title[col]] == "":
                    final.append(empty)
                else: final.append(default_data[title[col]])

    with open(output__,"a") as out_file:
        out_file.write(f"\n{str(title)}\n")
        for item in final:
            out_file.write(f"\"{item}\",")
        out_file.write("\n")
    final.clear()

# panda_dataframe = p.DataFrame(obj)    # creates a Panda data frame
# panda_dataframe.to_csv(output__)    # writes Pandas data frame as a cvs
# print("Created csv\n", panda_dataframe) # prints created csv

