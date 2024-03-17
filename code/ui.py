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

# definition of automaton transitions    
TRANSITIONS = {
    Automaton.IDLE: {"add": Automaton.ADD, "delete": Automaton.DEL, "options": Automaton.OPTIONS, "out":Automaton.OUT},
    Automaton.ADD: {"done": Automaton.IDLE},
    Automaton.DEL: {"done": Automaton.IDLE},
    Automaton.OPTIONS: {"ok" : Automaton.OK,
                        "title": Automaton.TITLE, #to add to automton graph 
                        "author": Automaton.AUTHOR, 
                        "date": Automaton.DATE,
                        "addex": Automaton.ADDEX,
                        "delete": Automaton.DELEX,
                        "quit": Automaton.QUIT,
                        },
    Automaton.OK: {"done":Automaton.IDLE},
    Automaton.TITLE: {"done": Automaton.OPTIONS},
    Automaton.AUTHOR: {"done": Automaton.OPTIONS},
    Automaton.DATE: {"done": Automaton.OPTIONS},
    Automaton.DELEX: {"done": Automaton.OPTIONS},
    Automaton.QUIT:{"done":Automaton.IDLE},
    Automaton.OUT:{}
}

#retrieves valid events for a given state of the automaton.:
#state is a parameter which corresponds to a state of the automaton 
def valid_events(state):
    return list(TRANSITIONS.get(state, {}).keys())

# The transition(state, event) function takes two arguments: 
# - the current state of the automaton (state) 
# - the event (event) triggered by the user. 
# It uses this information to determine the next state of the controller.  
def transition(state, event):
    state_possible = TRANSITIONS.get(state, {})
    next_state = state_possible.get(event)
    if next_state is None:
        valid = valid_events(state)
        print("\033[91mError: Invalid event.\033[0m Please enter one of the following events:")
        for option in valid:
            print(f"- \033[92m{option}\033[0m")
        return state
    return next_state



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

def main():
    automaton_state = Automaton.IDLE
    while automaton_state != Automaton.OUT:
        valid=valid_events(automaton_state)
        colored_events = [f"\033[92m{event}\033[0m" for event in valid]
        print(f"events possible: {', '.join(colored_events)}")
        action = input("Enter an action: ").strip().lower()
        automaton_state = transition(automaton_state, action)
        print("Current state:", automaton_state)

