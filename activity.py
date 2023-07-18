import os
import shutil

source = input("Enter name of folder that has to be sorted")
destination = "destinationFolder"

listoffiles=os.listdir(source)
#print(listoffiles)
for i in listoffiles:
    name, ext = os.path.splitext(i) #tom.png
    if ext == "":
        continue
    if ext in [".png", ".jpg", ".gif", ".jpg", '.jfif']:
        path1 = source+"/"+ i
        path2 = destination+"/"+"image_files"
        path3 = destination+"/"+"image_files"+ "/" + i

        if os.path.exists(path2):
            print("MOVING FILES TO", path3)
            shutil.move(path1, path3)
            print("FILE MOVED SUCCESSFULLY")
        else:
            os.makedirs(path2)
            print("FOLDER CREATED")
            print("MOVING FILES TO", path3)
            shutil.move(path1, path3)
            print("FILE MOVED SUCCESSFULLY")