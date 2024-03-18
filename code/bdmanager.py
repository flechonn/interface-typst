# File managing the database
import exercise as exo
import shutil
import os

# Adding an exercise in typst format to the database
# argument : path to file 
def add(path): 
    name = path.split("/")[-1]

    ext = name.split(".")[-1]

    if(name == "typ"):
        BD_path = "../DB/TYPST"

    else:
        BD_path = "../DB/LATEX"

    shutil.copy(path, BD_path)



# Deleting an existing exercise in the database
# argument : path to file
def delete(path): 
    ext = path.split(".")[-1]

    if(ext == "typ"):
        BD_path = "../DB/TYPST/" + path

    else:
        BD_path = "../DB/LATEX/" + path

    if os.path.exists(BD_path):
        os.remove(BD_path)
        print("The file has been successfully deleted.")
    else:
        print("The file does not exist.")






