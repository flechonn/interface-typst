import sys
import ui

def main():
    # Retrieving command line arguments 
    args = sys.argv

    if len(sys.argv) != 0: # Lauching manual mode
        # TODO
        print("Manual mode")
        return
    else: # Lauching interactive mode
        print("Interactive mode")
        ui.main()
    

if __name__ == "__main__":
    main()
