import tkinter as tk
from tkinter import filedialog
import json
import os

# https://realpython.com/python-gui-tkinter/

files = []
global root, update
update = False
root = tk.Tk()

def open_file_input():
    # opens a file dialog to select a file for input
    filetypes = (("excel files", "*.xlsx"), ("all files", "*.*"))
    filename = tk.filedialog.askopenfile(title="Select a File", initialdir=os.getcwd(), filetypes=filetypes)
    path = filename.name
    files.append(path)

def open_file_out():
    # opens a file dialog to select a file for output
    filetypes = (("textfile files", "*.csv"), ("all files", "*.*"))
    filename = tk.filedialog.askopenfile(title="Select a File", initialdir=os.getcwd(), filetypes=filetypes)
    path = filename.name
    files.append(path)

row_var=tk.IntVar()
# I am as confused as you are
def sub():
    row=row_var.get()
    files.append(row)
    close_window()

# used as part of the "be able to make pull requests from the ui" update .... it sees if the user wants to update
def SetTrue():
    global update
    update = True
    root.quit()


def close_window():
    if len(files) == 3:
        if files[2] == 0:
            files.remove(files[2])
            raise ValueError("Rows cannot be 0")
        else:root.destroy()

def open_git():
        import webbrowser
        webbrowser.open_new(r"https://github.com/us3-r/UPR")

def select_file():
    root.title("xlsx to csv for iFix")
    root.geometry("1098x720")

    # menu bar
    menubar = tk.Menu(root)
    _menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Options", menu=_menu)
    _menu.add_command(label="Update", command=SetTrue)
    _menu.add_command(label="Exit", command=root.quit)
    root.config(menu=menubar)

    # text
    label = tk.Label(root, text="https://github.com/us3-r/UPR")
    label.config(font=("Courier", 12))
    label.pack()
    label.bind("<Button-1>", lambda e:open())

    # main window

    #? this is used to open the window in the center of users screen
    ws = root.winfo_screenwidth() # width of the users screen
    hs = root.winfo_screenheight() # height of the users screen
    x = (ws/2) - (250/2)
    y = (hs/2) - (50/2) - 100
    root.geometry('%dx%d+%d+%d' % (450 , 250, x, y))

    # buttons and fields
    button_input = tk.Button(root, text="Select input file", command=open_file_input)
    button_input.place(relx=0.5, rely=0.20, anchor="center")
    button_output = tk.Button(root, text="select output file", command=open_file_out)
    button_output.place(relx=0.5, rely=0.40, anchor="center")
    row_labe = tk.Label(root, text="Rows")
    row_entry = tk.Entry(root, textvariable=row_var)
    row_labe.place(relx=0.5, rely=0.65, anchor="center")
    row_entry.place(relx=0.5, rely=0.75, anchor="center")
    button_submit = tk.Button(root, text="Submit", command=sub)
    button_submit.place(relx=0.5, rely=0.85, anchor="center")
    root.mainloop()

def ui_main():
    # opens the ui and adds selected values to config.json
    select_file()
    print(files)
    try:
        dic = {
            "input_file": files[0],
            "output_file": files[1] if files[1] != "" else "default_output.txt",
            "rows": files[2]
        }
        js_obj = json.dumps(dic, indent=4)
        with open("config.json", "w") as f:
            f.write(js_obj)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    ui_main()