# #Python the Hard Way Exercise 38


# ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print("Wait there are not 10 things in that list. Let's fix that. ")

# stuff = ten_things.split(' ')
# more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

# print("There we go: ", stuff)

# print("Let's do some things with stuff.")

# print(stuff[1])
# print(stuff[-1]) #whoa! fancy
# print(stuff.pop())
# print(' '.join(stuff)) #what? cool!
# print('#'.join(stuff[3:5]))


# #Exercise 39

# #create a mapping of state to abbreviation

# state = {
#     'Oregon': 'OR',
#     'Florida': 'FL',
#     'California': 'CA',
#     'New York': 'NY',
#     'Michigan': 'MI',
# }

# cities = {
#     'CA': 'San Francisco',
#     'MI': 'Detroit',
#     'FL': 'Jacksonille',
# }

# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'

# #print out some cities
# print('-' * 10)
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])

# # print some states
# print('-' * 10)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida has: ", cities[states['Florida']])

# #print every state abbreviation
# print('-' * 10)
# for state, abbrev in list(states.items()):
#     print(f"{state} is abbreviated {abbrev}")
#     print(f"and has city {cities[abbrev]}")

print('-' * 10)


things = {"name": "Bobby", "surname": "Johnson", "nickname": "OG", "height": "6 foot 7", "hobby": "eating"}

print(things)
print('-' * 5)

for i in things: 
    print(i, ":", things[i])