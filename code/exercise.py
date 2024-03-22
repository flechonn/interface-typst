import sys
import re 

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

    def printExercise(self):
        print(self.metadata)
        print(self.content)
    
    # Add the field (string) to the dictionary of visible fields
    def addVisible(self, field):
        self.visible[field] = self.metadata[field]
        
    # Remove the field (string) to the dictionary of visible fields
    def removeVisible(self, field):
        self.visible.pop(field)

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

    ex = Exercise(meta=metadata, content=content, solution=solution)

    return ex

def loadExercise(path):
    ext = path.split(".")[-1]

    if(ext == "typ"):
        loadExerciseTypst(path)
    else:
        loadExerciseLatex(path)


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

    ex = Exercise(meta=metadata, content=content, solution=solution)
    print(metadata)
    return ex

loadExerciseTypst("../BD/TYPST/format.typ")