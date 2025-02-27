<span style="color:#7B7D7D;">[ FRENCH VERSION BELOW ]

## INTERACTIVE MODE DOCUMENTATION

> <span style="color:#5D6D7E;"> Please make sure to only write the name of the exercise file (such as exo1.typ) instead of the whole path.

**Launching the creation software**

```bash
> python3 code/main.py
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
$ -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE> : create a new file named OUTPUT_FILE with EX1, EX2 until EXN

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
> -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE>
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

## DOCUMENTATION DU MODE INTERACTIF

> <span style="color:#5D6D7E;"> Veuillez vous assurer d'écrire uniquement le nom du fichier d'exercice (tel que exo1.typ) au lieu du chemin complet.


**Lancement du logiciel de création**

```bash
> python3 code/main.py
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
$ -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE> : create a new file named OUTPUT_FILE with EX1, EX2 until EXN

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
> -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE>
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
