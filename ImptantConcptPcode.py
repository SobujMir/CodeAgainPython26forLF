print("These are the core fundemantal concept for in programming")
# start with lists that are used to store multiple items in a single variable
Frt_list = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"] 

for i in Frt_list:
    print(i)
print(Frt_list,"\r\n",len(Frt_list))  
list_1 = [1, 2, 3, 4]
list_2 = [True, False, True, False, False]
list_3 = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"] 
list_4 = [list_1, 30, 20, "Jihad", "Rose", False, True,list_2]
print(list_4[0])
print(list_4[-1])
print(len(list_4),type(list_4))
Constructor_list = list(('apple', "jackfruit",100, "Papaya"))
print(Constructor_list,type(Constructor_list))
print(list_4)
print(list_4[1:4], list_4[-6: ]) # keep remember indexing method last range is not includes

if "jihad" in list_4:
    print("yeah, Jihad has in the list items")
else:
    print(" No, Jihad don't has in the list items")    
    
# How to change the value from list
#list_4[0] = 'Chang eSomething'    
print(list_4)
list_3 [2:4] = ['Bankcurptcy',"yellow" ]
print(list_3)
list_3[1:2] = ["Jihad", "Junayed", "Mostaqim who is the most talented Uncle"]
print(list_3, len(list_3))
list_3[1:6] = ['Nihad', "Arafat"]
print(list_3)
list_3.insert(3, "watermelon")
print(list_3)
list_3.append("Orange")
print(list_3)
list_3.insert(0, 100)
print(list_3)
list_3.extend(list_1)
print(list_3)
list_3.append(list_1)
print(list_3)
tuple_1 = ("Kiwi", "parrot")

list_3.extend(tuple_1)
print(list_3)
list_3.remove("jackfruit")
print(list_3)
list_3.append("Banana")
print(list_3)
list_3.remove("Banana")
print(list_3)
list_3.pop(1)
print(list_3)
list_3.pop()
print(list_3)
del list_3[1:3]
print(list_3)
# del list_3
list_3.clear()
print(list_3)
