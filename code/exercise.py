import sys

class Exercice:
    def __init__(self, id, title=None, duration=None, difficulty=None, solution=None, figures=None, points=None, bonus=None, author=None, references=None, language=None, material=None):
        self.id = id
        self.title = title
        self.duration = duration
        self.difficulty = difficulty
        self.solution = solution # booléen indiquant s'il y a une solution à la fin du fichier .typ
        self.figures = figures
        self.points = points
        self.bonus = bonus # booléen indiquant si l'exercice est facultatif ou non
        self.author = author
        self.references = references
        self.language = language
        self.material = material

        # List of all visible fields on the created sheet
        self.visible = [self.title, self.duration, self.difficulty, self.figures, self.points, self.bonus]

        # If the field visible is empty, we remove 
        self.visible = [x for x in self.visible if x]
        
    
    def get_id(self):
        return self.id

  
    # Each exercise is represented by a file.
    # Each line contains one information of the exercise separated by a specific delimiter
    # The information is not stored in a specific order, if there is no information the data is set to null
    @classmethod
    def load_exercises_from_file(cls, filename):
        #TODO
        exercises_list = []
        with open(filename, 'r') as file:
            lines = file.readlines()
    
    # Getters and setters (à voir si on les met ou pas)


# Add a field (string) to a list of visible fields so that it is displayed
# if the value is not in the list an error is returned

def addVisible(self, field):
    match field:
        case "title":
            self.visible.append(self.title)
        case "duration":
            self.visible.append(self.duration)
        case "difficulty":
            self.visible.append(self.difficulty)
        case "solution": 
            self.visible.append(self.duration)
        case "figures": 
            self.visible.append(self.figures)
        case "points":
            self.visible.append(self.points)
        case "bonus": 
            self.visible.append(self.bonus)
        case "author":
            self.visible.append(self.author)
        case "references":
            self.visible.append(self.references)
        case "language":
            self.visible.append(self.languages)
        case "material":
            self.visible.append(self.material)
        
        case _: 
            print("Not existing field")
    


# remove a field (string) to a list of visible fields so that it is displayed
# if the value is not in the list an error is returned

def removeVisible(self, field):
    match field:
        case "title":
            self.visible = set(self.visible.remove(self.title))
        case "duration":
            self.visible.remove(self.duration)
        case "difficulty":
            self.visible.remove(self.difficulty)
        case "solution": 
            self.visible.remove(self.duration)
        case "figures": 
            self.visible.remove(self.figures)
        case "points":
            self.visible.remove(self.points)
        case "bonus": 
            self.visible.remove(self.bonus)
        case "author":
            self.visible.remove(self.author)
        case "references":
            self.visible.remove(self.references)
        case "language":
            self.visible.remove(self.language)
        case "material":
            self.visible.remove(self.material)
        case _: 
            print("Not existing field")
