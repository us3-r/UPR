import pandas as p
import json

import util.classes as c
import util.titles  as t



# ------ code start ------ #

#file_path = input(c.Prompt.File_req) # get path to the file to convert



# append data to their core title
title = []
empty = ";"
obj   = {}
final = []
input__  = "example//test_book.xlsx" #input(f"{c.Prompt.File_req}")
output__ = "output.txt"              #input(f"{c.Prompt.Output_file}")
rows__   = 7                         #input(f"{c.Prompt.Rows}")



data = p.read_excel(input__)

for title_ in data:
    title.append(title_)                                # appends all titles in an excel document to a list
title = t.TitleFormat.missingTitle(title) # gets all titles added to one list


# with open("default.json","r") as file:
#     default_data = json.loads(file.read())
# print(title)

for r in range(int(rows__)):
    d = data.loc[r].values # returns a list of all the values from that row
    print(f"[row{r}] ================================")
    first = True
    json_ =""
    for col in range(len(title)):
        try:
            # print(title[col])
            if first:
                print(f"[...] {title[col]}|{str(d[col])}")
                json_ = t.SelectJson.select(str(d[col]))
                first = False
            else:pass
            with open(f"{json_}","r") as file:
                default_data = json.loads(file.read())
            # print(title[col])
            if title[col] in default_data:
                print(f"[+] {title[col]} | {str(d[col])}")
                if title[col] != "":
                    update_data = {title[col]: str(d[col])}
                    default_data.update(update_data)
                    print("in")
                else:
                    update_data = {title[col]: empty}
                    default_data.update(update_data)
                    print("out")
            else:
                print(f"[!] {title[col]} not in {json_}")

        except IndexError as e:
            if title[col] in default_data:
                if default_data[title[col]] == "":
                    update_data = {title[col]: empty}
                    default_data.update(update_data)
                else: pass
    with open(output__,"a") as out_file:
        out_file.write(str(title))
        out_file.write(f"\n{t.TitleFormat.low_title}")
        data_row = ';'.join([f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
        out_file.write(f"\n{data_row}\n")

            # Write a blank line after the data row
        out_file.write("\n")


# panda_dataframe = p.DataFrame(obj)    # creates a Panda data frame
# panda_dataframe.to_csv(output__)    # writes Pandas data frame as a cvs
# print("Created csv\n", panda_dataframe) # prints created csv

