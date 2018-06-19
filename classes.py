#messing around with classes in Python

class Students:
    def __init__(self,name,e,c):
        self.name = name
        self.email = e
        self.course = c

    def print_info(self):
        print('Below is the student information')
        print(self.name, self.email, self.course)
    
student1 = Students('john', 'john@snail.com', 'math')
student2 = Students('billy bob', 'billy_bob@snail.com', 'hillbillyism')


student1.print_info()

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

def apple():
    print("I AM APPLES")



# class MyStuff(object):
    
#     def __init__(self):
#         self.tangerine = "And now a thousand years between"

#     def apple(self):
#         print("I AM CLASSY APPLES!")

# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)
    
class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around th family",
                        "With pockets full of shells"])
                    
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


#Create a class named Employees with the following attributes: name, dept. ,role, gender

class Employees:
    def __init__(self, name, dept, role, gender):
        self.name = name
        self.dept = dept
        self.role = role
        self.gender = gender
    
    def change_roles(self):
        print("Employee's current role is: ", self.role)
        self.role = input("Please enter a new role for the employee: ")
        print("Employee's role has been updated. Thank you. New role is:", self.role)
    
employee1 = Employees('Clint Barton', 'East Coast Avengers', 'Archer', 'Male')
employee2 = Employees('Bibby', 'Self Care', 'Barber', 'Male')
employee3 = Employees('Jenn', 'Sales', 'Head of Sales', 'Female')
employee4 = Employees('Ashley', 'Engineering', 'Lead Software Engineer', 'Female')
employee5 = Employees('Peter', 'Accounting', 'CFO', 'Male')


employee1.change_roles()