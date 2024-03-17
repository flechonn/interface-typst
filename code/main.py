import sys
import ui

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py fichier1 fichier2 ...")
        sys.exit(1)
    
    output = open("output_file.typ", "w")
  
    args= sys.argv

    print("pour avoir la sortie en pdf: typst compile output_file.typ")


if __name__ == "__main__":
    main()
    ui.main()
