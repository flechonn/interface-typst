<span style="color:#7B7D7D;">[ FRENCH VERSION BELOW ]

## EXERCISE BASE

### Introduction

Documentation on the format we have chosen for the exercise sheets provided as input.

We initially started with the following exam sheet: [exam sheet](./exemple/Examen-ALGO6-2023.04.19.tex), which we then divided into several exercises and formatted according to our needs.

### Standard Exercise File

#### Metadata

##### LaTeX Exercise File

Metadata will be provided in the following format in the .tex exercise file:

```tex
% Command to define metadata
\newcommand{\setMeta}[2]{}

\setMeta{title}{Mon Title}
\setMeta{duration}{1h30}
\setMeta{difficulty}{easy}
\setMeta{solution}{0}
\setMeta{figures}{none}
\setMeta{points}{5pts}
\setMeta{bonus}{0}
\setMeta{author}{Moi}
\setMeta{references}{none}
\setMeta{language}{français}
\setMeta{material}{none}
```

##### Typst Exercise file

```.typ
#show terms: it => {
    let title = label("Mon Title")
    let duration = label("1h30")
    let difficulty = label("easy")
    let solution = label("0")
    let figures = label("none")
    let points = label("5pts")
    let bonus = label("0")
    let author = label("Moi")
    let references = label("none")
    let language = label("français")
    let material = label("none")
}
```

#### Exercise Content

##### Fichier exercice LaTeX

The exercise content will be provided in the following format in the .tex exercise file:

```tex
\begin{document}

\section{Exercice}
% Section dedicated to the exercise

\section{Solution}
% Section dedicated to the solution if it exists

\end{document}
```

##### Typst Exercise File

```typ
TODO
```

### Choice of Database

We chose to use formatted LaTeX and Typst exercise files to build our database. This will allow us to more easily retrieve metadata and exercise content.

<br>
<br>


<span style="color:#7B7D7D;">[ FRENCH VERSION ]

## BASE D'EXERCICES

### Introduction

Documentation sur le format que nous avons choisi pour les fiches d'exercices données en entrée.

Nous sommes initialement partis de la feuille d'examen suivante : [feuille examen](./exemple/Examen-ALGO6-2023.04.19.tex), que nous avons ensuite découpé en plusieurs exercices, et formaté selon nos besoins.

### Fichier exercice type

#### Métadonnées

##### Fichier exercice LaTeX

Les métadonnées seront données selon le format suivant dans le fichier exercice .Tex :

```tex
% Commande pour définir les métadonnées
\newcommand{\setMeta}[2]{}

\setMeta{title}{Mon Title}
\setMeta{duration}{1h30}
\setMeta{difficulty}{easy}
\setMeta{solution}{0}
\setMeta{figures}{none}
\setMeta{points}{5pts}
\setMeta{bonus}{0}
\setMeta{author}{Moi}
\setMeta{references}{none}
\setMeta{language}{français}
\setMeta{material}{none}
```

##### Fichier exercice Typst

```.typ
#show terms: it => {
    let title = label("Mon Title")
    let duration = label("1h30")
    let difficulty = label("easy")
    let solution = label("0")
    let figures = label("none")
    let points = label("5pts")
    let bonus = label("0")
    let author = label("Moi")
    let references = label("none")
    let language = label("français")
    let material = label("none")
}
```

#### Contenu de l'exercice

##### Fichier exercice LaTeX

Le contenu de l'exercice sera donné selon le format suivant dans le fichier exercice .tex :

```tex
\begin{document}

\section{Exercice}
% Partie dédiée à l'exercice

\section{Solution}
% Partie dédiée à la solution si celle-ci existe

\end{document}
```

##### Fichier exercice Typst

```.typ
A faire
```

### Choix de la base de données

Nous avons choisit de prendre des fichiers d'exercices LaTeX et Typst formatés pour constituer notre base de données. Cela nous permettra de retrouver plus facilement les métadonnées et le contenu de l'exercice.
