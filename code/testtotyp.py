import exercise as e
# import sheet as s
from sheet import *


def createExerciseSheet(title, author=None, date=None, modality=None, duration=None, ex=[], output=None)-> Sheet:
    # Create a new Sheet object
    new_sheet = Sheet(title, author, date, modality, duration, ex, output)

    # Return the created Sheet object
    return new_sheet

def main():
    exo:Exercise=loadExerciseTypst("BD/TYPST/exo1.typ")

    feuille: Sheet = createExerciseSheet("Ma Feuille d'exercices", author="Moi-même", ex=[exo], output="ma_feuille.typ")
    
    # feuille.add("BD/TYPST/exo1.typ")

    # Afficher les exercices de la feuille
    feuille.displayExercisesNames()
    
    feuille.toTyp()

main()
    
