# This file contains the functions that operate on Exercise objects. 
# It is also responsible for managing the typ output.

import exercise as e
import re

class Sheet:
    def __init__(self, title, heading, ids, output):
        self.title = title
        self.heading = heading
        self.ids = ids # List of exercise ids existing in the sheet
        self.output = output # Name of the output file
    
# Adding an exercise to the actual exercise sheet
def add(self, id):
    self.list.append(id)

# Deleting an exercise existing in the actual exercise sheet
def delete(self, id):
    self.list.append(id)

# Edit the heading format
def editHeading(self):
    # TODO
    return 


def idToExercise(path): # review this function, not coherent arguments and name function

    f = open(path, 'r')
    lines = f.readlines()

    exercise = e.Exercise(None)

    # Metadatas do not have a precise order in the formatted LaTeX file
    for line in lines:
        extractedwords = re.search(r'\\newcommand\{([^}]*)\}\{([^}]*)\}', line)
        
        key = extractedwords.group(1).replace("\my", "")
        value = extractedwords.group(2)

        if (value == ""):
            value = None

        exercise.metadata[key] = value
    
    return exercise


# Converting Sheet object to .typ file
def toTyp(self):
    # TODO
    # Creation of all exercise objects 
    return

# using typst tools for the file 
def setFormat():
    # TODO
    return
