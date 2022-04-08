import os

regfile=open("AddContextMenu.reg",'w')
regfile.write("Windows Registry Editor Version 5.00"+"\n\n"+"[HKEY_CLASSES_ROOT\Directory\shell\FolderSize]"+"\n")
path= os.getcwd()
pathlength=len(path)
newpath=""
for n in range (0,pathlength):
    newpath=(newpath+path[n])
    if path[n]=="\\":
        newpath=newpath+"\\"
regfile.write('"icon"'+"="+'"'+newpath+'\\'+'\\'+"folder.ico"+'"'+"\n\n")
regfile.write("[HKEY_CLASSES_ROOT\Directory\shell\FolderSize\command]"+"\n")
regfile.write('@="'+ newpath+'\\'+'\\'"foldersize.exe"+" "+'\\'+'"'+"%1"+"\\"+'""')
regfile.close()
os.system("start AddContextMenu.reg")
