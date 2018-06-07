# def lower(string):   
#     many = int(input('Enter a number: '))
#     nu_string = string[:many].lower()
#     print(nu_string)


# lower('TESting')

# def much_lower():   
#     many_more = int(input('Enter a number: '))
#     stringyy = input('Enter a string: ')
#     nu_nu_string = stringyy[:many_more].lower()
#     print(nu_nu_string)

# much_lower()

# # def lower(string)
# #     many = int(input('Enter a number: '))


# def string_start():
#     str = input("Please enter a string: ")
#     letter = input("Enter a single letter: ")
#     if str[0] == letter:
#         print('The string starts with', letter)
#     elif str[0] == letter.upper():
#         print('The string starts with an uppercase', letter)
#     else:
#         print('The string does not start with', letter)

# string_start()


# Write a Python program to count and display the vowels of a given text

def vowel_counter():
    texty = input("Please enter some text: ")
    the_vowels = 0
    testing = ['a','A','e','E','i','I','o','O','u','U']
    for i in range(len(texty)):
        for i in testing:
            if testing[i] == texty[i]:    #for i in range(len(str
                the_vowels = the_vowels + 1
        # if vow == 'a'or 'a'.upper(): 
        #     the_vowels = the_vowels + 1 
        # elif vow =='e' or 'e'.upper():
        #     the_vowels = the_vowels + 1 
        # elif vow == 'i' or 'i'.upper():
        #     the_vowels = the_vowels + 1
        # elif vow == 'o' or 'o'.upper():
        #     the_vowels = the_vowels + 1
        # elif vow == 'u' or 'u'.upper(): #or sometimes y
        #     the_vowels = the_vowels + 1
        # else:
        #     continue
    print("There are", the_vowels, " vowels in the supplied text.")

vowel_counter()