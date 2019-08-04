from sys import argv
from os.path import exists
script,from_file,to_file = argv
print(f'we will copy data from {from_file} to {to_file}')
print(f'do we have both files, {exists(from_file)} , {exists(to_file)}')
print(f'do you want to continue')
input('?')
in_file = open(from_file)
in_data = in_file.read()
print(f'length of the file is {len(in_data)}')
out_file = open(to_file,'w')
out_file.write(in_data)
print(f'copied the data')
out_file.close()
in_file.close()