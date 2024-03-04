## BASE D'EXERCICES

### Introduction

Documentation sur le format que nous avons choisi pour les fiches d'exercices données en entrée.

Nous sommes initialement partis de la feuille d'examen suivante : [feuille examen](./exemple/Examen-ALGO6-2023.04.19.tex), que nous avons ensuite découpé en plusieurs exercices, et formaté selon nos besoins.

### Fichier exercice type

#### Métadonnées

Les métadonnées seront données selon le format suivant dans le fichier exercice .Tex :

```tex
\begin{meta}
\meta ID (Obligatoire) : % Identifiant de l'exercice % ;
\meta Titre : % Titre de l'exercice % ;
\meta Auteur : % Auteur de l'exercice % ;
\meta Durée : % Durée de l'exerice % ;
\meta Difficulté : % Difficulté de l'exercice % ;
\meta Solution : % Oui ou non, indique si la solution est affichée après % ;
\meta Figures : % Lien vers les figures de l'exercice, séparés par ";" % ;
\meta Nombre de points : % Notation de l'exercice % ;
\meta Bonus : % Exercice bonus ou non % ;
\meta Langue : % Langue de l'exercice % ;
\end{meta}
```

##### Extensions possibles

Dans le cas d'une utilisation plus générale, les extensions suivantes peuvent être ajoutées :

* Matière

#### Contenu de l'exercice

Le contenu de l'exercice sera donné selon le format suivant dans le fichier exercice .tex :

```tex
\begin{contenu}
% Contenu de l'exercices, avec diverses balises, images... %
\end{contenu}
\begin{solution}
% Si présence d'une solution associée à l'exercice %
\end{solution}
```

### Choix de la base de données

Nous avons choisit de prendre des fichiers d'exercices typ formatés pour constituer notre base de données. Cela nous permettra de retrouver plus facilement les métadonnées et le contenu de l'exercice.
