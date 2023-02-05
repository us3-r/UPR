# i love classes :)
class Prefix:
    p = "$|  "

# unused because the UI was made (can be integrated instead of the UI)
class Prompt:
    File_req:str = f"{Prefix.p}Pleas enter a path to file: "
    Rows:int     = f"{Prefix.p}Enter the number of rows (minus the row with the titles) in your excel file: "
    Output_file:str = f"{Prefix.p}Enter a name/path of/to your output file: "


# meant to be used for making pull requests in UI
class Sec:
    def Pop(cmd):
        # because its meant to be run with UI only this opens and outputs content in "cmd" to cmd
        import subprocess
        import os
        subprocess.call(["cmd.exe", "/c", f"echo {cmd}"])
    def Enc():
        pass
    def Dec():
        pass

class UpdateReq():
    def PrintTree():
        with open(".\\util\\tree.txt","r") as file:
            for line in file:
                Sec.Pop(line)
    def MakePullReq(title,body):
    # creates a pull request to the repo
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