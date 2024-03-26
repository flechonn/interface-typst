# This file contains the functions that operate on Exercise objects. 
# It is also responsible for managing the typ output.

from exercise import *

class Sheet:
    def __init__(self, title, author=None, date=None, modality=None, duration=None, ex=[], output=None):
        self.title = title
        self.heading = {"author" : author,
                        "date" : date,
                        "modality" : modality,
                        "duration" : duration
        }
        self.ex: list[Exercise] = ex # List of exercise paths existing in the sheet
        self.output = title+".typ" # Name of the output file
    
    def displayExercises(self):
        print("List of exercises:")
        for i, exercise in enumerate(self.ex, 1):
            print(f"exercise number {i}")
            exercise.printExercise()
    
    def displayExercisesNames(self):
        print("List of exercises:")
        if not self.ex:
            print("No exercises available in :",self.title)
        else :
            for i, exercise in enumerate(self.ex, 1):
                name=exercise.metadata["name"]
                print("exercise name :",colorama.Fore.GREEN+"",name+colorama.Fore.RESET)
            
        
    # Adding an exercise to the actual exercise sheet
    def add(self, path):
        exo=loadExercise(path)
        name=exo.metadata["name"]
        for exercise in self.ex :
            if exercise.metadata["name"]==name:
                print("exercise already in the sheet")
                raise ValueError("exercise already in the sheet")
        if(exo):
            self.ex.append(exo)
            print(exo.metadata["name"],"added to sheet")
        

    # Deleting an exercise existing in the actual exercise sheet
    def delete(self, name):
        if(not self.ex):
            print("there is no file in the sheet")
            raise ValueError("there is no file in the sheet")
        for exo in self.ex:
            if exo.metadata["name"] == name:
                self.ex.remove(exo)
                return
        print("The file name is not in the sheet.")
        raise FileNotFoundError("The file name is not in the sheet.")        
        

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

        f = open(self.output, 'w')

        #heading
        if(not self.heading):
            for head in self.heading:
                f.write(head)

        #sheet content
        for exo in self.ex :
            solution_visible = False
            for ex_header in exo.visible.keys():
                if(exo.visible[ex_header]):
                    f.write(ex_header + " : " + exo.visible[ex_header] + " \ ")
                    if(ex_header == "solution"):
                        solution_visible = True

            f.write(exo.content)
            if(solution_visible):
                f.write(exo.solution)
            f.write(" \ ")

        return

# using typst tools for the file 
def setFormat(self):
    template = "../BD/TYPST/utilities.typ"
    importTemplate = "import " + template + ","

    f = open(self.output)
    f.seek(0)
    f.write(importTemplate + "\n")
    return

def createExerciseSheet(title, author=None, date=None, modality=None, duration=None, ex=[], output=None)-> Sheet:
    # Create a new Sheet object
    new_sheet = Sheet(title, author, date, modality, duration, ex, output)

    # Return the created Sheet object
    return new_sheet

