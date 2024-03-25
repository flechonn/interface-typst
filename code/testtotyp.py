import exercise as e
# import sheet as s
from sheet import *


def main():
    exo:Exercise=loadExerciseTypst("BD/TYPST/exo1.typ")

    feuille: Sheet = createExerciseSheet("Ma Feuille d'exercices", author="Moi-même", ex=[exo], output="ma_feuille.typ")
    
    # feuille.add("BD/TYPST/exo1.typ")

    # Afficher les exercices de la feuille
    feuille.displayExercisesNames()
    
    feuille.toTyp()

main()
    
