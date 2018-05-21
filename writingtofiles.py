from sys import argv
script, file_name = argv

text_file = open(file_name, 'w')
print(text_file)

text_file.write('Adding to the file')
text_file.close()
text_file = open(file_name)
print(text_file.read())