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
        self.currentExo:Exercise = None
        self.transitions = {
            State.IDLE: {"add": State.ADD, 
                         "delete": State.DEL, 
                         "create": State.CREATE, 
                         "out": State.OUT},
            State.ADD: State.IDLE,
            State.DEL: State.IDLE,
            State.CREATE: State.OPTIONS,
            State.OPTIONS: {"ok" : State.OK,
                                "title": State.TITLE, 
                                "author": State.AUTHOR, 
                                "date": State.DATE,
                                "addex": State.ADDEX,
                                "delex": State.DELEX,
                                "editex":State.EDITEX,
                                "quit": State.QUIT,
                                },
            State.OK: State.IDLE,
            State.TITLE: State.OPTIONS,
            State.AUTHOR: State.OPTIONS,
            State.DATE: State.OPTIONS,
            State.DELEX: State.OPTIONS,
            State.ADDEX: State.OPTIONS,
            State.QUIT: State.IDLE,
            State.EDITEX: {"addvisible" : State.ADDVISIBLEEX,
                          "delvisible" : State.DELVISIBLEEX,
                          "quit" : State.OPTIONS},
            State.ADDVISIBLEEX: State.EDITEX,
            State.DELVISIBLEEX: State.EDITEX,
            State.OUT : {}
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

        self.error = False # This flag allows the automata to manage errors

    ## FUNCTIONS ENABLING THE PROPER FreturnUNCTIONING OF THE AUTOMATON.

    # Returns the valid possible events for the current state
    def valid_events(self):

        if isinstance(self.transitions.get(self.currentState, {}), State):
            return self.currentState
        else:
            return list(self.transitions.get(self.currentState, {}).keys())

    # Determines the next state of the controller based on the current state and the triggered event.
    def transition(self, event=None):

        state_possible = self.transitions.get(self.currentState, {})
        next_state = state_possible.get(event) if event else state_possible

        # Invalid event management
        if next_state == None:
            valid = self.valid_events()
            print("\033[91mError: Invalid event.\033[0m Please enter one of the following events:")
            for option in valid:
                print(f"- \033[92m{option}\033[0m")
            return self.currentState
        else:
            return next_state

    # Call the function associated with the current state and executes it if found, otherwise it prints an error message.
    def call_function(self):
        try:
            function_name = self.functions.get(self.currentState)
            try:
                function = getattr(self, function_name, None)
                function()
            except Exception:
                    print(f"Function '{function_name}' not found.")
        except Exception:
            print("No function associated with the current state.")
    
    ## FUNCTIONS CALLED FOR EACH TRANSITION IN THE AUTOMATA

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

    def out(self):
        return
    
    # Options for a created sheet
    def options(self):
        return

    def ok(self):
        try:
            self.currentSheet.toTyp()
        except BaseException:
            print("Sheet creation couldn't have been done")
        
        print("Sheet creation : ", self.currentSheet.title)

    def title(self):
        title = input()
        try:
            self.currentSheet.editTitle(title)
        except BaseException:
            print("Title modification couldn't have been done")


    def author(self):
        author = input()
        try:
            self.currentSheet.editAuthor(author)
        except BaseException:
            print("Author modification couldn't have been done")

    def date(self):
        date = input()
        try:
            self.currentSheet.editDate(date)
        except BaseException:
            print("Date modification couldn't have been done")


    def addex(self):
        ex = input("File to add : ")
        try:
            self.currentSheet.add(ex)
        except BaseException:
            print("Addex couldn't have been done")

    def delex(self):
        ex = input("File to delete : ")
        try:
            self.currentSheet.delete(ex)
        except BaseException:
            print("Delex couldn't have been done")

    def editex(self):

        if self.currentSheet.ex == []:
            print("There are no exercises to edit, please add an exercise before")
            self.currentState = State.OPTIONS
        else:
            self.currentSheet.displayExercisesNames()
        
            name = input("Name of the exercise you want to edit : ")
            for exo in self.currentSheet.ex:
                if exo.metadata["name"] == name:
                    self.currentExo = exo
        
    def addvisibleex(self):
        self.currentExo.printFieldNotVisible()

        if self.currentExo == None:
            print("Name exercise invalid, please enter a valid name")
            self.currentState = State.EDITEX

        field = input("Field name to add : ")

        try:
            self.currentExo.addVisible(field)
        except BaseException:
            print("AddVisibleEx couldn't have been done")

    def delvisibleex(self):
        self.currentExo.printFieldVisible()

        if self.currentExo == None:
            print("Name exercise invalid, please enter a valid name")
            self.currentState = State.EDITEX
            
        field = input("Field name to del : ")

        try:
            self.currentExo.removeVisible(field)
        except BaseException:
            print("DelVisibleEx couldn't have been done")
    
    def quit(self):
        print("Quit the current sheet")
        self.currentSheet = None

    def main(self):
        
        while self.currentState != State.OUT:
            # Displaying valid events for the current state
            valid = self.valid_events()

            if not isinstance(valid, State):  
                colored_events = [f"\033[92m{event}\033[0m" for event in valid]
                print(f"\nPossible events : {', '.join(colored_events)}")

                # Transition from the current state to the next state, in function of the action entered
                action = input("Enter an action : ").strip().lower()
            else:
                action = None
                
            self.currentState = self.transition(action)

            # Calling the function, result of the transition
            self.call_function()

            


def main():
    aut = Automaton()
    aut.main()
