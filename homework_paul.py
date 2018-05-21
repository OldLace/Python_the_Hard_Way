#importing module to use later
import time

#Get input from user and validate as an integer
print("Note: Follow along in the book to find the numbers you need to complete this activity!")
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))
num4 = int(input("Please enter the fourth number: "))
num5 = int(input("Enter the fifth and final number: "))

end_message = "The average is: %s"
#Adds some flair to this program

print("Calculating the average...")
#Make user think computer is processing data
time.sleep(2)

#Add the numbers and store the total as a variable
total_sum = num1 + num2 + num3 + num4 + num5

#find the average and store it as a variable 
num_average = total_sum / 5

#Print the average
print(end_message % num_average)

num = int(input("Please enter a number: "))
even_result = "%s is an even number"
odd_result = "%s is an odd number"

if num is 0:
    print("Zero is even. Google it")
elif num % 2 == 0: 
    print(even_result % num)
else:
    print(odd_result % num)    