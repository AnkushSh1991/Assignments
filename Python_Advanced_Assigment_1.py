#Assignment_1_Advanced_Python

#Q1. What is the purpose of Python's' OOP?
#Ans - To create a well written,readable and maintainable code which also inhibits concepts like
       #inheritance, polymorphism, encapsulation,abstraction etc. in the programming

#Q2. Where does an inheritance search look for an attribute?
# Ans - Definition Tree

#Q3. How do you distinguish between a class object and an instance object?
#Ans-
class Emp():
   company="CodeTech Technologies" # Class object

   def __init__(self, id, dept):
      self.id = id
      self.dept = dept

emp1 = Emp(10,  "HR") #instance object


#Q4. What makes the first argument in a class’s method function special?
#Ans - The first argument in a class method is always a reference to the current instance of the class. By default, this argument is always named self.

#Q5. What is the purpose of the __init__ method?
#Ans -  The __init__ method works like a Constructor in C++/Java/C#. It initializes the object. T

#Q6. What is the process for creating a class instance?
#Ans -

class my_class(obj):
    #class definition


my_classinstance = my_class.__new__(my_class)

#Q7. What is the process for creating a class?
#Ans -
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#Q8. How would you define the superclasses of a class?
#Ans- The class whose properties gets inherited by another class is known as superclass or parent class

# superclass
class Person():
    def display1(self):
        print("This is superclass")


# subclass
class Employee(Person):
    def display2(self):
        print("This is subclass")




