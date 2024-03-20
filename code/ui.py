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
        self.currentSheet:Sheet = None
        self.currentState = State.IDLE
        self.currentExo:Exercise=None
        self.TRANSITIONS = {
            State.IDLE: {"add": State.ADD, 
                         "delete": State.DEL, 
                         "create": State.CREATE, 
                         "out":State.OUT},
            State.ADD: {"done": State.IDLE},
            State.DEL: {"done": State.IDLE},
            State.CREATE: {"done": State.OPTIONS},
            State.OPTIONS: {"ok" : State.OK,
                                "title": State.TITLE, 
                                "author": State.AUTHOR, 
                                "date": State.DATE,
                                "addex": State.ADDEX,
                                "delete": State.DELEX,
                                "editex":State.EDITEX,
                                "quit": State.QUIT,
                                },
            State.OK: {"done" : State.IDLE},
            State.TITLE: {"done": State.OPTIONS},
            State.AUTHOR: {"done": State.OPTIONS},
            State.DATE: {"done": State.OPTIONS},
            State.DELEX: {"done": State.OPTIONS},
            State.ADDEX: {"done": State.OPTIONS},
            State.QUIT:{"done":State.IDLE},
            State.EDITEX:{"addvisible":State.ADDVISIBLEEX,
                          "delvisible":State.DELVISIBLEEX,
                          "quit":State.OPTIONS},
            State.ADDVISIBLEEX:{"done":State.EDITEX},
            State.DELVISIBLEEX:{"done":State.EDITEX},
            State.OUT:{}
        }
        
        self.functions = {
            State.IDLE: "idle", 
            State.ADD: "add",
            State.DEL: "delete",
            State.CREATE: "create",
            State.OPTIONS: "options",
            State.OK: "ok",
            State.TITLE: "title",
            State.AUTHOR: "author",
            State.DATE: "date",
            State.ADDEX: "addex",
            State.DELEX: "delex",
            State.QUIT: "quit",
            State.OUT: "out",
            State.EDITEX:"editex",
            State.ADDVISIBLEEX:"addvisibleex",
            State.DELVISIBLEEX:"delvisibleex"
        }


    #retrieves valid events for a given state of the State.:
    #state is a parameter which corresponds to a state of the State 
    def valid_events(self):
        return list(self.TRANSITIONS.get(self.currentState, {}).keys())

    # The transition(state, event) function takes two arguments: 
    # - the current state of the State (state) 
    # - the event (event) triggered by the user. 
    # It uses this information to determine the next state of the controller.  
    def transition(self, event):
        state_possible = self.TRANSITIONS.get(self.currentState, {})
        next_state = state_possible.get(event)

        if next_state is None:
            valid = self.valid_events()
            print("\033[91mError: Invalid event.\033[0m Please enter one of the following events:")
            for option in valid:
                print(f"- \033[92m{option}\033[0m")
            return self.currentState
        return next_state

    def doneInNextTransition(self):
        valid = self.valid_events()
        if "done" in valid:
            self.currentState = self.transition("done")

    #call the fonction of the state and try apply "done" if it is possible
    def call_function(self):
        function_name = self.functions.get(self.currentState)
        if function_name:
            function = getattr(self, function_name, None)
            if function:
                function()
                self.doneInNextTransition()
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
        print("OK")

    def title(self):
        print("Title menu")
        title = input()
        self.currentSheet.editTitle(title)

    def author(self):
        print("Author menu")
        author = input()
        self.currentSheet.editAuthor(author)

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
        self.currentSheet.add(ex)

    def quit(self):
        print("Quit the current sheet")
        self.currentSheet = None

    def out(self):
        return

    def editex(self):
        self.currentSheet.display_exercises()
        if(self.currentSheet.ex==None):
            print("There are no exercises to edit.")
            return
        
        name=input("name of the exercise you want to edit :")
        for exo in self.currentSheet.ex:
            if exo.name == name:
                self.currentExo=exo
                return
            
        self.currentExo=None
        print("Exercices not fond")
        return 
    
    def addvisibleex(self):
        if(self.currentExo==None):
            print("Exercise Name invalid please enter a valid name")
            self.currentState=State.EDITEX
            return 
        field = input("Field name to add : ")
        self.currentExo.addVisible(field)
        return
    
    def delvisibleex(self):
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
            print(f"Possible events : {', '.join(colored_events)}")
            # Transition from the current state to the next state, in function of the action entered
            action = input("Enter an action : ").strip().lower()
            self.currentState = self.transition(action)
            print("Current state :", self.currentState)
            
            # Calling the function, result of the transition
            self.call_function()

            


def main():
    aut = Automaton()
    aut.main()