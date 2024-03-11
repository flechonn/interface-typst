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

        # Liste de  tous les champs visibles sur la fiche créée
        self.visible = [self.title, self.duration, self.difficulty, self.figures, self.points, self.bonus]

        # Si le champ visible est vide, on l'enlève de la liste
        self.visible = [x for x in self.visible if x]

# LaTeX (formatted) to Typst (formatted)
    # def latex_to_typst(latex_file):
    #     file = open(latex_file, 'r')
        
    #     for line in file.read():

        
    
    def get_id(self):
        return self.id

    def display_exercice(self):
        print("Exercice" +{self.number}+":"+ {self.exercise})
        print("Solution:" +self.solution)
        print("Niveau d'indice:"+ {self.difficulty})

    @classmethod
    def load_exercises_from_file(cls, filename):
        exercises_list = []
        with open(filename, 'r') as file:
            lines = file.readlines()

        number, exercise, solution, difficulty = None, None, None, None

        for line in lines:
            line = line.strip()
            if line.startswith('='):
                # A new exercise block is starting
                if number is not None:
                    # If this is not the first block, add the previous exercise to the list
                    exercises_list.append(cls(number, exercise, solution, difficulty))

                # Reset variables for the new exercise block
                number, exercise, solution, difficulty = None, None, None, None
            elif line.startswith('Exercice'):
                number = int(line.split(':')[0].split()[1])
                exercise = line.split(':')[1].strip()
            elif line.startswith('Solution'):
                solution = line.split(':')[1].strip()
            elif line.startswith('Niveau d\'indice'):
                difficulty = line.split(':')[1].strip()

        # Add the last exercise to the list
        if number is not None:
            exercises_list.append(cls(number, exercise, solution, difficulty))

        return exercises_list
