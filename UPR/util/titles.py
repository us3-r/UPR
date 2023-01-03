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
    low_title ="!A_NAME;A_TAG;A_NEXT;A_DESC;A_ISCAN;A_SCANT;A_SMOTH;A_IODV;A_IOHT;A_IOAD;A_IOSC;A_ELO;A_EHI;A_EGUDESC;A_IAM;A_IENAB;A_ADI;A_LOLO;A_LO;A_HI;A_HIHI;A_ROC;A_DBAND;A_PRI;A_EOUT;A_SA1;A_SA2;A_SA3;A_AREA1;A_AREA2;A_AREA3;A_AREA4;A_AREA5;A_AREA6;A_AREA7;A_AREA8;A_AREA9;A_AREA10;A_AREA11;A_AREA12;A_AREA13;A_AREA14;A_AREA15;A_ALMEXT1;A_ALMEXT2;A_ESIGTYPE;A_ESIGCONT;A_ESIGACK;A_ESIGTRAP;A_ESIGREQ_COMMENT;A_PDR_UPDATERATE;A_PDR_ACCESSTIME;A_PDR_DEADBAND;A_PDR_LATCHDATA;A_PDR_DISABLEOUT;A_PDR_ARRAYLENGTH;A_HIST_DESC;A_HIST_COLLECT;A_HIST_INTERVAL;A_HIST_OFFSET;A_HIST_TIMERES;A_HIST_COMPRESS;A_HIST_DEADBAND;A_HIST_COMPTYPE;A_HIST_COMPTIME;A_SCALE_ENABLED;A_SCALE_CLAMP;A_SCALE_USEEGU;A_SCALE_RAWLOW;A_SCALE_RAWHIGH;A_SCALE_LOW;A_SCALE_HIGH;A_IALMSHLVENAB;A_ALMSHELVEPOLICY!"

class SelectJson:
    def select(t:str)->str:
        available = ["AI","AO","DI","DO"]
        if t in available:
            return f"json//{t}.json"