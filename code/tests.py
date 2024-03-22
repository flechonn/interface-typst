import exercise as e
import colorama
import testaddex

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
    assert(exo1.metadata["figures"] == "")
    assert(exo1.metadata["points"] == "5")
    assert(exo1.metadata["bonus"] == "0")
    assert(exo1.metadata["author"] == "Moi")
    assert(exo1.metadata["references"] == "")
    assert(exo1.metadata["language"] == "français")
    assert(exo1.metadata["material"] == "")


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
    
    testaddex.testAddExercices()

if __name__ == "__main__":
    tests()