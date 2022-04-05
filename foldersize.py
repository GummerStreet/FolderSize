import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
import io

img=b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5gMcFDI18UpbNgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAGHSURBVDjLnZPLSwJRFMZ/d+6kBmUPqjHsIWGCQg96QJCLaBH9C/0f/U9tolXbSshFywJR0p70spKgGmrUmbktpAnLNPp25557Ps53zneEUkrRAKpcAdOqBR0BhN/X6Bv6j8KLe9x0DrLF+kQihJaMIyJG3bPwOrAdnN1DSBVoiqUYcnkKdFnfwf7eJuK5gN6vMf849jtBKo8DyJWZLwL7skjPyB19syGymWtOtx4a6xWSsL8bPZVHxcKIiFEjcNM5mKspGYsauOsN54ptOxxsn5K8jeGmc8iIga7KFVSuCHNQOL7DsmykFL9LmIQN64C17AKqXEH3VgVUqw4TU8NNZ+i6irNMCZ4A00L7TJQeTQaMLlrBNC0G74NerNERAODqskRff2dLgtcXi4GnoGcwTfh9iLgBgj/h4rxENGBAIoTw+2oSZDJBeKi3ZbFtu7yevBNsa0dLxr98IEdDaNkRTnZumhJYb1UWb6KwGvMs/c3KR5DKt7DyOHJ52rOy+H6N/z+mf57zB3hioi9FsuHVAAAAAElFTkSuQmCC'
root= tk.Tk()
top= root
top.geometry("600x450+468+138")
top.title("Folder Size")
favicon=tk.PhotoImage(data=img) 
root.wm_iconphoto(True, favicon)

#Textbox
textbox = Text(top)
textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)
scroll_1=Scrollbar (top)
scroll_1.pack(side=RIGHT, fill=Y)
textbox.configure(yscrollcommand=scroll_1.set)
scroll_1.configure(command=textbox.yview)

def copy_text():
        textbox.event_generate(("<<Copy>>"))

#CopyContextMenu
menu = Menu(root, tearoff = 0)
menu.add_command(label="Copy", command=copy_text)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()

base_dir=str(sys.argv[1])
def dir_size(path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:

            f = os.path.join(dirpath, i)
            
            total_size += os.path.getsize(f)
    return total_size
dirtext=(dir_size(base_dir))
formatteddirsize=str(format(dirtext,","))
textbox.insert(INSERT, formatteddirsize+"\n")
    
files = os.listdir(base_dir)

folders = []

for e in files:
    filepath = os.path.join(base_dir, e)
    if os.path.isdir(filepath):
        folders.append({"name":e, "path":filepath, "size":dir_size(filepath)})

folders.sort(key=lambda filename: filename['size'], reverse=True)
for f in folders:
    textbox.insert(INSERT, ("#"*50)+"\n")
    textbox.insert(INSERT, ("folder name: " + f['name'])+"\n")
    textbox.insert(INSERT, ("folder path: " + f['path'])+"\n")
    foldersize=f['size']
    formattedsize=format(foldersize,",")
    textbox.insert(INSERT, ("folder size: " + formattedsize)+"\n")
textbox.configure(state=DISABLED)


root.bind("<Button-3>", context_menu)
root.mainloop()
