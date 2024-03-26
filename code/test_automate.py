from unittest.mock import patch
from ui import *
from sheet import *


def addex_input(prompt):
    if prompt == "File to add : ":
        return "exo1.typ"
    
def addex2_input(prompt):
    if prompt == "File to add : ":
        return "exo2.typ"
    

def create_input1(prompt):
    if prompt == "Title of the new sheet : ":
        return "hagrid", "hagrid.typ"


def testautomate(automaton: Automaton):
    
    # Test creating a new sheet
    automaton.currentState = automaton.transition("create")
    automaton.call_function()  # This should prompt for the sheet file name 
                
    automaton.currentState = automaton.transition(None)

    # Test adding an exercise
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it
    
    automaton.currentState = automaton.transition(None)
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex2_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it

    automaton.currentState = automaton.transition(None)
    automaton.currentState = automaton.transition("ok")
    automaton.call_function()
        

def test_automate():
    try:
        aut = Automaton()
        testautomate(aut)
        print(colorama.Fore.GREEN + "delingExercises passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "delingExercises did not pass")

test_automate()