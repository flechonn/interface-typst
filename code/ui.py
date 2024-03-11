# User Interactions 
# This file listens to user requests and offers three choices: add, delete, and create. It cannot change modes.

import bdmanager 

# TODO : Definition of the automaton managing the interactions

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
