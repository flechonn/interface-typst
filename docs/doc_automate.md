[ FRENCH VERSION BELOW ]

## Explanation of Automaton Implementation

**Operation:**

    - Adding states and transitions is made easier due to the use of a Python dictionary.
    - There's a dictionary defining the automaton and its transitions called _transitions_.
    -  There's a dictionary intended for state functions, with the same name (one state = one function), for example: state: option, then there exists a function option.
- To add a state and its associated transitions, one needs to add the state and its transitions to the transitions dictionary, create a function with the same name as the state, and add the function to the _functions_ dictionary.
- The function transition retrieves an action from a list defined in the transitions dictionary, and sends the next state.
-  The function call_function calls the function associated with the state (one state = one function).
- Errors are raised and managed within the automaton for incorrect user input.

**Advantages:**

The code is **more modular** and **more understandable**:

    The programmer doesn't have to inspect each function to understand which state the automaton is in, but just needs to follow the transitions entered by the user in a single dictionary.

**Error handling is managed by each state** (one state = one function). If there's an error in user usage not foreseen by the automaton, we can more easily choose the state to which it returns.

## Explication implémentation automate

**fonctionnement :**

    - ajout d'état et de transition plus facile dû à l'utilisation de dictionnaire python
    - il y a un dictionnaire définissant l'automate et ses transitions appelé _transitions_ .
    - il y a un dictionnaire destiné aux fonctions des états, du même nom (un état = une fonction), exemple :
    état : option, alors il existe une fonction option

- Pour ajouter un état et les transitions qu'ils lui sont liées, il faut ajouter l'état et ses transitions dans le dictionnaire transitions, créer la fonction du même com que l'état, et ajouter, la fonction donc le dictionnaire _fonctions_  
- la fonction **transition**, récupère une action parmi une liste définie dans le dictionnaire *transitions*, et envoie le prochain état 
- la fonctions **call_fonction** apelle la fonction liée à l'état (un état = une fonction)
- les erreurs sont renvoyées par des *raise* et gérer dans l'automate, pour des mauvaises entré de l'utilisateur. 

**Avantage  :**

le code est **plus modulable** et **plus compréhensible** :

    Le programmeur n'a pas à inspecter chaque fonction pour comprendre dans quel état l'automate se trouve, mais juste à suivre les transitions entrées par l'utilisateur dans un seul dictionnaire.

**la gestion des erreurs est gérée par chaque état** (un état = une fonction) s'il y a une erreur d'utilisation de l'utilisateur pas prévue par l'automate, on peut plus facilement choisir l'état dans lequel celui-ci revient.

