<span style="color:#7B7D7D;">[ FRENCH VERSION BELOW ]

## COMMAND LINE DOCUMENTATION

> <span style="color:#5D6D7E;"> Please make sure to only write the name of the exercise file (such as exo1.typ) instead of the whole path.

**Command to display all possible actions**

```bash
> python3 code/main.py -help
$
$ -add <EX1> : add the file EX1 to the database
$ -del <EX1> : delete the file EX1 from the database
$
$ -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE> : create a new file named OUTPUT_FILE with EX1 and EX2, until EXN

```

**Adding an exercise to the database**

```bash
> python3 code/main.py -add <EX1> 
$ EX1 has been successfully added to the database.
```

**Deleting an exercise from the database**

```bash
> python3 code/main.py -del <EX1>
$ EX1 has been successfully deleted from the database.
```

**Creation of a sheet**

```bash
> python3 code/main.py -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE>
$ The sheet OUTPUT_FILE has been successfully created.
```

<br>
<br>


<span style="color:#7B7D7D;">[ FRENCH VERSION ]

## DOCUMENTATION LIGNES DE COMMANDES

> <span style="color:#5D6D7E;"> Veuillez vous assurer d'écrire uniquement le nom du fichier d'exercice (tel que exo1.typ) au lieu du chemin complet.

**Commande permettant d'afficher toutes les actions possibles**

```bash
> python3 code/main.py -help
$
$ -add <EX1> : add the file EX1 to the database
$ -del <EX1> : delete the file EX1 from the database
$
$ -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE> : create a new file named OUTPUT_FILE with EX1 and EX2, until EXN

```

**Ajout d'un exercice à la base de données :**

```bash
> python3 code/main.py -add <EX1> 
$ EX1 has been successfully added to the database.
```

**Suppression d'un exercice de la base de données :**

```bash
> python3 code/main.py -del <EX1>
$ EX1 has been successfully deleted from the database.
```

**Creation d'une fiche d'exercice :**

```bash
> python3 code/main.py -create <EX1> <EX2> ... <EXN> <OUTPUT_FILE>
$ The sheet OUTPUT_FILE has been successfully created.
```
