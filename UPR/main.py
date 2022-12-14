import pandas as p
import json

import util.classes as c
import util.titles  as t
# from util.color import colors as color
from  colorama import Fore as color

# ------ code start ------ #

#file_path = input(c.Prompt.File_req) # get path to the file to convert

print("Hello world!\nps this program is not very safe for your pcs memory\nGLHF <3\n\n")


# append data to their core title
title = []
empty = ";"
obj   = {}
final = []
input__  = input(f"{c.Prompt.File_req}")
output__ = input(f"{c.Prompt.Output_file}")
rows__   = input(f"{c.Prompt.Rows}")



data = p.read_excel(input__)

for title_ in data:
    title.append(title_)                                # appends all titles in an excel document to a list
title = t.TitleFormat.missingTitle(title) # gets all titles added to one list


# with open("default.json","r") as file:
#     default_data = json.loads(file.read())
# print(title)

current_block_type = ""
previous_block_type = ""
same = 0

for r in range(int(rows__)):
    d = data.loc[r].values # returns a list of all the values from that row
    print(f"\n================= [row{r}] ======================")
    first = True
    json_ =""
    if first:
        print(f"[...] CURRENT  {title[0]} >> {str(d[0])}")
        json_ = t.SelectJson.select(str(d[0]))
        current_block_type = str(d[0])
    else:False
    with open(f"{json_}","r") as file:
        default_data = json.loads(file.read())
    print(f"[...] USING {json_}\n")
    for col in range(len(title)):
        try:
            # print(title[col])
            if title[col] in default_data:
                print(f"[+] {title[col]} | {str(d[col])}")
                if title[col] != "":
                    update_data = {title[col]: str(d[col])}
                    default_data.update(update_data)
                else:
                    update_data = {title[col]: empty}
                    default_data.update(update_data)
            else:
                print(f"|__[!] {title[col]} not in {json_} (skipped)")

        except IndexError as e:
            if title[col] in default_data:
                if default_data[title[col]] == "":
                    update_data = {title[col]: empty}
                    default_data.update(update_data)
                else: pass
    if current_block_type != previous_block_type:
        same = 0
        previous_block_type = current_block_type
    else: pass
    with open(output__,"a") as out_file:
        print(f"\n[?] WRITING UNDER BLOCK TYPE: {current_block_type} ")
        if  previous_block_type == current_block_type and same < 1:
            out_file.write(str(list(default_data.keys())))
            out_file.write(f"\n{t.TitleFormat.low_title}")
            data_row = ';'.join([f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
            out_file.write(f"\n{data_row}\n")
            same += 1
        elif previous_block_type == current_block_type:
            data_row = ';'.join([f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
            out_file.write(f"\n{data_row}\n")
            same += 1
        else:
            # Write a blank line after the data row
            out_file.write("\n")
    print(f"[?] SUCCESSFULLY WRITTEN ROW {r} TO {output__}")
print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++")
print(f"+++++++++++++++++ DONE ++++++++++++++++++++++++")

