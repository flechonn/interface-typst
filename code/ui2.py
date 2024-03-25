# User Interactions 
# This file listens to user requests and offers three choices: add, delete, and create. It cannot change modes.
from enum import Enum

from sheet import *
import bdmanager
from exercise import *

# Definition of the automaton managing the interactions

class State(Enum):
    IDLE = 0
    ADD = 1
    DEL = 2
    CREATE = 3

    OPTIONS = 4
    OK = 5
    TITLE = 6
    AUTHOR = 7
    DATE = 8
    ADDEX = 9
    DELEX = 10
    QUIT = 11
    
    EDITEX=12
    ADDVISIBLEEX=13
    DELVISIBLEEX=14

    OUT = 15

class Automaton:

    def __init__(self):
        self.currentState = State.IDLE
        self.currentExo : Exercise = None
        self.currentSheet : Sheet = None

        self.error = False # This flag allows the automata to manage errors


    #call the fonction of the state and try apply "done" if it is possible
    def call_function(self):
        function_name = self.functions.get(self.currentState)
        if function_name:
            function = getattr(self, function_name, None)
            if function:
                function()
                if not(self.error):
                    self.doneInNextTransition()
                else:
                    self.error = False
            else:
                print(f"Function '{function_name}' not found.")
        else:
            print("No function associated with the current state.")

    
    # Creating a new exercise sheet
    def create(self):
        title = input("Title of the new sheet : ")
        self.currentSheet = Sheet(title)

    # Adding a new exercise in the database
    def add(self):
        ex_file = input("Exercise file name to add : ")
        bdmanager.add(ex_file)

    # Deleting an existing exercise in the database
    def delete(self):
        ex_file = input("Exercise file name to delete : ")
        bdmanager.delete(ex_file)

    def idle(self):
        return

    # Options for a created sheet
    def options(self):
        print("Options menu")


    def ok(self):
        print("création de la fiche : ",self.currentSheet.title,"et de son fichier respectif")
        self.currentSheet.toTyp()

    def title(self):
        print("Title menu")
        title = input()
        self.currentSheet.editTitle(title)

    def author(self):
        print("Author menu")
        author = input()
        try :
            self.currentSheet.editAuthor(author)
            self.currentState = State.OPTIONS
        except :
            raise Exception()

        

    def date(self):
        print("Date menu")
        date = input()
        self.currentSheet.editDate(date)


    def addex(self):
        ex = input("try with ../BD/TYPST/exo1.typ :")
        self.currentSheet.add(ex)

    def delex(self):
        print("Deleting exercise menu")
        ex = input("try with ../BD/TYPST/exo1.typ :")
        self.currentSheet.delete(ex)

    def quit(self):
        print("Quit the current sheet")
        self.currentSheet = None

    def out(self):
        return

    def editex(self):
        self.currentSheet.displayExercisesNames()

        if(self.currentSheet.ex==None):
            print("There are no exercises to edit.")
            return
        
        name=input("name of the exercise you want to edit :")
        for exo in self.currentSheet.ex:
            if exo.metadata["name"] == name:
                self.currentExo=exo
                self.currentSheet.displayExercisesNames()

                return
            
        self.currentExo=None
        print("Exercices not fond")
        return 
    
    def addvisibleex(self):
        self.currentExo.printFieldNotVisible()

        if(self.currentExo==None):
            print("Exercise Name invalid please enter a valid name")
            self.currentState=State.EDITEX
            return 
        field = input("Field name to add : ")
        self.currentExo.addVisible(field)
        return
    
    def delvisibleex(self):
        self.currentExo.printFieldVisible()
        if(self.currentExo==None):
            print("Exercise Name invalid please enter a valid name")
            self.currentState=State.EDITEX
            return 
        field = input("Field name to del : ")
        self.currentExo.removeVisible(field)
        return

    def main(self):
        
        while self.currentState != State.OUT:
            # Displaying valid events for the current state
            valid = self.valid_events()
            colored_events = [f"\033[92m{event}\033[0m" for event in valid]
            print(f"\nPossible events : {', '.join(colored_events)}")
            # Transition from the current state to the next state, in function of the action entered
            action = input("Enter an action : ").strip().lower()
            self.currentState = self.transition(action)
            print("Current state :", self.currentState)
            
            # Calling the function, result of the transition
            self.call_function()

            


def main():
    aut = Automaton()
    aut.main()