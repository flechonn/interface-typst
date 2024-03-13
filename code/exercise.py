import sys

class Exercise:
    def __init__(self, id, title=None, duration=None, difficulty=None, solution=None, figures=None, points=None, bonus=None, author=None, references=None, language=None, material=None):
        self.metadata = {"id" : id,
                        "title" : title,
                        "duration" : duration,
                        "difficulty" : difficulty,
                        "solution" : solution, # booléen indiquant s'il y a une solution à la fin du fichier .typ
                        "figures" : figures,
                        "points" : points,
                        "bonus" : bonus, # booléen indiquant si l'exercice est facultatif ou non
                        "author" : author,
                        "references" : references,
                        "language" : language,
                        "material" : material
        }

        # Dictionary of all visible fields on the final output
        self.visible = dict(self.metadata)
        self.visible.pop("solution")
        self.visible.pop("author")
        self.visible.pop("references")
        self.visible.pop("language")
        self.visible.pop("material")

    
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
    
    # Add the field (string) to the dictionary of visible fields
    def addVisible(self, field):
        self.visible[field] = self.metadata[field]
        
    # Remove the field (string) to the dictionary of visible fields
    def removeVisible(self, field):
        self.visible.pop(field)
