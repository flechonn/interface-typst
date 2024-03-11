import sys

list_arg = sys.argv[1:]

output = open("output_file.typ", "w")

for file in list_arg:
    f = open(file, "r")
    output.write("\n= New file : " + file + "\n")
    content = f.read()
    output.write(content)