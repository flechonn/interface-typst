# Fiche de suivi de projet 
Groupe 5

## Semaine 1 (29/01)

Durant cette séance, nous avons principalement discuté des différentes étapes et nous avons mieux défini le cahier des charges de ce projet.

Nous avons également contacté Jean-Marc Vincent, qui est à l'initiative du sujet, pour obtenir des précisions.

Finalement, nous avons commencé à schématiser l'architecture de notre code.

## Semaine 2 (05/02) : 
Elaboration du QQOQCCP, ainsi que d'une matrice SWOT pour commencer ce projet sur de bonnes bases.

## Semaine 3 (12/02)
Elaboration des différentes à réaliser + priorisation des tâches
(Options : composotion de documents, modification de toute la fiche finale, supprimer/ajouter/modifier des exos de la base de données)

## Semaine 4 (19/02)
Prise en main de Typst et LaTeX (mise à jour de Typst, permettant de traduire un projet .tex et .docx en .typ)

Finalisation du diagramme de Gantt

## Semaine 5 (04/03)

* Définition du formattage des fichiers exercices
* Réflexion sur le squelette du code, en lien avec l'architecture déjà établie
* Mise en place des dépôts git
* Implémentation de la classe Exercise
* Réflexion sur la base de données

## Semaine 6 (11/03)

### Lundi 11/03
* Définition de l'automate gérant les interactions
* Redéfinition de l'architecture, suite à une incompréhension au sein du groupe
* Essai d'intégration de l'API (inutile après discussion)

### Mardi 12/03 
* Début d'implémentation de l'automate
* Ecriture d'un format de base pour les exercices en LaTeX (format.tex)
* Travail sur le powerpoint et la présentation de vendredi (soutenance de mi-projet)

### Vendredi 15/05
* Prise en compte des remarques durant la soutenance de mi-projet (ajouter un mode ligne de commandes et ajout d'un format d'entrée typst dans la base de données)
* Création d'un nouveau format d'entrée typst
* Tests pour la méthode chargeant un exercice de la base de données en un objet exercice

## Semaine 7 (18/03)

### Lundi 18/03

* Elaboration de fichiers exercices Typst et Latex pour la base de données (afin de tester)
* Implémentation de l'automate et de l'ui.py (reste à clean le fichier et tester)
* Implémentation du bdmanager.py
* Traduction du README en anglais
* Ajout du mode en ligne de commandes, en plus du mode interactif

### Mardi 19/03

* Modification de l'automate (ajout d'options)
* Modification de LoadExerciseTypst
* En cours d'implémentation : fonction toTyp

### Vendredi 22/03

* Merge des branches pour obtenir un projet cohérent
* Finalisation de la fonction toTypst
* Test de la transition OK de l'automate
* Finalisation des implémentations de LoadExercise (Typst et Latex)
* Finalisation du fichier bdmanager.py
* Remise en question de l'implémentation de l'automate
  

## Semaine 8 (25/03)

### Lundi 25/03

* Discussion de l'implémentation de l'automate
* Avancement sur la gestion des erreurs de l'automate
* Formattage de la feuille d'exercices
* Tests des fonctions add et delete de BDManager
* Tests des fonctions addex et delex 