
num = int(input("Please enter a number: "))
even_result = "%s is an even number"
odd_result = "%s is an odd number"

if num is 0:
    print("Zero is even. Google it")
elif num % 2 == 0: 
    print(even_result % num)
else:
    print(odd_result % num)    
    # print("The number is odd")
# elif num % 3 == 0
#     print("The number is odd")
# else num === 0
#     print("Zero is even. Google it!")

