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
        self.list.append(path)

    # Deleting an exercise existing in the actual exercise sheet
    def delete(self, path):
        self.list.append(path)

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
    # TODO
    # Creation of all exercise objects 
    return

# using typst tools for the file 
def setFormat():
    # TODO
    return
