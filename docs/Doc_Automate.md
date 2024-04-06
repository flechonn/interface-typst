[ ENGLISH VERSION ]

## Explanation of Automaton Implementation

**Functioning :**


- To add a **state** and its **associated transitions**, the programmer needs to add the state and its transitions to the _transitions_ dictionary, create a function with the same name as the state, and add the function to the _functions_ dictionary.
- The function **transition** retrieves an action from a list defined in the _transitions_ dictionary, based on the input given by the user, and returns the next state.
-  The function **call_function** calls the function associated with the state (one state = one function).
- Errors are raised using _raise Exception_, and then they are handled within the functions of the automaton.

**Advantages :**

The code is **more modular** and **more understandable**:

The programmer doesn't have to inspect each function to understand which state the automaton is in, but just needs to follow the transitions entered by the user in a dictionary.

Indeed, by following a more classical approach to implementing the automaton, we would have had to modify the state of the automaton within each function. This would require following the automaton's schema step by step, which can lead to errors on the programmer's part, making it a tedious task.

[ VERSION FRANÇAISE ]
## Explication de notre implémentation de l'automate

**Fonctionnement :**

- Pour ajouter un **état** et les **transitions** qui lui sont liées, il suffit d'ajouter l'état et ses transitions dans le dictionnaire _transitions_ de la classe Automaton, créer la fonction du même nom que l'état, et enfin, ajouter la fonction donc le dictionnaire _fonctions_. 
- la fonction **transition** récupère une action parmi une liste définie dans le dictionnaire *transitions*, en fonction de l'input donné par l'utilisateur, et renvoie le prochain état.
- la fonction **call_fonction** appelle la fonction liée à l'état (un état = une fonction).
- les erreurs sont renvoyées par des *raise Exception*, puis celles-ci sont gérées dans les fonctions de l'automate.

**Avantages :**

Le code est **plus modulable** et **plus compréhensible** :

Le programmeur n'a pas à inspecter chaque fonction pour comprendre dans quel état l'automate se trouve, mais juste à suivre les transitions entrées par l'utilisateur dans un seul dictionnaire.

En effet, en suivant une approche plus classique d'implémentation de l'automate, nous aurions dû modifier l'état de l'automate dans chaque fonction. Il faudrait donc suivre pas à pas le schéma de l'automate, ce qui peut engendrer des erreurs de la part du programmeur, c'est une tâche fastidieuse.


