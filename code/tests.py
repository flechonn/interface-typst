import unittest
from sheet import *
import exercise as e
import bdmanager as bd
import colorama

def test_delex():
    feuille=None
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
    
      

def testLoadingExercisesLatex():
    path = "BD/LATEX/format.tex"

    exo1 = e.loadExerciseLatex(path)
    assert(exo1.metadata["title"] == "Mon Title")
    assert(exo1.metadata["duration"] == "1h30")
    assert(exo1.metadata["difficulty"] == "easy")
    assert(exo1.metadata["solution"] == "0")
    assert(exo1.metadata["figures"] == None)
    assert(exo1.metadata["points"] == "5")
    assert(exo1.metadata["bonus"] == "0")
    assert(exo1.metadata["author"] == "Moi")
    assert(exo1.metadata["references"] == None)
    assert(exo1.metadata["language"] == "français")
    assert(exo1.metadata["material"] == None)

def testLoadingExercisesTypst():
    path = "BD/TYPST/format.typ"

    exo1 = e.loadExerciseTypst(path)
    # exo1.printExercise()
    assert(exo1.metadata["title"] == "Mon Title")
    assert(exo1.metadata["duration"] == "1h30")
    assert(exo1.metadata["difficulty"] == "easy")
    assert(exo1.metadata["solution"] == "0")
    assert(exo1.metadata["figures"] == None)
    assert(exo1.metadata["points"] == "5")
    assert(exo1.metadata["bonus"] == "0")
    assert(exo1.metadata["author"] == "Moi")
    assert(exo1.metadata["references"] == None)
    assert(exo1.metadata["language"] == "français")
    assert(exo1.metadata["material"] == None)
    
def testAddBDManager():
    exo_latex = "test/test_latex.tex"
    exo_typst = "test/test_typst.typ"
    
    bd.add(exo_latex)
    bd.add(exo_typst)
    
    assert(os.path.exists("BD/LATEX/test_latex.tex"))
    assert(os.path.exists("BD/TYPST/test_typst.typ"))
    
def testDeleteBDManager():
    exo_latex = "test_latex.tex"
    exo_typst = "test_typst.typ"
    
    bd.delete(exo_latex)
    bd.delete(exo_typst)
    
    assert(not os.path.exists(exo_latex))
    assert(not os.path.exists(exo_typst))


def tests():
    try:
        testLoadingExercisesLatex()
        print(colorama.Fore.GREEN + "LoadingExercisesLatex passed : 100%"+colorama.Fore.RESET)
    except AssertionError as e:
        print(colorama.Fore.RED + "LoadingExercisesLatex did not pass"+colorama.Fore.RESET)

    try:
        testLoadingExercisesTypst()
        print(colorama.Fore.GREEN + "LoadingExercisesTypst passed : 100%"+colorama.Fore.RESET)
    except AssertionError as e:
        print(colorama.Fore.RED + "LoadingExercisesTypst did not pass"+colorama.Fore.RESET)
    

    try:
        test_delex()
        print(colorama.Fore.GREEN + "DelingExercises passed : 100%"+colorama.Fore.RESET)
    except AssertionError as e:
        print(colorama.Fore.RED + "DelingExercises did not pass"+colorama.Fore.RESET) 
        
    try:
        test_addex()
        print(colorama.Fore.GREEN + "AddingExercises passed : 100%"+colorama.Fore.RESET)
    except AssertionError as e:
        print(colorama.Fore.RED + "AddingExercises did not pass"+colorama.Fore.RESET)
          
        print(colorama.Fore.RED + "LoadingExercisesTypst did not pass")
        
    try:
        testAddBDManager()
        print(colorama.Fore.GREEN + "AddBDManager passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.GREEN + "AddBDManager did not pass")
        
    try:
        testDeleteBDManager()
        print(colorama.Fore.GREEN + "DeleteBDManager passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.GREEN + "DeleteBDManager did not pass")
    
    

if __name__ == "__main__":
    tests()