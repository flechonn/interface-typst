# This file contains the functions that operate on Exercise objects. 
# It is also responsible for managing the typ output.

from exercise import *
from colorama import Fore, Style

class Sheet:
    def __init__(self, title, author=None, date=None, modality=None, duration=None, ex=[]):
        self.title = title
        self.heading = {"author" : author,
                        "date" : date,
                        "modality" : modality,
                        "duration" : duration
        }
        self.ex: list[Exercise] = ex # List of exercises existing in the sheet
        self.output = title + ".typ" # Name of the output file
    
    def displayExercisesNames(self):
        print("List of exercises :", end=" ")
        exercise_strings = [f"{Fore.CYAN}{exercise.metadata['name']}" for i, exercise in enumerate(self.ex, 1)]
        print(", ".join(exercise_strings))
        print(Style.RESET_ALL)
        
    # Adding an exercise to the actual exercise sheet
    def add(self, path):
        exo = loadExercise(path)
        name = exo.metadata["name"]
        for exercise in self.ex :
            if exercise.metadata["name"] == name:
                print("Exercise already in the sheet")
                raise ValueError("Exercise already in the sheet")
        if exo:
            self.ex.append(exo)
            print(exo.metadata["name"],"added to sheet")

    # Deleting an exercise existing in the actual exercise sheet
    def delete(self, name):
        for exo in self.ex:
            if exo.metadata["name"] == name:
                self.ex.remove(exo)
                return    
        print("Error : unknown exercise")
        

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

        # Heading
        if not self.heading:
            for head in self.heading:
                f.write(head)

        # Sheet content
        for exo in self.ex :
            solution_visible = False
            
            for ex_header in exo.visible.keys():

                if exo.visible[ex_header]:
                    f.write(ex_header + " : " + exo.visible[ex_header] + " \ ")
                    if ex_header == "solution":
                        solution_visible = True

            f.write(exo.content)

            if solution_visible:
                f.write(exo.solution)
                
            f.write(" \ ")

        return
