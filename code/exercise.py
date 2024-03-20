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

    def printFieldNotVisible(self):
        not_visible_fields = set(self.metadata.keys()) - set(self.visible.keys())
        for field in not_visible_fields:
            print(field)
    
    def printFieldVisible(self):
        for field in self.visible.keys():
            print(field)
    
    def printExercise(self):
        print(self.metadata)
        print(self.content)
    
    # Add the field (string) to the dictionary of visible fields
    def addVisible(self, field):
        if field in self.metadata.key():
            self.visible[field] = self.metadata[field]
            print("field : ",field," is now visible")
        else:
            print("\033[91mError: Invalid field.\033[0m Please enter one of the field:")
            self.printFieldNotVisible()
            

        
    # Remove the field (string) to the dictionary of visible fields
    def removeVisible(self, field):
        if field in self.visible.keys():
            self.visible.pop(field)
            print("Field:", field, "has been removed from the visible dictionary.")
        else:
            print("\033[91mError: Invalid field or field already invisible.\033[0m Please enter one of the visible fields:")
            self.printFieldVisible()

        
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
    ext = path.split(".")[-1]
    if(ext == "typ"):
        return loadExerciseTypst(path)
    else:
        return loadExerciseLatex(path)


def loadExerciseTypst(path):
    f = open(path, 'r')
    lines = f.readlines()
    
    exercise = Exercise(None)

    # Metadatas do not have a precise order in the formatted Typst file
    for line in lines:

        extractedwords = re.search(r'let\s+(\w+)\s+=\s+label\("([^"]*)"\)', line)
        if (extractedwords != None):
            key = extractedwords.group(1)
            key = key.replace("\my", "")
            value = extractedwords.group(2)

            if (value == ""):
                value = None

            exercise.metadata[key] = value
    
    return exercise