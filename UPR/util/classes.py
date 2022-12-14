class Prefix:
    p = "$|  "
class Error:
    pass
class Pass:
    pass
class Prompt:
    File_req:str = f"{Prefix.p}Pleas enter a path to file: "
    Rows:int     = f"{Prefix.p}Enter the number of rows (minus the row with the titles) in your excel file: "
    Output_file:str = f"{Prefix.p}Enter a name/path of/to your output file: "
class Dict:
    def __init__(self) -> None:
        self = dict()

    def add(self,key,value):
        self[key] = value