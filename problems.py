########################INSTRUCTIONS ##############################################
#######	Your Names: Paul Gelot												#######
#######	Each member is to submit this file on google classroom				#######													#######
#######	Make sure to include comments explaining your approach to the problem #####
##
	#1: there should be a function for each question. 
	#2: Working code and no comments will result in point loss

###################################################################################



#####################LIst all the resources you used here ####################
##########													################## 
##########													##################
##############################################################################

################## STRINGS ##################################################

# Write a Python program to calculate the length of a string
def string_length(string):
	length = len(string)
	return length

# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

def change_to_upper(str):
  count = 0
  four_count = 0
  for i in range(len(str[:4])):
    if str[i] == str[i].upper():
      count = count + 1
    else:
      continue
    if count >= 2:
      print(str.upper())
  
    
change_to_upper('FUnctionWorks')
    


# Write a Python program to check whether a string starts with specified characters. 

def string_start():
    str = input("Please enter a string: ")
    # str[0] = first
    if str[0] == 'p':
        print('The string starts with a p')
    elif str[0] == 'P':
        print('The string starts with an uppercase P')
    else:
        print('The string does not start with p or P')

string_start()

# Write a Python program to lowercase first n characters in a string. n given by the user

# Write a Python program to swap comma and dot in a string. 
	#Sample string: "32.054,23"
	#Expected Output: "32,054.23"

# Write a Python program to count and display the vowels of a given text

################## CONDITIONALS ##################################################

#4. When squirrels get together for a party, they like to have cigars. 
	#A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
	#Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
	# TODO:

#5. Given a number n, return True if n is in the range 1..10, inclusive. 

#6. Write a Python program to print the index of the character in a string. 
	#Sample string: w3resource
	#Expected output:
	#Current character w position at 0
	#Current character 3 position at 1
	#Current character r position at 2
	#- - - - - - - - - - - - - - - - - - - - - - - - -
	#Current character c position at 8



#Given an integer, , perform the following conditional actions:

	#If  is odd, print Weird
	#If  is even and in the inclusive range of  to , print Not Weird
	#If  is even and in the inclusive range of  to , print Weird
	#If  is even and greater than , print Not Weird


#You are given a string . Your task is to find out if the string  contains: alphanumeric characters, 
	#alphabetical characters, digits, lowercase and uppercase characters. 
	# '''Output Format

	# In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
	# In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
	# In the third line, print True if  has any digits. Otherwise, print False. 
	# In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
	# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
	# '''

################## LOOPS ##################################################

#Given an integer (by the user), print the following:
	#if input = 4, print 1234
	#if input = 14, print 1234567891011121314





################## LISTS ##################################################

# Write a Python program to convert a string in a list


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
	# You are given scores. Store them in a list and find the score of the runner-up.



# Write a function called middle that takes a list and returns a new list that contains
	#all but the first and last elements. For example:
	# '''>>> t = [1, 2, 3, 4]
	# 			>>> middle(t)
	# 			[2, 3]'''


# Take a list, say for example this one:

#  ''' a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#    and write a program that prints out all the elements of the list that are less than 5.
#    '''

# 	'''Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 				Write this in one line of Python.
# 				Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.'''
			

			
################# MORE PRACTICE #######################################################
#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
	#If the given string already ends with 'ing' then add 'ly' instead. 
	#If the string length of the given string is less than 3, leave it unchanged


# Get two integers inputs and print three lines where:
	
	#The first line contains the sum of the two numbers.
	#The second line contains the difference of the two numbers (first - second).
	#The third line contains the product of the two numbers.




#Write a Python program to get a single string from two given strings, separated by a space and swap 
	#the first two characters of each string. 
		#Sample String : 'abc', 'xyz' 
		#Expected Result : 'xyc abz'