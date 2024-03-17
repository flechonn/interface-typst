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





# Converting Sheet object to .typ file
def toTyp(self):
    # TODO
    # Creation of all exercise objects 
    return

# using typst tools for the file 
def setFormat():
    # TODO
    return
