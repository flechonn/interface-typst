<span style="color:#7B7D7D;">[ FRENCH VERSION BELOW ]

## COMMAND LINE DOCUMENTATION

**Launching the creation software**

```bash
> ./Projet_Typst.py
$
$ Welcome to the worksheet creation software!
$ What do you want to do ? (-h for help)
```

**Command to display all possible actions**

```bash
> -h
$
$ -add <EX1> : add the file EX1.typ to the database
$ -del <EX1> : delete the file EX1 from the database
$
$ -create <EX1> <EX2> <EXIT_FILE> : create a new file named EXIT_FILE with EX1 and EX2 

```

**Adding an exercise to the database**

```bash
> -add <EX1> 
```

**Deleting an exercise from the database**

```bash
> -del <EX1>
```

**Creation of a sheet**

```bash
> -create <EX1> <EX2> <FileOutput.typ>
$ Please choose one of the following options :
$ - ok : create the .typ file
$ - title : add a title to the sheet
$ - author : add an author to the sheet
$ - date : add a date to the sheet
$ - modalities : add some modalities in the begining of the sheet
$ - add : add a new exercise from the database to the sheet
$ - delete : delete an exercise from the sheet
$ - quit : cancel the creation of the base
```

<br>
<br>


<span style="color:#7B7D7D;">[ FRENCH VERSION ]

## DOCUMENTATION LIGNES DE COMMANDES

**Lancement du logiciel de création**

```bash
> ./Projet_Typst.py
$
$ Welcome to the worksheet creation software!
$ What do you want to do ? (-h for help)
```

**Commande permettant d'afficher toutes les actions possibles**

```bash
> -h
$
$ -add <EX1> : add the file EX1.typ to the database
$ -del <EX1> : delete the file EX1 from the database
$
$ -create <EX1> <EX2> <EXIT_FILE> : create a new file named EXIT_FILE with EX1 and EX2 

```

**Ajout d'un exercice à la base de données :**

```bash
> -add <EX1> 
```

**Suppression d'un exercice de la base de données :**

```bash
> -del <EX1>
```

**Creation d'une fiche d'exercice :**

```bash
> -create <EX1> <EX2> <FileOutput.typ>
$ Please choose one of the following options :
$ - ok : create the .typ file
$ - title : add a title to the sheet
$ - author : add an author to the sheet
$ - date : add a date to the sheet
$ - modalities : add some modalities in the begining of the sheet
$ - add : add a new exercise from the database to the sheet
$ - delete : delete an exercise from the sheet
$ - quit : cancel the creation of the base
```
