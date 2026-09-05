Setlist = {'apple', 'banana', 'cherry', 'kiwi', 'mango',"apple",True, 1,False, 0}
print(Setlist)
print(type(Setlist))
print(len(Setlist))

for x in Setlist:
    print(x)
set2 = {"apple", "banana",1,4, 7, True, False, 3.5}
print(set2)
# set constructor
set3 = set(("apple", "banana", "cherry", "kiwi", "mango"))
# print(set3)
# set3.add(1)
# print(set3)
# print("apple" in set3)
# print("grapes" not in set3)
# print("banana" not in set3)
# set3.remove("banana")
# print(set3)
# set3.update(set2)
# print(set3)
OneList = [10,100, 202,"tree,","animal"]
# set3.update(OneList)
# print(set3)
# set3.discard("kiwi")
# set3.remove("banana")
# # set3.remove("men")
# print(set3)
# set3.pop()
# print(set3)
# set3.clear()
# print(set3)
# del set3
# print(isinstance(set3, set))  # This will give an error because set3 is deleted
# There are several way to join sets like union(), update(), intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference() and difference_update(), difference()

# set2.update(set3)
set2 = set2 | set3
# set2.union(set3)
# set3.intersection(set2)
# set3.symmetric_difference(set2)
print(set2)
# print(set3)
set4 = {1,101,300,40}
set5 = {"men", "difference", "form",'women'}
set6 = set2.union( set3, set4, set5)
tuple1 = (1, 100, 2020, 1030)
print(set6)
set6.update(tuple1)
print(set6)
# newSet = set6.union(tuple1)
# print(newSet)
set_var = set2.intersection(set3)
set_var2 = set4 & set5
print(set_var2)
print(set_var)
set_1 = {'apple', 'annar', 'mango'}
set_2 = {1, 2,'mango'}
# set_3 = set_1.difference(set_2)
# print(set_3)
sets = set_1 - set_2
print(sets)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
set1.pop()
print(set1)

forzn_set = frozenset({'apple'," cherry", "mango",'etcetra'})
print(forzn_set)
