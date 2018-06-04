
import math
print("Testing!!!")

#1. How many seconds are there in 42 minutes 42 seconds?
def seconds_forty_two():
    seconds = (42 * 60) + 42
    print("There are", seconds, "seconds in 42 minutes, 42 seconds")

seconds_forty_two()

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
#0.621371 * 10
def miles_ten_km():
    miles = 0.621371 * 10
    print("There are", miles, "miles in 10 kilometers.")

miles_ten_km()




# 3. How much is 83 degree Fahrenheit in degree celsius   
def eighty_three():
    converted = (83 - 32) * (5/9) 
    print(converted)

eighty_three()

# 4. import math library and find the square root of numbers 81, 19, 16, 121
def square_root():
    num1 = math.sqrt(81)
    print(num1)
    num2 = math.sqrt(19)
    print(num2)
    num3 = math.sqrt(121)
    print(num3)

square_root()
# 5. write a program that returns the area of a circle with radius r= 9
# 6. write a boolean function that returns true or false if the letter x is in a string provided by
# the user

if 

# 7. write a boolean function that returns true or false if any of the letter a, e, i, o, u and in a
# string provided by the user
# 8. Write a boolean function that returns true if a given input is divisible by 3 or return false
# otherwise
# def three():
#     thing = input("Enter a number: ")
    
#     if thing % 3 == 0:
#         print("True")
#     else:
#         print("False")

# three()
# 9. Import data/time library and print out today’s data and current time
import time

print(time.ctime())

# 10. write a function that counts how many times the letter a is repeated in a given word (get
# the work from the user as an input)

