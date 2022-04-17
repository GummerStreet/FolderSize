import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import io

#create main window
def create_main_window():
        global top
        global root
        img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5gQIBzQ2TSKs+wAAA1FJREFUWMPVl0tvE1cYhp8znhqHCcYmdi52cILjVihAWkIEBTVSlAUXBcGaHXtWSCyR2PQXFKmLLrokYgviIlWVqipCqKFQhYhFwYE4sSF33yY29tiHhR0nE9tNEw8Czm7OzJn3+b7vXN4jpJSST9jU7Q6QRgHiOizGzS88LnBpCNX2EQCkRIZjyIlp5JPIf34qBgKIvi5Ejw+E2PLXYqsSyNfvKN57CrHk9lLlc6KM9CMOtO8QwChQfPg38tFUQzUWp4IoZ49BndLUBJB6hsLoGGJqyZKJJoMt2C79gNCatgZIpVL89cst0hOlyN27NI65u3HY7I1RBFuwXR6uyoQJwDAMbv50g8FhJ44mexkoy583X3DNP9JwJsSpIMr546Y+ZePD0qs3eNrTdAZa8Hj34PHu4UDQi3dorzWleDSFfP2uzjKUsjTbO6oH2u0qd6PPEDsQPd7SQ6vDWXku3nuK7cq5yhKtAMhwDKLxmgAnB78mM5DbtrhhFBi9/5hLb79fh4glkeEYIuTfBDAxXfMn2WweoQh2a7t2lPaTQyH++Xma0x1H2KhlApBGoeYON/54igd3JmBHyS+1fN7AvmBjMjXLd64uhlt7kU8iyAsnEKqtnIG4XjUw/HKOeFzn+o8XURTR8AScfB7lj99ecDTbhduulTQ9zvIq2HywlKMfHDpoiThALl8gkzHQ1HIpy5pKvQG6nsPh+Moa8ZyBnn5Pd9SNXVHr7wNrbXZmmd7DPsvO/GQiS3xZp1fzV72rCTAzvcj+wD7LAFZWdBbnU4ScbXUAPC5T55vwMu0+l2UAiUSG+XCCzqZ9ZgNTAXBplf50MotQJOo2nU29trqaQ0+/51BqU0nLmgqAUG2IgQAAz8YjhL5psy76+CrLSzqH93aaXVM5wMocEH1dALydSdIdbLVuAiazRCNLhJrXg1rTMgP0+MDvomO/E4+32RLxYlGysrIKsZKvWLNqosdX4zQUAmWkn6PNv1sWfTqdJZnI0JdfX37KSL/JrJp2hd3+Nhbm0iwupCwBePnvHJNjEa56z1QMyWaTWmXJotFZxn+9jXg13zBAs+rgW3egtPf/H0u20ZQWR8fAUlM6iNAcX4gt/zwuJp/L1exjX07Fp76efwCi6XAcvCTwRQAAAABJRU5ErkJggg=='
        root= tk.Tk()
        top= root
        top.geometry("600x450+468+138")
        top.title("Folder Size")
        favicon=tk.PhotoImage(data=img) 
        root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.878, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)

#menu
def create_menu():
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left",label="Copy", command=copy_code)
    sub_menu.add_command(compound="left",label="Save", command=Save_to_file)
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp)

#Quit
def QuitApp():
    top.destroy()

#Copy Code
def copy_code():
    textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Copy>>"))

#CopyContextMenu
def create_context_menu():
        global menu
        menu = Menu(root, tearoff = 0)
        menu.add_command(label="Copy", command=copy_text)
        root.bind("<Button-3>", context_menu)

def context_menu(event): 
    try: 
        menu.tk_popup(event.x_root, event.y_root)
    finally: 
        menu.grab_release()
        
def copy_text():
        textbox.event_generate(("<<Copy>>"))

#Save to file
def Save_to_file():
        data=[('Text','*.txt')]
        reportfile=asksaveasfilename(filetypes=data, defaultextension=data)
        folderlist=textbox.get(1.0,END)
        folderlistascii=str(folderlist.encode("utf8"))
        if str(reportfile)!='':
              reportfilesave=open(reportfile,'w')
              reportfilesave.write(folderlistascii)
              reportfilesave.close()


#List folders
def dir_size(path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for i in filenames:

            f = os.path.join(dirpath, i)
            
            total_size += os.path.getsize(f)
    return total_size

def list_folder_size():
        global base_dir
        base_dir=str(sys.argv[1])
        dirtext=(dir_size(base_dir))
        formatteddirsize=str(format(dirtext,","))
        files = os.listdir(base_dir)
        foldername=""
        exitcycle=0
        for n in range (1, len(base_dir), 1) :
                if base_dir[-n]!="\\" and exitcycle==0:
                        foldername=base_dir[-n]+foldername
                else:
                        exitcycle=1
        textbox.insert(INSERT,"folder name: "+foldername+"\n")       
        textbox.insert(INSERT,"folder path: "+base_dir+"\n")
        textbox.insert(INSERT, formatteddirsize+"\n")

        folders = []
        level=1
        indentspaces=""
        for e in files:
            filepath = os.path.join(base_dir, e)
            if os.path.isdir(filepath):
                folders.append({"name":e, "path":filepath, "size":dir_size(filepath)})
                subfiles = os.listdir(filepath)
                for x in subfiles:
                        subfilepath = os.path.join(filepath,x)
                        if os.path.isdir(subfilepath):
                                folders.append({"name":x, "path":subfilepath, "size":dir_size(subfilepath)})
                                sub2files = os.listdir(subfilepath)
                                for y in sub2files:
                                        sub2filepath = os.path.join(subfilepath,y)
                                        if os.path.isdir(sub2filepath):
                                                folders.append({"name":y, "path":sub2filepath, "size":dir_size(sub2filepath)})
                                                sub3files = os.listdir(sub2filepath)
                                                for z in sub3files:
                                                        sub3filepath = os.path.join(sub2filepath,z)
                                                        if os.path.isdir(sub3filepath):
                                                                folders.append({"name":z, "path":sub3filepath, "size":dir_size(sub2filepath)})
        

        folders.sort(key=lambda filename: filename['size'], reverse=True)
        for f in folders:
            textbox.insert(INSERT, ("#"*50)+"\n")
            textbox.insert(INSERT, ("folder name: " + f['name'])+"\n")
            textbox.insert(INSERT, ("folder path: " + f['path'])+"\n")
            foldersize=f['size']
            formattedsize=format(foldersize,",")
            textbox.insert(INSERT, (indentspaces+"folder size: " + formattedsize)+"\n")
        textbox.configure(state=DISABLED)


def main():
        create_main_window()
        create_textbox()
        create_menu()
        create_context_menu()
        list_folder_size()
        
main()
root.mainloop()
