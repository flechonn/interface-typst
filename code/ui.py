# User Interactions 
# This file listens to user requests and offers three choices: add, delete, and create. It cannot change modes.
from enum import Enum

import sheet as s
import bdmanager 

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
    OUT = 12


class Automaton:

    def __init__(self):
        self.currentSheet = None
        self.currentState = State.IDLE
        self.TRANSITIONS = {
            State.IDLE: {"add": State.ADD, "delete": State.DEL, "create": State.CREATE, "out":State.OUT},
            State.ADD: {"done": State.IDLE},
            State.DEL: {"done": State.IDLE},
            State.CREATE: {"done": State.OPTIONS},
            State.OPTIONS: {"ok" : State.OK,
                                "title": State.TITLE, #to add to automton graph 
                                "author": State.AUTHOR, 
                                "date": State.DATE,
                                "addex": State.ADDEX,
                                "delete": State.DELEX,
                                "quit": State.QUIT,
                                },
            State.OK: {"done" : State.IDLE},
            State.TITLE: {"done": State.OPTIONS},
            State.AUTHOR: {"done": State.OPTIONS},
            State.DATE: {"done": State.OPTIONS},
            State.DELEX: {"done": State.OPTIONS},
            State.ADDEX: {"done": State.OPTIONS},
            State.QUIT:{"done":State.IDLE},
            State.OUT:{}
        }
        
        self.functions = {
            State.IDLE: "idle", #lambda: None,  # Aucune action à effectuer pour l'état IDLE
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
            State.OUT: "out"
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
    
    def transition_done(self,event):
        self.transition(event)
        self.transition("done")

    def call_function(self):
        function_name = self.functions.get(self.currentState)
        if function_name:
            # function = globals().get(function_name)
            function = getattr(self, function_name, None)
            if function:
                function()
            else:
                print(f"Function '{function_name}' not found.")
        else:
            print("No function associated with the current state.")

    
    # Creating a new exercise sheet
    def create(self):
        title = input("Title of the new sheet : ")
        self.currentSheet = s.Sheet(title)

        self.currentState = State.OPTIONS

    # Adding a new exercise in the database
    def add(self):
        ex_file = input("Exercise file name to add : ")
        bdmanager.add(ex_file)

        self.currentState = State.IDLE

    # Deleting an existing exercise in the database
    def delete(self):
        ex_file = input("Exercise file name to delete : ")
        bdmanager.delete(ex_file)

        self.currentState = State.IDLE

    def idle(self):
        return

    # Options for a created sheet
    def options(self):
        print("Options menu")

    def ok(self):
        print("OK")
        # self.currentState = State.IDLE

    def title(self):
        print("Title menu")
        title = input()
        self.currentSheet.editTitle(title)

        # self.currentState = State.OPTIONS

    def author(self):
        print("Author menu")
        author = input()
        self.currentSheet.editAuthor(author)

        # self.currentState = State.OPTIONS

    def date(self):
        print("Date menu")
        date = input()
        self.currentSheet.editDate(date)

        # self.currentState = State.OPTIONS

    def addex(self):
        print("Adding exercise menu")
        ex = input()
        self.currentSheet.add(ex)

        # self.currentState = State.OPTIONS

    def delex(self):
        print("Deleting exercise menu")
        ex = input()
        self.currentSheet.add(ex)

        # self.currentState = State.OPTIONS

    def quit(self):
        print("Quit the current sheet")
        self.currentSheet = None

        # self.currentState = State.IDLE

    def out(self):
        return


    def main(self):
        
        while self.currentState != State.OUT:
            # Displaying valid events for the current state
            valid = self.valid_events()
            colored_events = [f"\033[92m{event}\033[0m" for event in valid]
            print(f"Possible events : {', '.join(colored_events)}")

            # Transition from the current state to the next state, in function of the action entered
            action = input("Enter an action : ").strip().lower()
            self.currentState = self.transition_done(action)
            print("Current state :", self.currentState)

            # Calling the function, result of the transition
            self.call_function()


def main():
    aut = Automaton()
    aut.main()