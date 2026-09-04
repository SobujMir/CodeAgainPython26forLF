# tuple = "tuples are used to store multiple item in a single variable"
# print(tuple)
# # round bracket = () = parenthesis
# tuple = ("apple", "mango", "banana", "cherry", "jackfruit", "papaya")
# print(tuple)
# print(len(tuple))
# print(type(tuple))
# print(tuple[0])
# print(tuple.__len__())
# print(tuple[-1])

# tuple1 = 1, 2, 3, 4, 5, 6, 7, 8, 9,2,2
# # tuple1 [0] = 100 # this will give an error because tuple is immutable
# print(tuple1)
# print(tuple1[2:5])

# print(tuple1)
# # One significant concept that when you create a tuple if this tuple has only one value then you have to put a comma. otherwise it will be considered as a string or integer or float or boolean
# tuple2 = (10,)  # This is a tuple with one element
# print(tuple2)
# print(type(tuple2))
# tuple3 = (10)  # This is not a tuple, it's an integer
# print(tuple3)
# print(type(tuple3))
# tuple4 = ()
# print(type(tuple4))
# tuple5 = ("apple", "banana", "cherry", "kiwi", "mango")
# tuple6 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# tuple7 = (True, False, True, False, True)
# # print(tuple5,"\n", tuple6, "\n", tuple7)
# # tuple_add = tuple5 + tuple6 + tuple7
# # print(tuple_add)
# # tuple = tuple(("apple", "banana", "cherry", "kiwi", "mango"))
# # print(tuple)
# # print(tuple.count("apple"))
# # print(type(tuple))
# # tuple accessing almost same as list accessing
# tuple = ("apple", "banana", "cherry", "kiwi", "mango")
# print(tuple[0])
# print(tuple[-1])
# print(tuple[2:5])
# print(tuple[2:])
# print(tuple[:4])
# print(tuple[-4:-1])
# print(tuple[-4:])

# if "apples" in tuple:
#     print("Yes, 'apple' is in the tuple")

# else:
#     print("No, 'apples' is not in the tuple")
tuple1 = ("apple", "banana", "cherry", "kiwi", "mango")
x = list(tuple1)
x[1] = "promegranate"
print(x)
x.append("watermelon")

tuple1 = tuple(x)
print(tuple1)
y = ("papaya", "jackfruit", "guava")
tuple1 += y
print(tuple1)
x = (100,)
tuple1 += x
print(tuple1)

x = list(tuple1)
x.remove("kiwi")
x.pop()
tuple1 = tuple(x)
print(tuple1)
# del tuple1
# print(tuple1)  # This will give an error because tuple1 is deleted
fruits = "apple", "banana", "cherry", "kiwi", "mango"
print(fruits, type(fruits))
(x,*y, z) = fruits
print(x, "\n",y)
print(z)

for i in fruits:
    print(i)

for i in range(len(fruits)):
    print(i)

j = 0 

while j < len(fruits):
    print(fruits[j])
    j = j + 1

tuple1 = ("a", 'b', 'c', 'd', 'e')
tuple2 = (1, 2, 3, 4, 5,3,3,3,3)
tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = tuple2* 2
print(tuple4)
print(tuple2.index(5))
tuple2.count(2)
print(tuple2.count(3))

