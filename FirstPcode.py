print("Wellcome back to coding earth.")
print("Wellcome to Consistency and Discipline")
# print("Because those are the key to success in any field of life.")
# print("Hello, World!")

# import sys
# print(sys.version)
#Python programming Indentation is very important. It is used to define the blocks of code. Python uses indentation to indicate a block of code. The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount.

# if 5 > 2:
# print("Five is greater than two!")# this code does not work because the print statement is not indented properly. It should be indented to indicate that it is part of the if statement block.
    
    
# if 5 > 4:
#     print("Five is greater than four!")
#     print("This is a properly indented block of code.")
    
# # Python Statements
# # Statements are instructions that a Python interpreter can execute. A statement is a logical line of code that performs a specific action. In Python, statements can be simple or compound.
              
# print("Python is Fun!")
# # Python statements are executed one by one.
# print("Python is easy to learn.")
# print("Python is a powerful programming language.")
# print("It is used for versatile applications.")
# # Semicolons can be used to separate multiple statements on a single line.
# print("Hello");print("World");print("Python is great!")
# print('Single quotes are working')

# # Uese of end function in python
# print("Hello", end=" ");print("World", end=" ")
# print("Python is great!", end="\n")
# # Use of Print function in python
# print("Coding is Fun", 100 , "If you have passion about it")
# print(5, 4*5)
# print(" I am ", 25)
# Variables in Python
# X = 5
# Y = "Python"
# print(Y, "is", X, "time faster than other programming languages.")

# V_variable = 10,
# print(V_variable)  

#Variable casting

# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0
# print(x,"\n", y, z)
# print(type(x), type(y), type(z))

# X = "Sobuj"
# Y = 'Sobuj'
# print(X, Y, type(X), type(Y))



# Variable naming rules in Python which is very crucial for good coder.

# Person_name ="Sobuj Mir who is very poor in English"
# Person_country = "Bangladesh in South Asia"

# print(Person_name, Person_country)

# # Assignment of multiple values to multiple variables in Python
# Name, Age, Nationality = "Jihad",10, "Bangladeshi"
# print(Name, Age, Nationality)

# x = 10
# y = 14
# sum = x + y
# print(sum)

# Global variables and Local variables in Python
# X = "Global Variable"
# def Ownfunc():
#     y = "Local Variable"
#     print("Inside the function:", y)
#     print("Inside the function:", X)
    
# Ownfunc()

#print("Outside the function:", y) # Here y does not exist

# Globar keyword use

# def myfunc():
#     global x 
#     x = "Global Variable"
    
# myfunc()
# #x = "Local Variable"
# print("Outside the function:", x) # Here x is global variable    

# # Data types in Python

# All_types =["str=String","int = number", "float = decimal value", "complex = complex value", "list, tuple,range","dict, set,frozenset","bool = True or False", "bytes, bytearray, memoryview", "NoneType = None"]
# # this is called list in python

# print(All_types)
# print(type(All_types))


# Python Numbers
x,y,z = 5, 2.5, 1j
print(type(x), type(y), type(z))

# python convert types
# x = float(x) # convert from int to float
# y = int(y)   # convert from float to int        
# z = complex(z) # convert from int to complex
# print(x, y, z)
# print(type(x), type(y), type(z))
# m = 5+3j
# print(m, type(m))
n =int(y)
print(n, type(n)) # this will give error because complex number cannot be converted to int or float
# Random number generation in Python

import random

print(random.randrange(1, 100))
# One object have data and behavior

import random

x = random.randrange(70,99)
if x > 80:
    print("You are lucky person because you got ", x)
elif x > 90:
    print("You are super lucky person because you got ", x)    
else:
    print("You are unlucky person because you got ", x)