from ui import *

def test_game(automaton: Automaton):
    # Affichage de l'état initial
    print("Current state:", automaton.currentState)

    # Test creating a new sheet
    automaton.currentState = automaton.transition("create")
    automaton.call_function()  # This should prompt for a title and create a new sheet
    print("Current state:", automaton.currentState)

    # Test adding an exercise
    automaton.currentState = automaton.transition("addex")
    automaton.call_function()  # This should prompt for the exercise file name and add it
    print("Current state:", automaton.currentState)

    # Test quitting the current sheet
    automaton.currentState = automaton.transition("quit")
    automaton.call_function()  # This should quit the current sheet
    print("Current state:", automaton.currentState)

    # Test going out of the program
    automaton.currentState = automaton.transition("out")
    automaton.call_function()  # This should end the program
    print("Current state:", automaton.currentState)

if __name__ == "__main__":
    aut = Automaton()
    print("Initial state:", aut.currentState)  # Affichage de l'état initial de l'automate
    test_game(aut)
