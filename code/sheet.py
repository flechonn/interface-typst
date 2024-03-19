# This file contains the functions that operate on Exercise objects. 
# It is also responsible for managing the typ output.

import exercise as e

class Sheet:
    def __init__(self, title, author=None, date=None, modality=None, duration=None, ex=None, output=None):
        self.title = title
        self.heading = {"author" : author,
                        "date" : date,
                        "modality" : modality,
                        "duration" : duration
        }
        self.ex = ex # List of exercise paths existing in the sheet
        self.output = output # Name of the output file
    
    # Adding an exercise to the actual exercise sheet
    def add(self, path):
        exo=e.loadExercise(path)
        
        self.ex.list.append(exo)

    # Deleting an exercise existing in the actual exercise sheet
    def delete(self, name):
        for exo in self.ex:
            if exo.name == name:
                self.ex.list.remove(exo)
                return    
        print("Error name unknow")
        

    # Functions editing the heading format
    def editTitle(self, title):
        self.title = title
    
    def editAuthor(self, author):
        self.heading["author"] = author
    
    def editDate(self, date):
        self.heading["date"] = date
    
    def editModality(self, modality):
        self.heading["modality"] = modality
    
    def editDuration(self, duration):
        self.heading["duration"] = duration



# Converting Sheet object to .typ file
def toTyp(self):
    
    f = open(self.output)

    #heading
    for head in self.heading:
        f.write(self.head)

    #sheet content
    for exo in self.ex :
        for ex_header in exo.visible.keys():
            f.write(ex_header + " : " + exo.visible[ex_header] + "\n")
            if(ex_header == "solution"):
                solution_visible = True

        f.write(exo.content)
        if(solution_visible):
            f.write(exo.solution)
        f.write("\n")

    return

# using typst tools for the file 
def setFormat(self):
    template = "../BD/TYPST/utilities.typ"
    importTemplate = "import " + template + ","

    f = open(self.output)
    f.seek(0)
    f.write(importTemplate + "\n")



    return
