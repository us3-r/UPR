class TitleFormat:
    # lower titles for specific block types
    low_title_AI = "!A_NAME;A_TAG;A_NEXT;A_DESC;A_ISCAN;A_SCANT;A_SMOTH;A_IODV;A_IOHT;A_IOAD;A_IOSC;A_ELO;A_EHI;A_EGUDESC;A_IAM;A_IENAB;A_ADI;A_LOLO;A_LO;A_HI;A_HIHI;A_ROC;A_DBAND;A_PRI;A_EOUT;A_SA1;A_SA2;A_SA3;A_AREA1;A_AREA2;A_AREA3;A_AREA4;A_AREA5;A_AREA6;A_AREA7;A_AREA8;A_AREA9;A_AREA10;A_AREA11;A_AREA12;A_AREA13;A_AREA14;A_AREA15;A_ALMEXT1;A_ALMEXT2;A_ESIGTYPE;A_ESIGCONT;A_ESIGACK;A_ESIGTRAP;A_ESIGREQ_COMMENT;A_PDR_UPDATERATE;A_PDR_ACCESSTIME;A_PDR_DEADBAND;A_PDR_LATCHDATA;A_PDR_DISABLEOUT;A_PDR_ARRAYLENGTH;A_HIST_DESC;A_HIST_COLLECT;A_HIST_INTERVAL;A_HIST_OFFSET;A_HIST_TIMERES;A_HIST_COMPRESS;A_HIST_DEADBAND;A_HIST_COMPTYPE;A_HIST_COMPTIME;A_SCALE_ENABLED;A_SCALE_CLAMP;A_SCALE_USEEGU;A_SCALE_RAWLOW;A_SCALE_RAWHIGH;A_SCALE_LOW;A_SCALE_HIGH;A_IALMSHLVENAB;A_ALMSHELVEPOLICY!"
    low_title_AO = "!A_NAME;A_TAG;A_NEXT;A_DESC;A_IODV;A_IOHT;A_IOAD;A_IOSC;A_ELO;A_EHI;A_EGUDESC;A_COLD;A_EVENT;A_ROUT;A_LOLIM;A_HILIM;A_RATE;A_IENAB;A_ADI;A_SA1;A_SA2;A_SA3;A_AREA1;A_AREA2;A_AREA3;A_AREA4;A_AREA5;A_AREA6;A_AREA7;A_AREA8;A_AREA9;A_AREA10;A_AREA11;A_AREA12;A_AREA13;A_AREA14;A_AREA15;A_ALMEXT1;A_ALMEXT2;A_ESIGTYPE;A_ESIGCONT;A_ESIGACK;A_ESIGTRAP;A_ESIGREQ_COMMENT;A_PDR_UPDATERATE;A_PDR_ACCESSTIME;A_PDR_DEADBAND;A_PDR_LATCHDATA;A_PDR_DISABLEOUT;A_PDR_ARRAYLENGTH;A_HIST_DESC;A_HIST_COLLECT;A_HIST_INTERVAL;A_HIST_OFFSET;A_HIST_TIMERES;A_HIST_COMPRESS;A_HIST_DEADBAND;A_HIST_COMPTYPE;A_HIST_COMPTIME;A_SCALE_ENABLED;A_SCALE_CLAMP;A_SCALE_USEEGU;A_SCALE_RAWLOW;A_SCALE_RAWHIGH;A_SCALE_LOW;A_SCALE_HIGH!"
    low_title_DI = "!A_NAME;A_TAG;A_NEXT;A_DESC;A_IODV;A_IOHT;A_IOAD;A_IAM;A_ISCAN;A_SCANT;A_INV;A_OPENDESC;A_CLOSEDESC;A_IENAB;A_ADI;A_PRI;A_ALMCK;A_EVENT;A_SA1;A_SA2;A_SA3;A_EOUT;A_AREA1;A_AREA2;A_AREA3;A_AREA4;A_AREA5;A_AREA6;A_AREA7;A_AREA8;A_AREA9;A_AREA10;A_AREA11;A_AREA12;A_AREA13;A_AREA14;A_AREA15;A_ALMEXT1;A_ALMEXT2;A_ESIGTYPE;A_ESIGCONT;A_ESIGACK;A_ESIGTRAP;A_ESIGREQ_COMMENT;A_PDR_UPDATERATE;A_PDR_ACCESSTIME;A_PDR_DEADBAND;A_PDR_LATCHDATA;A_PDR_DISABLEOUT;A_PDR_ARRAYLENGTH;A_HIST_DESC;A_HIST_COLLECT;A_HIST_INTERVAL;A_HIST_OFFSET;A_HIST_TIMERES;A_HIST_COMPRESS;A_HIST_DEADBAND;A_HIST_COMPTYPE;A_HIST_COMPTIME;A_IALMSHLVENAB;A_ALMSHELVEPOLICY!"
    low_title_DO = "!A_NAME;A_TAG;A_NEXT;A_DESC;A_IODV;A_IOHT;A_IOAD;A_OPENDESC;A_CLOSEDESC;A_COLD;A_INV;A_EVENT;A_IENAB;A_ADI;A_SA1;A_SA2;A_SA3;A_AREA1;A_AREA2;A_AREA3;A_AREA4;A_AREA5;A_AREA6;A_AREA7;A_AREA8;A_AREA9;A_AREA10;A_AREA11;A_AREA12;A_AREA13;A_AREA14;A_AREA15;A_ALMEXT1;A_ALMEXT2;A_ESIGTYPE;A_ESIGCONT;A_ESIGACK;A_ESIGTRAP;A_ESIGREQ_COMMENT;A_PDR_UPDATERATE;A_PDR_ACCESSTIME;A_PDR_DEADBAND;A_PDR_LATCHDATA;A_PDR_DISABLEOUT;A_PDR_ARRAYLENGTH;A_HIST_DESC;A_HIST_COLLECT;A_HIST_INTERVAL;A_HIST_OFFSET;A_HIST_TIMERES;A_HIST_COMPRESS;A_HIST_DEADBAND;A_HIST_COMPTYPE;A_HIST_COMPTIME;A_WRITEONDIFF!"
    end_block = "[-------------------------------------------------End of Block List-------------------------------------------------]"

    def return_top_seq(file_name)->str:
        # returns the top sequence of info for the iFix file
        import datetime, os
        now_ = datetime.datetime.now()
        path = file_name.replace("/","\\")
        top_seq = f"[NodeName : FIX;Database : DATABASE;File Name : {path};Date : {now_.strftime('%d.%m.%Y')};Time : {now_.strftime('%H:%M:%S')};]"
        return top_seq

# as name suggests, this function is used to select from which .json file to get the titles from
class SelectJson:
    def select(t:str)->str:
        available = ["AI","AO","DI","DO"]
        if t in available:
            return f"json//{t}.json"
    def select_type(t:str)->str:
        available = ["AI","AO","DI","DO"]
        if t in available:
            return t