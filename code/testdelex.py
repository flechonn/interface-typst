import unittest
from unittest.mock import patch

import colorama
from ui import *

def addex_input(prompt):
    if prompt == "try with ../BD/TYPST/exo1.typ :":
        return "BD/TYPST/exo1.typ"
    
def addex2_input(prompt):
    if prompt == "try with ../BD/TYPST/exo1.typ :":
        return "BD/TYPST/exo2.typ"
    
def delex_input(prompt):
    if prompt == "try with ../BD/TYPST/exo1.typ :":
        return "exo1"
    

def create_input(prompt):
    if prompt == "Title of the new sheet : ":
        return "titre de feuille"


def test_delex():
    feuille: Sheet = Sheet("Ma Feuille d'exercices", author="Moi-même", output="ma_feuille.typ")
    
    assert feuille.ex == []
    
    with unittest.TestCase.assertRaises(unittest.TestCase(), ValueError) as context:
        feuille.delete("hagrid")  
    assert str(context.exception) == "there is no file in the sheet"

    
    feuille.add("BD/TYPST/exo1.typ")
    feuille.displayExercisesNames() 
    
    with unittest.TestCase.assertRaises(unittest.TestCase(), FileNotFoundError) as context:
        feuille.delete("hagrid")  
    assert str(context.exception) == "The file name is not in the sheet."
    
    feuille.delete("exo1")
    assert (feuille.ex== [])
    
    feuille.add("BD/TYPST/exo1.typ")
    feuille.add("BD/TYPST/exo2.typ")
    feuille.delete("exo1")
    assert len(feuille.ex) == 1
    assert feuille.ex[0].metadata['name']=="exo2"
    exo=loadExercise("BD/TYPST/exo2.typ")
    assert feuille.ex[0].content == exo.content
    assert feuille.ex[0].metadata['name']== exo.metadata['name']
    
    feuille.delete("exo2")
    assert feuille.ex== []

def testdelex(automaton: Automaton):

    # Test creating a new sheet
    automaton.currentState = automaton.transition("create")
    with patch('builtins.input', side_effect=create_input):
        automaton.call_function()  # This should prompt for the sheet file name 

    # Test adding an exercise
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it
    
    automaton.currentSheet.displayExercisesNames()
    
    automaton.currentState = automaton.transition("delex")
    with patch('builtins.input', side_effect=delex_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it
    
    #first test == none 
    assert not automaton.currentSheet.ex
    
    automaton.currentSheet.displayExercisesNames()
        # Test adding an exercise
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it
    automaton.currentState = automaton.transition("addex")
    with patch('builtins.input', side_effect=addex2_input):
        automaton.call_function()  # This should prompt for the exercise file path and load and add it    
    
    automaton.currentState = automaton.transition("delex")
    with patch('builtins.input', side_effect=delex_input):
        automaton.call_function()  
    automaton.currentSheet.displayExercisesNames()
    
    assert "exo2" in [exercise.metadata["name"] for exercise in automaton.currentSheet.ex]    

def testDelExercices():
    try:
        test_delex()
        print(colorama.Fore.GREEN + "delingExercises passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "delingExercises did not pass")

if __name__ == "__main__":
    testDelExercices()