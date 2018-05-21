
# - Arguments & Unpacking

from sys import argv
## script is always name of file

script, user_name, second, third, fourth = argv

print("The file name is: ", script)
print("The username is: ", user_name)
print("The second variable is: ", second)
print("The third variable is: ", third)
print("The fourth variable is: ", fourth)



# from sys import argv
# script, file_name = argv
# print(file_name)

# text_file = open(file_name)
# print(text_file)
# print(text_file.read())
