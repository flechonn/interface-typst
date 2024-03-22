import sys
import re

import colorama 

class Exercise:
    def __init__(self, content, meta=None, name=None, title=None, duration=None, difficulty=None, solution=None, figures=None, points=None, bonus=None, author=None, references=None, language=None, material=None, solution_content=None):
        
        if (meta != None):
            self.metadata = meta
        else:
            self.metadata = {"title" : title,
                            "duration" : duration,
                            "difficulty" : difficulty,
                            "solution" : solution, # booléen indiquant s'il y a une solution à la fin du fichier .typ
                            "figures" : figures,
                            "points" : points,
                            "bonus" : bonus, # booléen indiquant si l'exercice est facultatif ou non
                            "author" : author,
                            "references" : references,
                            "language" : language,
                            "material" : material,
                            "name" : name
            }


        # Dictionary of all visible fields on the final output
        self.visible = dict(self.metadata)
        self.visible.pop("solution")
        self.visible.pop("author")
        self.visible.pop("references")
        self.visible.pop("language")
        self.visible.pop("material")

        self.content = content
        self.solution = solution_content
    
    def get_id(self):
        return self.id

    def printFieldNotVisible(self):
        print("Invisible Field: "+colorama.Fore.LIGHTCYAN_EX +"", end="")
        not_visible_fields = set(self.metadata.keys()) - set(self.visible.keys())
        print(", ".join(not_visible_fields)+colorama.Fore.RESET+"")
        
    
    def printFieldVisible(self):
        print("Visible Field: "+colorama.Fore.LIGHTCYAN_EX +"", end="")
        print(", ".join(self.visible.keys())+colorama.Fore.RESET+"")       
 
    
    def printExercise(self):
        print(self.metadata)
        print(self.content)
    
    # Add the field (string) to the dictionary of visible fields
    def addVisible(self, field):
        if field in self.visible.keys():
            print(colorama.Fore.BLUE+"Error: field is already visible.")
            self.printFieldNotVisible()
        elif field in self.metadata.keys():
            self.visible[field] = self.metadata[field]
            print("field : ",field," is now visible")
        else:
            print("\033[91mError: Invalid field.\033[0m Please enter one of the field:")
            self.printFieldNotVisible()
            

        
    # Remove the field (string) to the dictionary of visible fields
    def removeVisible(self, field):
        if field in self.visible.keys():
            self.visible.pop(field)
            print("Field:", field, "is now invisible dictionary.")
        elif field in self.metadata.keys():
            print("Field:", field, "is already invisible dictionary. Please enter one of the visible fields:")
            self.printFieldVisible()
        else:
            print("\033[91mError: Invalid field \033[0m Please enter one of the visible fields:")
            self.printFieldVisible()

        


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

def loadExerciseLatex(path):
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Le fichier '{path}' est introuvable.")
        exit()
    
    meta_match = re.findall(r'\\setMeta\{(\w+)\}\{(.+?)\}', content, re.DOTALL)
    exercise_match = re.search(r'\\section\{Exercice\}(.*?)\\section\{Solution\}', content, re.DOTALL)
    solution_match = re.search(r'\\section\{Solution\}(.*?)\Z', content, re.DOTALL)

    if meta_match:
        metadata = initMeta()
        for key, value in meta_match: metadata[key] = value
    
    if exercise_match:
        content = exercise_match.group(1).strip()

    if solution_match:
        solution = solution_match.group(1).strip()

    # Object exercise creation

    for key in metadata.keys():
        if metadata[key] ==  "":
            metadata[key] = None

    ex = Exercise(meta=metadata, content=content, solution_content=solution)

    return ex

def loadExercise(path):
    ext = path.split(".")[-1]

    if(ext == "typ"):
        return loadExerciseTypst(path)
    else:
        return loadExerciseLatex(path)


def loadExerciseTypst(path):
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Le fichier '{path}' est introuvable.")
        exit()

    meta_match = re.search(r'#show terms: meta => {(.*?)}', content, re.DOTALL)
    exercise_match = re.search(r'= Exercise(.*?)= Solution', content, re.DOTALL)
    solution_match = re.search(r'= Solution\n(.*?)', content, re.DOTALL)

    if meta_match:
        metadata = dict(re.findall(r'let\s+(\w+)\s*=\s*label\("(.*?)"\)', meta_match.group(1)))

    if exercise_match:
        content = exercise_match.group(1).strip()

    if solution_match:
        solution = solution_match.group(1).strip()

    # Object exercise creation

    for key in metadata.keys():
        if metadata[key] ==  "":
            metadata[key] = None

    ex = Exercise(meta=metadata, content=content, solution_content=solution)
    return ex