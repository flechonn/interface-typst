import sys
import re 

class Exercise:
    def __init__(self, content, name=None, title=None, duration=None, difficulty=None, solution=None, figures=None, points=None, bonus=None, author=None, references=None, language=None, material=None, solution_content=None):
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

def loadExerciseLatex(path):

    f = open(path, 'r')
    lines = f.readlines()
    
    exercise = Exercise(None)

    # Metadatas do not have a precise order in the formatted LaTeX file
    for line in lines:

        extractedwords = re.search(r'\\setMeta\{(\w+)\}\{([^}]*)\}', line)
        if (extractedwords != None):
            key = extractedwords.group(1)
            key = key.replace("\my", "")
            value = extractedwords.group(2)

            if (value == ""):
                value = None

            exercise.metadata[key] = value
    
    return exercise

def loadExercise(path):
    ext = ext = path.split(".")[-1]

    if(ext == "typ"):
        loadExerciseTypst(path)
    else:
        loadExerciseLatex(path)


def loadExerciseTypst(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' est introuvable.")
        exit()

    meta_match = re.search(r'#show terms: meta => {(.*?)}', content, re.DOTALL)
    exercise_match = re.search(r'= Exercise(.*?)= Solution', content, re.DOTALL)
    solution_match = re.search(r'#show terms: solution => {(.*?)}', content, re.DOTALL)

    if meta_match:
        metadata = dict(re.findall(r'let\s+(\w+)\s*=\s*label\("(.*?)"\)', meta_match.group(1)))

    if exercise_match:
        content = exercise_match.group(1).strip()

    if solution_match:
        solution = solution_match.group(1).strip()

    # Object exercise creation

    ex = Exercise(None)
    ex.metadata = metadata
    ex.content = content
    ex.solution = solution

    return ex
