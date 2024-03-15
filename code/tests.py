import exercise as e
import re
def tests():
    path = "../BD/format.tex"

    exo1 = e.loadExerciseLatex(path)
    print(exo1.metadata)

tests()

# line = "\setMeta{title}{Mon Title}"
# if "\setMeta" in line: 
#     extractedwords = re.search(r"\\setMeta\{(\w+)\}\{(.+?)\}", line)
#     print(extractedwords.group(1))