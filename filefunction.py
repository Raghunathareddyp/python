from sys import argv
script_name,file_name=argv
current_file = open(file_name)
def print_all(f):
    output = f.read()
    print(output)

def rewind(f):
    f.seek(0)

def print_single_line(f,line):
    print(line, f.readline())

def print_one_line(f,n):
    file = open(f)
    line = file.seek(n)
    print(file.readline())
print(f"let print the hole file {file_name}")
print_all(current_file)
print("lets rewind, kind of tape")
rewind(current_file)
print("lets print three lines")
current_line = 1
print_single_line(current_file,current_line)
current_line += 5
print_single_line(current_file, current_line )
#print('lets print all lines again ')
#rewind(current_file)
#print_all(current_file)
current_line +=  10
print_single_line(current_file, current_line)

#print_one_line(file_name,2)