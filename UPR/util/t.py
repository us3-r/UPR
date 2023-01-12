import tkinter as tk
from tkinter import filedialog
import json


files = []
global root
root = tk.Tk()

def open_file_input():
    filetypes = (("excel files", "*.xlsx"), ("all files", "*.*"))
    filename = tk.filedialog.askopenfile(title="Select a File", initialdir="/", filetypes=filetypes)
    path = filename.name
    files.append(path)
def open_file_out():
    filetypes = (("textfile files", "*.txt"), ("all files", "*.*"))
    filename = tk.filedialog.askopenfile(title="Select a File", initialdir="/", filetypes=filetypes)
    path = filename.name
    files.append(path)
row_var=tk.IntVar()
def sub():
    row=row_var.get()
    files.append(row)
    close_window()

def close_window():
    if len(files) == 3:
        if files[2] == 0:
            raise ValueError("Rows cannot be 0")
            files.remove(files[2])
        else:root.destroy()

def select_file():
    root.title("UPR")
    root.geometry("1098x720")

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen
    x = (ws/2) - (250/2)
    y = (hs/2) - (50/2) - 100
    root.geometry('%dx%d+%d+%d' % (450 , 250, x, y))

    button_input = tk.Button(root, text="Select input file", command=open_file_input)
    button_input.place(relx=0.5, rely=0.15, anchor="center")
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
    select_file()
    print(files)
    dic = {
        "input_file": files[0],
        "output_file": files[1] if files[1] != "" else "default_output.txt",
        "rows": files[2]
    }
    js_obj = json.dumps(dic, indent=4)
    with open("config.json", "w") as f:
        f.write(js_obj)

if __name__ == "__main__":
    ui_main()