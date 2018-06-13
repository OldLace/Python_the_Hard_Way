
# 1. Write a Python program to iterate over dictionaries using for loops

character = {"name": "Walter", "surname": "White", "nickname": "Isenberg", "height": "6 foot 7", "hobby": "trafficking"}

for i in character:
    print(i,":", character[i])

# 2. Write a function that takes a string as a parameter and returns a dictionary. The
# dictionary keys should be numbers from 0 to the length of strings and values should be
# the characters appeared in the string.
print("***************" * 4)

def into_dictionary(string):
    string_dict = {}
    for i in range(len(string)):
        string_dict.update({i:string[i]})    
    print(string_dict)

into_dictionary("quick")

print("***************" * 4)

def make_dict(string):
    the_dict = {}
    key = 0
    for val in string:
        the_dict[key] = val
        key = key + 1
    return the_dict

print(make_dict("test"))


print("***************" * 4)
# a. For example: function call with ‘hello’ should print {0: ‘h’, 1:’e’, 2:’l’, 3: ‘l’ , 4:’o’}
# 3. Write a Python script to check if a given key already exists in a dictionary.

def check_for_key(q):
    for i in character:
        if i == q:
            print("Key exists")
        else:
            continue 

check_for_key("surname")

# 4. Create a dictionary to hold information about pets. Each key is an animal's name, and
# each value is the kind of animal.
# i. For example, 'ziggy': 'canary'
# b. Put at least 3 key-value pairs in your dictionary.

pets = {'Lucky': 'hamster', 'Spot': 'dog', 'Sophia': 'cat', 'Dumbo': 'elephant'}


# c. Use a for loop to print out a series of statements such as "Willie is a dog."
print("******" * 4)
for i in pets:
    print(i, "is a", pets[i])