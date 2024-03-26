# This file contains the functions that operate on Exercise objects. 
# It is also responsible for managing the typ output.

from exercise import *

class Sheet:
    def __init__(self, title, logo=None, author=None, date=None, modality=None, duration=None, ex=[], output=None):
        self.title = title
        self.logo = logo
        self.heading = {"author" : author,
                        "date" : date,
                        "duration" : duration
        }
        self.modality = modality
        self.ex: list[Exercise] = ex # List of exercise paths existing in the sheet
        self.output = title+".typ" # Name of the output file
    
    def displayExercises(self):
        print("List of exercises:")
        for i, exercise in enumerate(self.ex, 1):
            print(f"exercise number {i}")
            exercise.printExercise()
    
    def displayExercisesNames(self):
        print("List of exercises:")
        if not self.ex:
            print("No exercises available in :",self.title)
        else :
            for i, exercise in enumerate(self.ex, 1):
                name=exercise.metadata["name"]
                print("exercise name :",colorama.Fore.GREEN+"",name+colorama.Fore.RESET)
            
        
    # Adding an exercise to the actual exercise sheet
    def add(self, path):
        exo=loadExercise(path)
        self.ex.append(exo)
        print(exo.metadata["name"],"added to sheet")
        

    # Deleting an exercise existing in the actual exercise sheet
    def delete(self, name):
        for exo in self.ex:
            if exo.metadata["name"] == name:
                self.ex.remove(exo)
                return    
        print("Error name unknow")
        

    # Functions editing the heading format
    def editTitle(self, title):
        self.title = title
    
    def editAuthor(self, author):
        self.heading["author"] = author
    
    def editDate(self, date):
        self.heading["date"] = date
    
    def editModality(self, modality):
        self.modality = modality
    
    def editDuration(self, duration):
        self.heading["duration"] = duration



    # Converting Sheet object to .typ file
    def toTyp(self):
        
        with open(self.output, 'w') as f:
            template = "BD/TYPST/utilities.typ"
            f.write(f'#import "{template}" :* \n')
            
            ## SHEET HEADER ##
        
            #title 
            f.write("#show: title \n")
            f.write(" \ \n" + self.title + "\n")

            #logo
            if(self.logo):
                logo_input = '#place(top + right, image("' + self.logo + '", width: 15%))\n'
                f.write(logo_input)
            f.write("#show: lines \n")

            #heading - Author, date, duration
            f.write("#show: header \n")
            if self.heading:
                formatted_headings = []  # Liste pour stocker les en-têtes formatés
                for head, value in self.heading.items():
                    if value:
                        formatted_headings.append(f"{head} : {value}")
                formatted_line = " - ".join(formatted_headings)  # Concaténation avec des tirets
                f.write(formatted_line + " \ \n")
                        
            #modality
            f.write("#show: modality \n")
            if self.modality :
                f.write(self.modality + " \ \n")
            f.write("#show: lines \n \ \n")
            
            
            ## SHEET CONTENT

            #exercise
            for exo in self.ex :
                solution_visible = False
                
                #header exercise
                main_heading = [] # for title, bonus, points and duration
                other_heading = [] # for other metadata (those less useful)
                
                shown_header = ["title", "bonus", "points", "duration"]
                
                main_heading.append("#main_meta[")
                if exo.metadata["title"]:
                    main_heading.append("title " + exo.metadata["title"] + " ")
                    
                if exo.metadata["bonus"]:
                    if exo.metadata["bonus"] == "1":
                        main_heading.append("bonus ")
                        
                main_heading.append("#h(1fr) ")
                if exo.metadata["duration"]:
                    if exo.metadata["points"]:
                        main_heading.append(f"duration ($tilde.op$ " + exo.metadata["duration"] + ") | ")
                    else :
                        main_heading.append("duration " + exo.metadata["duration"])
                        
                if exo.metadata["points"]:
                    main_heading.append("points " + exo.metadata["points"])
                main_heading.append("] \ \n")
                
                f.write(''.join(main_heading) + "\n")
                
                f.write("#show: meta \n")
                for ex_header, header_value in exo.visible.items():
                    if header_value :
                        if ex_header not in shown_header :
                            
                            
                            other_heading.append(f"{ex_header} {header_value}\n")
                            
                            if(ex_header == "solution"):
                                solution_visible = True
                
                f.write(' | '.join(other_heading) + "\n")
                f.write(" \ \ \n" + "#show: exercise \n" + exo.content + "\n")
                if(solution_visible):
                    f.write("#show: solution_header \n \ \ \n solution \n \ \n")
                    f.write(f"#show: solution \n {exo.solution}")
                f.write(" \ \ \n")

        return

