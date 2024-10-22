import exercise as e
import sheet as s
from sheet import *



def main():
    
    exo1 = e.loadExerciseTypst("BD/TYPST/exo1.typ")
    exo2 = e.loadExerciseTypst("BD/TYPST/exo2.typ")
    
    exo2.addVisible("solution")
    
    logo_path = "BD/LOGO/UFR_IM2AG_2020.jpg"
    modalities = ("Sont interdits : les documents, les ordinateurs, les téléphones (incluant smartphone, tablettes,... tout ce qui contient un dispositif électronique). Seuls les dictionnaires papier pour les personnes de langue étrangère sont autorisés."
                " En cas de doutes sur l’énoncé, préciser les choix que vous faites sur votre copie et continuer."
                " Il sera tenu compte de la qualité de la rédaction et de la clarté de la présentation (2 pts)."
                " Le barème indicatif : Exercice I : 5 points ; Exercice II : 5 points ; Problème III : 8 points"
                " Les exercices et le problème peuvent être traités indépendamment."
                " Les durées sont indicatives, penser à se relire.")

    feuille = s.Sheet("Ma Feuille d'exercices", logo=logo_path, author="Moi-même", date="25 Mars 2024", modality=modalities, duration="3 heures", ex=[exo2, exo1], output="ma_feuille.typ")


    # Dipslay the exercises of the file
    feuille.displayExercisesNames()
    
    # create the file with .typ extension
    feuille.toTyp()

main()
    
