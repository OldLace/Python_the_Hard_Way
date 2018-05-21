# from sys import argv
# script, file_name = argv
# print(file_name)

# text_file = open(file_name)
# print(text_file)
# print(text_file.read())


#####################################

#import argv method from sys
from sys import argv

#define script & filename as argument
script, filename = argv


txt = open(filename)

#displays message and name of file
print(f"Here's your file {filename}:")

#displays contents of text file
print(txt.read())

#Asks for filename 
print("Type the filename again:")
file_again = input("> ") #seeks input from user for file name

#Uses input from previous line
txt_again = open(file_again) 

#displays contents of second text file
print(txt_again.read())