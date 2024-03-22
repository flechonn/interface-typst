from unittest.mock import patch

import colorama
from ui import *

def addex_input(prompt):
    if prompt == "try with ../BD/TYPST/exo1.typ :":
        return "BD/TYPST/exo1.typ"
    

def create_input(prompt):
    if prompt == "Title of the new sheet : ":
        return "titre de feuille"


def testaddex(automaton: Automaton):

    # Test creating a new sheet
    automaton.currentState = automaton.transition("create")
    with patch('builtins.input', side_effect=create_input):
        automaton.call_function()  # This should prompt for the sheet file name 

    # Test adding an exercise
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it
    
    exo:Exercise=loadExerciseTypst("BD/TYPST/exo1.typ")
    exo_addex:Exercise=automaton.currentSheet.ex[0]
    
    assert(automaton.currentState ==State.OPTIONS) 
    assert(exo.metadata == exo_addex.metadata)
    assert (exo.content == exo_addex.content)
    assert (exo.solution == exo_addex.solution)
    assert (exo.visible == exo_addex.visible)

def testAddExercices():
    aut = Automaton()
    try:
        testaddex(aut)
        print(colorama.Fore.GREEN + "AddingExercises passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "AddingExercises did not pass")
