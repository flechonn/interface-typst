import sys
import ui
import bdmanager as bd
from sheet import *

def create(ex, output):
    sheet = Sheet(output)
    for e in ex:
        sheet.add(e)

    sheet.toTyp()

def manualMode(args):
    match(args[1]):
        case "-h":
            print("\n-add <EX1> : add the file EX1 to the database")
            print("-del <EX1> : delete the file EX1 from the database\n")
            print("-create <EX1> <EX2> ... <EXN> <OUTPUT_FILE> : create a new file named OUTPUT_FILE with EX1, EX2, until EXN")

        case "-add":
            bd.add(args[2])

        case "-del":
            bd.delete(args[2])
            
        case "-create":
            ex = args[2: len(args)-1]
            output = args[-1]
            create(ex, output)
            print("The sheet " + output + " has been successfully created")

def main():
    # Retrieving command line arguments 
    args = sys.argv

    if len(sys.argv) >= 2: # Lauching manual mode
        print("Manual mode")
        manualMode(args)
        return
    else: # Lauching interactive mode
        print("Interactive mode")
        ui.main()
    

if __name__ == "__main__":
    main()
