import pandas as p
import json


#! import util.classes as c
import titles

import time
# ------ code start ------ #
start = time.time()

# append data to their core title
title = []
empty = ";"
obj   = {}
final = []



input__ = "..\\UPR\\example\\big.xlsx"
output__ = "..\\UPR\\new.csv"



data = p.read_excel(input__)

for title_ in data:
    title.append(title_)                                # appends all titles in an excel document to a list

current_block_type = ""
previous_block_type = ""
same = 0


for test in range(0,5100,100):
    first = True
    with open(output__,"a") as out_file:
        out_file.write(f"{titles.TitleFormat.return_top_seq(output__)}\n\n")
    for r in range(int(test)):

    # makes a list of all the values from that row
        d = data.loc[r].values
        print(f"\n================= [row{r}] ======================")
        json_ ="AI.json"

        with open(f"{json_}","r") as file:
            default_data = json.loads(file.read())
        print(f"[...] USING {json_}\n")
        for col in range(len(title)):

    #? for each column in the row, it checks if the title is in the json file and if it is, it appends the value to the list
            try:
                if title[col] in default_data:
                    print(f"[+] {title[col]} | {str(d[col])}")

    # it checks if the value is empty and if it is, it adds a semicolon if not it updates the value
                    if title[col] != "":
                        update_data = {title[col]: str(d[col])}
                        default_data.update(update_data)
                    else:
                        update_data = {title[col]: empty}
                        default_data.update(update_data)
                else:
                    print(f"|__[!] {title[col]} not in {json_} (skipped)")

    # index error is the only error that should be able to happen
            except IndexError as e:
                if title[col] in default_data:
                    if default_data[title[col]] == "":
                        update_data = {title[col]: empty}
                        default_data.update(update_data)
                    else: pass

    #? checks it the block type is different from the previous one
        if current_block_type != previous_block_type:
            same = 0
            previous_block_type = current_block_type
        else: pass

    # writes data to the output file
        with open(output__,"a") as out_file:
            print(f"\n[?] WRITING UNDER BLOCK TYPE: {current_block_type} ")
            if  previous_block_type == current_block_type and same < 1:
                out_file.write(f"\n\n{str(list(default_data.keys()))}")

    #? checks which block type it is and according to it, it chooses which lower_title to use
                type_ = "AI"
                lower_title = titles.TitleFormat.low_title_AI if type_ == "AI" else t.TitleFormat.low_title_AO if type_ == "AO" else t.TitleFormat.low_title_DI if type_ == "DI" else t.TitleFormat.low_title_DO if type_ == "DO" else None

    #? if its an unsupported type, it writes an error message
                out_file.write(f"\n{lower_title if lower_title != None else '[!] ERROR UNSUPPORTED TYPE'}\n")
                data_row = ';'.join([f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
                out_file.write(f"\n{data_row}")
                same += 1

    #? if its the same block type, it just writes the data in a new row
            elif previous_block_type == current_block_type:
                data_row = ';'.join([f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
                out_file.write(f"\n{data_row}")
                same += 1
            else:
    #? Writes a blank line after the data row
                out_file.write("\n")

        print(f"[?] SUCCESSFULLY WRITTEN ROW {r} TO {output__}")

    #? writes the end block to specify the end of the file
    with open(output__,"a") as out_file:
        out_file.write(f"\n\n{titles.TitleFormat.end_block}")

    print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++ DONE ++++++++++++++++++++++++")



    end = time.time()
    time_ = end-start
    print(f"\n\nTime taken for {test} rows: {time_}sec")
    with open("time.txt",'a') as t:
        t.write(f"rows[{test}] :: {time_}s\n")
