import pandas as p
import json


#! import util.classes as c
import util.titles as t
import util.ui as ui


# ------ code start ------ #


# append data to their core title
title = []
empty = ";"
obj = {}
final = []


ui.ui_main()  # opens a ui to select files


with open("config.json", "r") as file:
    data = json.loads(file.read())
input__ = data["input_file"]
output__ = data["output_file"]
rows__ = data["rows"]


data = p.read_excel(input__)

for title_ in data:
    # appends all titles in an excel document to a list
    title.append(title_)

current_block_type = ""
previous_block_type = ""
same = 0

with open(output__, "a") as out_file:
    out_file.write(f"{t.TitleFormat.return_top_seq(output__)}\n\n")

for r in range(int(rows__)):

    # makes a list of all the values from that row
    d = data.loc[r].values
    print(f"\n================= [row{r}] ======================")
    first = True
    json_ = ""
    if first:

        # if block type is different from the previous one, it switches the json file
        print(f"[...] CURRENT  {title[0]} >> {str(d[0])}")
        json_ = t.SelectJson.select(str(d[0]))
        current_block_type = str(d[0])
    else:
        False
    with open(f"{json_}", "r") as file:
        default_data = json.loads(file.read())
    print(f"[...] USING {json_}\n")
    for col in range(len(title)):

        # ? for each column in the row, it checks if the title is in the json file and if it is, it appends the value to the list
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

# index error is the only error that should be able to happen, check the inputted row count
        except IndexError as e:
            if title[col] in default_data:
                if default_data[title[col]] == "":
                    update_data = {title[col]: empty}
                    default_data.update(update_data)
                else:
                    pass

# ? checks it the block type is different from the previous one
    if current_block_type != previous_block_type:
        same = 0
        previous_block_type = current_block_type
    else:
        pass

# writes data to the output file
    with open(output__, "a") as out_file:
        print(f"\n[?] WRITING UNDER BLOCK TYPE: {current_block_type} ")
        if previous_block_type == current_block_type and same < 1:
            out_file.write(f"\n\n{str(list(default_data.keys()))}")

# ? checks which block type it is and according to it, it chooses which lower_title to use
            type_ = t.SelectJson.select_type(str(d[0]))
            lower_title = t.TitleFormat.low_title_AI if type_ == "AI" else t.TitleFormat.low_title_AO if type_ == "AO" else t.TitleFormat.low_title_DI if type_ == "DI" else t.TitleFormat.low_title_DO if type_ == "DO" else None

# ? if its an unsupported type, it writes an error message
            out_file.write(
                f"\n{lower_title if lower_title != None else '[!] ERROR UNSUPPORTED TYPE'}\n")
            data_row = ';'.join(
                [f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
            out_file.write(f"\n{data_row}")
            same += 1

# ? if its the same block type, it just writes the data in a new row
        elif previous_block_type == current_block_type:
            data_row = ';'.join(
                [f'"{str(value)}"' if value != ';' else '""' for value in default_data.values()])
            out_file.write(f"\n{data_row}")
            same += 1
        else:
            # ? Writes a blank line after the data row
            out_file.write("\n")

    print(f"[?] SUCCESSFULLY WRITTEN ROW {r} TO {output__}")

# ? writes the end block to specify the end of the file
with open(output__, "a") as out_file:
    out_file.write(f"\n\n{t.TitleFormat.end_block}")

print(f"\n+++++++++++++++++++++++++++++++++++++++++++++++\n+++++++++++++++++ DONE ++++++++++++++++++++++++")


# reset config.json
dic = {
    "input_file": "",
    "output_file": "",
    "rows": ""
}
js_obj = json.dumps(dic, indent=4)
with open("config.json", "w") as f:
    f.write(js_obj)
