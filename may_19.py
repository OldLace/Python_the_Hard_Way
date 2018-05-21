#May 19 - Paul Gelot

#Python the Hard Way - Exercise 12
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
total_sum = num1 + num2
subtract = num1 - num2 
product = num1 * num2
division1 = num1 / num2

print("The sum of the two numbers is:", total_sum)
print("The difference between the two numbers is:", subtract)
print ("The product of the two numbers is:", product)

print(25 * "**")
print(int(division1))
print(division1)



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




from sys import argv
script, file_name = argv

text_file = open(file_name, 'w')
print(text_file)

text_file.write('Adding to the file')
text_file.close()
text_file = open(file_name)
print(text_file.read())


#Importing 
import math
thenumber = int(input("Please enter a number: "))
print(int(math.sqrt(thenumber)))


# Two Files - I got it... I think
from sys import argv

script, filename1, filename2 = argv
# txt = filename.read()

text_file1 = open(filename1)
info = text_file1.read()
# print(info)


text_file2 = open(filename2, 'w')
text_file2.write(info)
text_file2.close()
text_file2 = open(filename2, 'r')
info2 = text_file2.read()
# text_file2.write(info)
print(info2)
