import sys
import re

import colorama 

class Exercise:
    def __init__(self, content, meta=None, name=None, title=None, duration=None, difficulty=None, solution=None, figures=None, points=None, bonus=None, author=None, references=None, language=None, material=None, solution_content=None):
        
        if (meta != None):
            self.metadata = meta
        else:
            self.metadata = {"title" : title,  # Title of the exercise
                            "duration" : duration,
                            "difficulty" : difficulty,
                            "solution" : solution,  # Boolean indicating if there is a solution to the end of the exercise
                            "points" : points,
                            "bonus" : bonus,  # Boolean indicating if the exercise is bonus
                            "author" : author,
                            "references" : references,
                            "language" : language,
                            "material" : material,
                            "name" : name  # Output name of the exercise (without extension)
            }


        # Dictionary of all visible fields on the final output
        self.visible = {"title" : title,
                        "duration" : duration,
                        "points" : points
        }

        self.content = content
        self.solution = solution_content
    

    def printFieldNotVisible(self):
        print("Invisible Field: " + colorama.Fore.LIGHTCYAN_EX + "", end="")
        not_visible_fields = set(self.metadata.keys()) - set(self.visible.keys())
        print(", ".join(not_visible_fields) + colorama.Fore.RESET + "")
        
    
    def printFieldVisible(self):
        print("Visible Field: " + colorama.Fore.LIGHTCYAN_EX + "", end="")
        print(", ".join(self.visible.keys()) + colorama.Fore.RESET + "")       
 
    
    # Add the field (string) to the dictionary of visible fields
    def addVisible(self, field):

        if field in self.visible.keys():
            print(colorama.Fore.BLUE + "Field is already visible.")

            self.printFieldNotVisible()
            raise ValueError("Error: Field is already visible")
        
        elif field in self.metadata.keys():
            self.visible[field] = self.metadata[field]
            print("Field ", field, " is now visible")

        else:
            print("\033[91mError: Invalid field.\033[0m Please enter one of the field:")
            self.printFieldNotVisible()
            raise ValueError("Error: Invalid field")
            

        
    # Remove the field (string) to the dictionary of visible fields
    def removeVisible(self, field):
        if field in self.visible.keys():
            self.visible.pop(field)
            print("Field", field, "is now invisible dictionary.")

        elif field in self.metadata.keys():
            print("Field", field, "is already invisible dictionary. Please enter one of the visible fields : ")
            self.printFieldVisible()
            raise ValueError("Error: Field already invisible")
        else:
            print("\033[91mError: Invalid field \033[0m Please enter one of the visible fields:")
            self.printFieldVisible()
            raise ValueError("Error: Invalid field")

        

def initMeta():
    return {"title" : None,
            "duration" : None,
            "difficulty" : None,
            "solution" : None, # booléen indiquant s'il y a une solution à la fin du fichier .typ
            "figures" : None,
            "points" : None,
            "bonus" : None, # booléen indiquant si l'exercice est facultatif ou non
            "author" : None,
            "references" : None,
            "language" : None,
            "material" : None,
            "name" : None
            }

def loadExercise(path):
    ext = path.split(".")[-1]
    
    if ext == "typ":
        path = "BD/TYPST/" + path
        return loadExerciseTypst(path)
    elif ext == "tex":
        path = "BD/LATEX/" + path
        return loadExerciseLatex(path)
    else:
        print("format not supported try with .typ or .tex")
        raise ValueError("format not supported try with .typ or .tex")


def loadExerciseLatex(path):
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"The file '{path}' could not be found.")
        raise FileNotFoundError(f"The file could not be found.")
    
    #meta_match = re.findall(r'\\setMeta\{([^}]+)\}\{([^}]+)\}', content)
    meta_match = re.findall(r'\\setMeta\{([^}]+)\}\{([^}]*)\}', content)
    exercise_match = re.search(r'\\section\{Exercice\}(.*?)\\section\{Solution\}', content, re.DOTALL)
    solution_match = re.search(r'\\section\{Solution\}(.*?)\Z', content, re.DOTALL)

    solution = None

    if meta_match:
        metadata = dict(meta_match)
        for key, value in meta_match:
            metadata[key] = value if value != "" else None

    
    if exercise_match:
        content = exercise_match.group(1).strip()

    if solution_match:
        solution = solution_match.group(1).strip()

    print(metadata)
    # Object exercise creation

    for key in metadata.keys():
        if metadata[key] ==  "":
            metadata[key] = None

    ex = Exercise(meta=metadata, content=content, solution_content=solution)

    return ex

def loadExerciseTypst(path):
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"The file '{path}' could not be found.")
        raise FileNotFoundError(f"The file could not be found.")
            

    meta_match = re.search(r'#show terms: meta => {(.*?)}', content, re.DOTALL)
    exercise_match = re.search(r'= Exercise(.*?)= Solution', content, re.DOTALL)
    solution_match = re.search(r'= Solution\n(.*?)$', content, re.DOTALL)

    solution = None

    if meta_match:
        metadata = dict(re.findall(r'let\s+(\w+)\s*=\s*label\("(.*?)"\)', meta_match.group(1)))

    if exercise_match:
        content = exercise_match.group(1).strip()
    else: 
        print("The file does not contain the '= Exercise' tag.")
        raise ValueError("The file does not contain the '= Exercise' tag.")

    if solution_match:
        solution = solution_match.group(1).strip()

    # Object exercise creation

    for key in metadata.keys():
        if metadata[key] ==  "":
            metadata[key] = None

    if(not metadata.get('name') or not metadata['name']):
        print("'name' attribute missing")
        raise ValueError("The file does not contain the a 'name' tag.")
    
    ex = Exercise(meta=metadata, content=content, solution_content=solution)
    
    
    return ex

# loadExerciseLatex("BD/LATEX/format.tex")