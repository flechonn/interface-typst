import exercise as e
import bdmanager as bd
import colorama
import testaddex
import os

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
        print(colorama.Fore.GREEN + "LoadingExercisesLatex passed : 100%")
    except AssertionError as e:
        print(colorama.Fore.RED + "LoadingExercisesLatex did not pass")

    try:
        testLoadingExercisesTypst()
        print(colorama.Fore.GREEN + "LoadingExercisesTypst passed : 100%")
    except AssertionError as e:
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
    
    
    testaddex.testAddExercices()

if __name__ == "__main__":
    tests()