filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    c_line = line.strip().replace('Python', 'C')
    print(c_line)