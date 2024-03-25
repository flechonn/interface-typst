from unittest.mock import patch
import pytest

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
    feuille: Sheet = createExerciseSheet("Ma Feuille d'exercices", author="Moi-même", output="ma_feuille.typ")
    feuille.displayExercisesNames()
    
    assert not feuille.ex
    
    feuille.add("BD/TYPST/exo1.typ")
    feuille.displayExercisesNames() 
    
    exo:Exercise=loadExerciseTypst("BD/TYPST/exo1.typ")
    exo_addex:Exercise=feuille.ex[0]
    
    #loading exerciceworking
    assert(exo.metadata == exo_addex.metadata)
    assert (exo.content == exo_addex.content)
    assert (exo.solution == exo_addex.solution)
    assert (exo.visible == exo_addex.visible)   

    with patch('builtins.open', side_effect=FileNotFoundError):
        # Appel de la fonction avec un chemin de fichier qui n'existe pas
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            feuille.add("BD/TYPST/exo1.typ")
            
    exo.printExercise()
    
        
    feuille.add("BD/TYPST/exo1.txt")  # extension incorrecte
    
    # Tentative d'ajout d'un exercice avec des attributs manquants
    feuille.add("BD/TYPST/exo2_missing_attributes.typ")  # attributs manquants
    
    # Tentative d'ajout d'un exercice avec un contenu invalide
    feuille.add("BD/TYPST/exo3_invalid_content.typ")  # contenu invalide
    
    feuille.add("BD/TYPST/exo1.typ") #pas censé fonctionné
    feuille.displayExercisesNames()    
    
    


def testAddExercices():
    aut = Automaton()
    try:
        test_addex()
        print(colorama.Fore.GREEN + "AddingExercises passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "AddingExercises did not pass")
        
testAddExercices()