from sys import argv
script, file_name = argv

text = open(file_name)
print(f"here is your file name {file_name}")
print(text.read())
text.close()
prompt = "#$"
print(f"type the file name again")
file_name_again = input(prompt)
text2 = open(file_name_again)
print(text2.read())
text2.close()