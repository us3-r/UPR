class Error:
    pass


class Pass:
    pass


class Prompt:
    File_req = f"Pleas enter a path to file: "


class Dict:
    def __init__(self) -> None:
        self = dict()

    def add(self,key,value):
        self[key] = value