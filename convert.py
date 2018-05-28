
print("Here are a list of options: ")
print("1. To convert kilobytes to bytes")
print("2. To convert megabytes to bytes")
print("3. To convert terabytes to bytes ")
print("4. To convert terabytes to megabytes")


selected_option = input("Please select an option: ")
# user_input = int(input("Enter kilobytes: "))
user_input = 0



#to byte
def kilobytes(user_input): 
    user_input = int(input("Enter kilobytes: "))
    answer1 = user_input * 1024
    print(user_input, "kilobytes is equal to",  answer1, "bytes")

# to byte
def megabytes(user_input): 
    user_input = int(input("Enter amount to be converted in megabytes: "))
    answer1 = user_input * 1000000
    print(user_input, "megabytes is equal to",  answer1, "bytes")

#to byte
def terabytes(user_input): 
    user_input = int(input("Enter amount to be converted in terabytes: "))
    answer1 = user_input * 1000000000000
    print(user_input, "terabytes is equal to", answer1, "bytes")

#to megabyte
def tera(user_input):
    user_input = int(input("Enter amount to be converted in terabytes: "))
    answer1 = user_input * 1000000
    print(user_input, "terabytes is equal to", answer1, "bytes")

if selected_option == "1":
    kilobytes(user_input)
elif selected_option == "2":
     megabytes(user_input)
elif selected_option == "3":
    terabytes(user_input)
elif selected_option == "4":
    tera(user_input)
else:
    print("Please select from one of the options!")

