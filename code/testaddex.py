import unittest
from unittest.mock import patch

from sheet import *

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

def test_addex():
    feuille: Sheet = Sheet("Ma Feuille d'exercices", author="Moi-même", output="ma_feuille.typ")
    assert (feuille.ex == [])
    
    feuille.add("BD/TYPST/exo1.typ") 
    
    exo:Exercise=loadExerciseTypst("BD/TYPST/exo1.typ")
    exo_addex:Exercise=feuille.ex[0]
    
    #loading exerciceworking
    assert(exo.metadata == exo_addex.metadata)
    assert (exo.content == exo_addex.content)
    assert (exo.solution == exo_addex.solution)
    assert (exo.visible == exo_addex.visible)
    
    with unittest.TestCase.assertRaises(unittest.TestCase(), FileNotFoundError) as context:
        feuille.add("BD/TYPST/hagrid.typ")  
    assert str(context.exception) == "The file could not be found."

    with unittest.TestCase.assertRaises(unittest.TestCase(), ValueError) as context:
        feuille.add("BD/TYPST/exo1.txt")  # incorrect extension
    assert str(context.exception) == "format not supported try with .typ or .tex"

    with unittest.TestCase.assertRaises(unittest.TestCase(), ValueError) as context:
        feuille.add("BD/TYPST/exo2_missing_attributes.typ")
    assert str(context.exception) == "The file does not contain the '= Exercise' tag."
    
    with unittest.TestCase.assertRaises(unittest.TestCase(), ValueError) as context:
        feuille.add("BD/TYPST/exo2_missing_name.typ")
    assert str(context.exception) == "The file does not contain the a 'name' tag."
    
    with unittest.TestCase.assertRaises(unittest.TestCase(), ValueError) as context:
        feuille.add("BD/TYPST/exo1.typ") #cannot have 2 exo with the same name
    assert str(context.exception) == "Exercise already in the sheet"
    
    feuille.add("BD/TYPST/exo2.typ")
    feuille.add("BD/TYPST/exo3.typ")
    assert len(feuille.ex) == 3
    
    


def testAddExercices():
    aut = Automaton()
    try:
        test_addex()
        print(colorama.Fore.GREEN + "AddingExercises passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "AddingExercises did not pass")
        
testAddExercices()