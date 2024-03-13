# User Interactions 
# This file listens to user requests and offers three choices: add, delete, and create. It cannot change modes.
from enum import Enum

import bdmanager 

# Definition of the automaton managing the interactions
# TODO : finish it

class Automaton(Enum):
    IDLE = 0
    ADD = 1
    DEL = 2
    OPTIONS = 3
    OK = 4
    TITLE = 5
    AUTHOR = 6
    DATE = 7
    ADDEX = 8
    DELEX = 9
    QUIT = 10
    OUT = 11

    def __init__(self):
        self.state = Automaton.IDLE
    




# Adding a new exercise in the database
def add(ex_file): 
    bdmanager.add(ex_file)

# Deleting an existing exercise in the database
# argument : path to file
def delete(id): 
    bdmanager.delete(id)

# Creating a new exercise sheet from a list of ids given in argument
# argument : exercise ids of the new sheet
def create(ids):
    # TODO
    return
