# Inheritance in pyhton

# Four pillers of OOPS
# 1. Inheritance - code Re-usability - Extending a property from one class to another class
# Base Class - parent class
# Derived class - Child class
# 2. Polymorphism
# 3. Abstraction
# 4. Encapsulation

# class Team:
#     def team_name(self):
#         print("Real Madrid")
# class Player(Team):
#     def info(self):
#         print("Name : K Mabappe")
#         print("Position : CF(center forword)")
# obj=Player()
# obj.team_name()
# obj.info()

# class Team:
#     def team_name(self):
#         print("Real Madrid")
# class Player(Team):
#     def info(self):
#         print("Name : K Mabappe")
#         print("Position : CF(center forword)")
# class Country(Player):
#     def country(self):
#         print("Country : France")
# obj=Country()
# obj.team_name()
# obj.info()
# obj.country()


# Class Parent1:
# Class Parent2:
# Class Parent3:
# Class Derived class(Parent1,Parent2,Parent3):

# Multiple Inheritance

# class Team:
#     goal=int(input("Enter the goals scored in a year: "))
#     assist=int(input("Enter the assist in a year: "))
# class Player:
#     form=input("Enter the form throughout the the year (Good/Moderate/Bad): ")

# class Eligible(Team,Player):
#     def info(self):
#         if self.goal>=100 and self.assist>=50 and self.form=="Good":
#             print("The player is eligible to win the Ballon'dor")
#         else:
#             print("Not Eligible")
# obj=Eligible()
# obj.info()

# Polymorphism

# Polymorphism means having many forms
# We can define polymorphism as the ability of a message to be displayed in more than one form.
# there are two types of polymorphism
# Compile Time - function overloading
# Run Time - function overriding

class A:
    def role(self):
        print("Hi i am A")
class B:
    def role(self):
        print("Hi i am B")
class C:
    def role(self):
        print("Hi i am C")
class D:
    def role(self):
        print("Hi i am D")
def func(obj):
    obj.role()
E=[A(),B(),C(),D()]
for obj in E:
    func(obj)