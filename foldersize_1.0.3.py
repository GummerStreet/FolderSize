"""FolderSize 1.0.3 - Display the size of folders and sort them in
descending order.
Copyright (C) 2022  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import *
from tkinter.filedialog import asksaveasfilename
import io
import webbrowser

try:
    import pyi_splash
    pyi_splash.close()
except:
    True

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

    #About menu
    about=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=about,compound="left", label="?")
    about.add_command(compound="left", label="Help", command=helpbox)
    about.add_command(compound="left", label="About", command=aboutbox)

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
        if str(reportfile)!='':
              reportfilesave=open(reportfile,'w')
              reportfilesave.write(folderlist)
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
                                                                folders.append({"name":z, "path":sub3filepath, "size":dir_size(sub3filepath)})
        

        folders.sort(key=lambda filename: filename['size'], reverse=True)
        for f in folders:
            textbox.insert(INSERT, ("#"*50)+"\n")
            textbox.insert(INSERT, ("folder name: " + f['name'])+"\n")
            textbox.insert(INSERT, ("folder path: " + f['path'])+"\n")
            foldersize=f['size']
            formattedsize=format(foldersize,",")
            textbox.insert(INSERT, (indentspaces+"folder size: " + formattedsize)+"\n")
        textbox.configure(state=DISABLED)

#About
def aboutbox():
    global aboutbox
    #print ('about')
    aboutbox=tk.Toplevel(top)
    aboutbox.geometry("500x240")
    aboutbox.resizable(0,0)
    aboutbox.title("About")
    about_label=Label(aboutbox)
    logo=b'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'
    logoimg=tk.PhotoImage(data=logo)
    about_label.place(x=35,y=40,height=102,width=430)
    about_label.configure(image=logoimg)
    about_label.image=logoimg
    about_label.bind("<Button-1>", lambda e: callback("https://fonazzastent.com/"))

    url_title=Label(aboutbox)
    url_title.place(x=35,y=10,height=40,width=430)
    url_title.configure(text="FolderSize 1.0.3", font=("Arial",15), anchor='center')

    url_label=Label(aboutbox)
    url_label.place(x=35,y=152,height=15,width=430)
    url_label.configure(text="https://fonazzastent.com/", anchor='center')
    url_label.bind("<Button-1>", lambda e: callback("https://fonazzastent.com/"))

    url_label2=Label(aboutbox)
    url_label2.place(x=35,y=172,height=30,width=430)
    url_label2.configure(text="https://fonazzastent.com/foldersize/", anchor='center')
    url_label2.bind("<Button-1>", lambda e: callback("https://fonazzastent.com/foldersize/"))

    close_button=Button(aboutbox)
    close_button.place(x=220,y=200,height=30,width=40)
    close_button.configure(text="Close")
    close_button.bind("<Button-1>", close_aboutbox)
    
def close_aboutbox(event):
    aboutbox.destroy()

def callback(url):
    webbrowser.open_new_tab(url)

def helpbox():
    global helpbox
    helpbox=tk.Toplevel(top)
    helpbox.geometry("440x540")
    helpbox.resizable(0,0)
    helpbox.title("Help")
    
    textbox1 = Text(helpbox)
    textbox1.place(x=20, y=20, height=470, width=400)
    scroll_2=Scrollbar (helpbox)
    scroll_2.place(x=421, y=20, height=470, anchor='n')
    textbox1.configure(yscrollcommand=scroll_2.set, wrap=WORD)
    scroll_2.configure(command=textbox1.yview)
    textbox1.focus_set()
    readme="FolderSize 1.0.3\n\
\n\
The program will list the size of a folder and its subfolders, up to 3 levels.\n\
Unzip the file to a folder, run the AddContextMenu.exe program to add a \
\"FolderSize\" command to the right-click context menu of each folder.\n\
The tool will generate a registry entry and import it into the registry.\n\
If you don't have administrator privileges on the computer, the tool will only \
generate the registry file (AddContextMenu.reg) and you will have to add it \
manually, by opening Regedit with administrator privileges and importing it \
through the Import command of the File menu.\n\
Once you have completed the operation, you can right click on any folder and \
then click on FolderSize. A window will appear listing the folder size, followed \
 by names, path and size of subfolders up to 3 levels. The folders are sorted by \
 size in decreasing order, so you will know which folder is occupying more space \
 on your drive. The info is in text format and can be copied (click on \"Copy\" in \
 the \"Edit\" menu or select text and right click-Copy or CTRL-C) and pasted into \
your text editor. You can also save the list to a text file (Save command on the \
 File menu), useful, for instance, to print out or email a report.\n\
If you don't want to add a registry entry to add a context menu, you can still \
use the program, just drag and drop a folder to the program icon or start the \
program from a Command Prompt window, with the folder path as an argument.\n\
\n\
New in this version:\n\
\n\
- Help and About windows added"
    textbox1.insert(INSERT,readme)
    textbox1.configure(state=DISABLED)
    close_button1=Button(helpbox)
    close_button1.place(x=200,y=500,height=30,width=40)
    close_button1.configure(text="Close")
    close_button1.bind("<Button-1>", close_helpbox)

def close_helpbox(event):
    helpbox.destroy()

def main():
        create_main_window()
        create_textbox()
        create_menu()
        create_context_menu()
        list_folder_size()
        
main()
root.mainloop()
