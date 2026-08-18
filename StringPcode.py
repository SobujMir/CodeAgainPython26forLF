# print("Hello python")
# print("It's alright")
# print('He is called "johnny')
# # How to write a multi-line string in python.
# a = """ Now I can write a multi-line string in python.
# I can write as many lines as I want.
# I want to be a consistent programmer from today in 18 august
# """

# b = '''It is also similar to previous way of writing multi-line,
# but Now the differnce is between quatation marks.
#  If you want to write string under single quatation marks then you can use this way of writing multi-line string in python.'''
# print(a, b)

# a = "Hello World Python"
# print(len(a),a[0], a[9],a[0:6])
# print(a[6:12])

# # Loop concept in string in python
# for x in "Python":
#     print(x)
 
# str1 = "Python is dynamic."
# for x in str1:
#      print(x)

# txt = "Jihad is a good gamer \"Because\" he play a lot. "
# print(txt, '\n\n\n', len(txt))     
# print("free" in txt, "\n","Because" in txt, "good" in txt)     

# if "Sobuj" in txt:
#     print("Yes, 'Jihad' is present in the string.")
# else:
#     print("No, 'Jihad' is not present in the string.")
    
# print("present" not in txt, "b" not in txt, "lot" not in txt, "Jihad" not in txt)    

a = "Hello World Python"
# print(a[2:7])# index slicing end number is not included in the output.
# print(a[1:])

# Negative indexing
print(a[-6:])
print(a.upper(),a.lower())
# print(upper(a))# syntex error

a ="    Hello, , Python"
print(a.strip())
print(a.replace("P", "H"))
print(a.replace("Hello", "World"))
print(a.split())
b = "Hello"
c = "world"

d = b + c
print(d)

print(b+ " " +c)
age = 50
# txt = "My name is demon, I am " + age # syntax error

txt = f"My name is Demon, I am {age}"

print(txt)
print(f"This product price is {age} dollar")
print(f"This product price is {age:.3f} dollar")
print(f"What will be the multiplication both number is  {20*10} is working")
#Escape character
txt = " \r We are done so-called\n \"\\Fuck\" is this relation"
print(txt)

txt1= "hello coding, and welcome aFter a long time."
print(txt1.capitalize())
print(10> 9, 100 ==10, 2==2)
m = 100
n = 200

if m > n :
    print(" M is greater than n")
else:
    print(" n is greater than M")  
print(bool("Hello"))  
print(bool(13))    
print(bool(0))
print(bool(False), bool(True),bool(()))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()

print(bool(myobj))    

def myFunction():
    return False
print(myFunction())
if myFunction():
    print("YES!")
else:
    print("NO!")    
    
x = 100

print(isinstance(x, int), isinstance(x, str))    