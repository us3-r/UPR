class Titles:
    all_titles = [
    "BLOCK TYPE",
    "Tag",
    "Next block",
    "Description",
    "Initial scan",
    "Scan time",
    "Smoothing",
    "I/O device",
    "H/W options",
    "I/O address",
    "Signal conditioning",
    "Low EGU limit",
    "High EGU limit",
    "EGU tag",
    "Initial A/M status",
    "Alarm enable",
    "Alarm area(s)",
    "LOLO alarm limit",
    "LO alarm limit",
    "HI alarm limit",
    "HIHI alarm limit",
    "ROC alarm limit",
    "Dead band",
    "Alarm priority",
    "Enable output",
    "Security area 1",
    "Security area 2",
    "Security area 3",
    "Alarm area 1",
    "Alarm area 2",
    "Alarm area 3",
    "Alarm area 4",
    "Alarm area 5",
    "Alarm area 6",
    "Alarm area 7",
    "Alarm area 8",
    "Alarm area 9",
    "Alarm area 10",
    "Alarm area 11",
    "Alarm area 12",
    "Alarm area 13",
    "Alarm area 14",
    "Alarm area 15",
    "User field 1",
    "User field 2",
    "ESIG type",
    "ESIG allow cont use",
    "ESIG xmpt alarm ack",
    "ESIG unsigned writes",
    "ESIG cmnt required",
    "PDR update rate",
    "PDR access time",
    "PDR deadband",
    "PDR latch",
    "PDR disable output",
    "PDR array length",
    "Hist tag description",
    "Hist collect",
    "Hist interval",
    "Hist offset",
    "Hist time resolution",
    "Hist compression",
    "Hist deadband",
    "Hist compress type",
    "Hist compress time",
    "Scale enabled",
    "Scale clamping",
    "Scale use EGU",
    "Scale raw low",
    "Scale raw high",
    "Scale low",
    "Scale high",
    "Shelve enable",
    "Shelve policy",
    ]


class TitleFormat:
    all_titles = Titles.all_titles
    def missingTitle(new_list:list,max_list=all_titles) -> list:
        filled_list=new_list
        for name in max_list:
            if name not in new_list:filled_list.append(name)
            else:pass
        return filled_list

set_values = {}

for item in Titles.all_titles:
    set_values[item]=""

# print(set_values)

import json

with open("default.json", "w") as file:
    json.dump(set_values, file)