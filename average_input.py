#importing module to use later
import time

#Get input from user and validate as an integer
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
#if num_average = 67.6
#    print("You completed question 2, part i")
