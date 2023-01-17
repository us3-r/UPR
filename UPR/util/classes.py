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

# this class needs to get encrypted before release
class Sec:
    def Pop(cmd):
        import subprocess
        import os
        subprocess.call(["cmd.exe", "/c", f"echo {cmd}"])

    def MakePullReq(title,body):
        import requests
        # not tested yet
        url = "https://api.github.com/repos/us3-r/UPR/pulls"
        headers = {
            "Authorization": "Token secret",
            "Accept": "application/vnd.github+json"
        }
        data = {
            "title": title,
            "head": "new_feature",
            "base": "main",
            "body": body
        }
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 201:
            print("Pull request created successfully")
        else:
            print("Error creating pull request")
            print(f"[!] STATUS CODE: {response.status_code}\n[!] CONTENT:\n{response.content}")

class UpdateReq():
    def PrintTree():
        with open(".\\util\\tree.txt","r") as file:
            for line in file:
                Sec.Pop(line)
