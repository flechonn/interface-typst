import sys
from exercise import Exercice

def lire_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
            print(f"Contenu du fichier {nom_fichier} :\n{contenu}")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py fichier1 fichier2 ...")
        sys.exit(1)
    
    output = open("output_file.typ", "w")

        
    args= sys.argv
    
    
    #fusion de fichier 
    for file in args[1:]:
        print(file)
        f = open(file, "r")
        output.write("\n= New file : " + file + "\n")
        content = f.read()
        output.write(content)
        
    print("pour avoir la sortie en pdf: typst compile output_file.typ")
    
def tests(test_files):
    #test_files = 

    for file in test_files:

        
    
if __name__ == "__main__":
    main()
