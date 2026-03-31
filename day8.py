# class Student:
#     roll_no=101
#     num1=23
#     num2=20

#     def add(self):
#         print(self.num1+self.num2)
#         self.name=input("Enter the name : ")
#         print(self.name)
# obj=Student()
# obj.add()
# print(obj.roll_no)
# print(obj.num1)

# self variable

# In class level or in function first argument must be self
# By using constructor we initialize the object - asssigning the memory to object
# when we create object constructor calls automatically 
# __init__(self) - constructor
# for one object the constructor call ones

# class NewClass:
#     def __init__(self):
#         print("Constructor always executes first")
#     def show(self):
#         print("Welcome to class level programming")
# obj=NewClass()
# obj.show()
# obj1=NewClass()
# obj2=NewClass()
# obj2=NewClass()

# Default Constructor

# class Hod:
#     def __init__(self):
#         self.name="Basavaraj"
#         self.age=21
#         self.emp_id=101
#     def info(self): # instance method
#         print("My name is :",self.name)
#         print("My age is :",self.age)
#         print("My employee ID is :",self.emp_id)
# obj=Hod()
# obj.info()

# Parameterized constructor

# class Hod:
#     def __init__(self,name,age,emp_id):
#          self.name=name
#          self.age=age
#          self.emp_id=emp_id
#     def info(self): # instance method
#          print("My name is :",self.name)
#          print("My age is :",self.age)
#          print("My employee ID is :",self.emp_id)
# obj=Hod('Basu',21,101)
# obj.info()

# How many types of variable we declare inside a class
# 1. instance var - it create separate memory for each object
# 2. static var - it create same memory for evey object
# 3. local va

# class New:
#     def __init__(self):
#         self.a=10
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=30
# print(obj1.a)
# obj2.a=30
# print(obj2.a)

# There are two ways to access the static variable
# 1. By class name
# 2. By object reference - we cannot modify or delete then we use class

# class New:
#     a=10
#     def __init__(self):
#         self.name="Basavaraj"
# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.name)
# print(New.a)
# New.a=70
# print(obj1.a)
# print(obj2.a)

# There are three types of methods
# 1. Class method
# 2. Static method - we can use static method when the code that belongs to class it do not use the object
# 3. Instance method - if any instance variable we are implementing inside of any method then that method will be called as instance method.
# instance method should have self as parameter

# class Hod:
#     def __init__(self,name,age,emp_id):
#         self.name=name
#         self.age=age
#         self.emp_id=emp_id
#     def info(self): # instance method
#         print(self.name," ",self.age," ",self.emp_id)
# obj=Hod('Basu',21,101)
# obj.info()

# class Hod:
#     @staticmethod
#     def get_personal_detail(fName,lName):
#         print("Your personal detail = ",fName,lName)
#     @staticmethod
#     def contact(mob,roll):
#         print("Your contact detail = ",mob,roll)
# Hod.get_personal_detail("Basu","Ghasti")
# Hod.contact(8197361037,21)

class Student:
    school="HSIT"
    @classmethod
    def get_school(cls):
        return cls.school
print(Student.get_school())
