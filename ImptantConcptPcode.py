# print("These are the core fundemantal concept for in programming")
# # start with lists that are used to store multiple items in a single variable
# Frt_list = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"] 

# for i in Frt_list:
#     print(i)
# # print(Frt_list,"\r\n",len(Frt_list))  
# list_1 = [1, 2, 3, 4]
# list_2 = [True, False, True, False, False]
# list_3 = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"] 
# list_4 = [list_1, 30, 20, "Jihad", "Rose", False, True,list_2]
# # print(list_4[0])
# # print(list_4[-1])
# # print(len(list_4),type(list_4))
# Constructor_list = list(('apple', "jackfruit",100, "Papaya"))
# print(Constructor_list,type(Constructor_list))
# print(list_4)
# print(list_4[1:4], list_4[-6: ]) # keep remember indexing method last range is not includes

# if "jihad" in list_4:
#     print("yeah, Jihad has in the list items")
# else:
#     print(" No, Jihad don't has in the list items")    
    
# # How to change the value from list
# #list_4[0] = 'Chang eSomething'    
# print(list_4)
# list_3 [2:4] = ['Bankcurptcy',"yellow" ]
# print(list_3)
# list_3[1:2] = ["Jihad", "Junayed", "Mostaqim who is the most talented Uncle"]
# print(list_3, len(list_3))
# list_3[1:6] = ['Nihad', "Arafat"]
# print(list_3)
# list_3.insert(3, "watermelon")
# print(list_3)
# list_3.append("Orange")
# print(list_3)
# list_3.insert(0, 100)
# print(list_3)
# list_3.extend(list_1)
# print(list_3)
# list_3.append(list_1)
# print(list_3)
# tuple_1 = ("Kiwi", "parrot")

# list_3.extend(tuple_1)
# print(list_3)
# list_3.remove("jackfruit")
# print(list_3)
# list_3.append("Banana")
# print(list_3)
# list_3.remove("Banana")
# print(list_3)
# list_3.pop(1)
# print(list_3)
# list_3.pop()
# print(list_3)
# del list_3[1:3]
# print(list_3)
# # del list_3
# #list_3.clear()
# print(list_3)
# for i in list_3:
#     print(i)

# for i in list_3:
#     if isinstance(i, list):
#         for j in i:
#             print(j)
        
#     else:
#         print(i)    


# # Loop lists
# print("Finish all")
# for k in range(len(list_3)):
#     print(k)

# print("Print list item now")

# for m in range(len(list_3)):


#     print(list_3[m])

# i = 0
# while i < len(list_3):
#      print(list_3[i])
#      i +=1
                                       
# [print(x) for x in list_3]

# import random
# print(random.randrange(1,400))
# print(random)

# List_loop = ['Apple','Banana', "Cherry", 'Mango', "Jackfruit","Banana"]    
  
# for items in List_loop:
#       print(items) 

# for items in range(len(List_loop)):
#     print(items)   
    
# print(len(List_loop))
# while loop
# i = 0
# while i < len(List_loop):
#     print(List_loop[i])
#     i = i +1
# j = 0
# while j < len(List_loop):
#     print(List_loop[j])    
#     j = j + 1
    
# # print("Comprehension Loop")    
# # [ print(x) for x in List_loop ]    

# new_list = []

# for x in List_loop:
#     if "a" in x:
#         new_list.append(x)  
# print(new_list)         
# NewList1  = [ x for x in List_loop if "a" in x ]
# print(NewList1)
# NewList2 = [y for y in List_loop if y != "Apple"]
# print(NewList2)    
# NewList3 = [x for x in List_loop]
# print(NewList3)  

# newlist= [x for x in range(10) if x > 0] 
# print(newlist)   
# newlist5 = [ x.upper() for x in List_loop]
# print(newlist5)     
# helloList = [ "hello" for x in List_loop]
# print(helloList)          
# Fruits = [x if x != "Banana" else "Orange" for x in List_loop]
# print(Fruits)
# List_loop.sort()
# print(List_loop)
# List_loop.sort(reverse=True)
# print(List_loop)

# def myFunc(n):
#     return abs(n-50)

# thislist = [ 100, 50, 65, 82, 23]
# thislist.sort(key = myFunc)
# print(thislist)

# thislist = ["banana", "orange", "kiwi","cherry"]
# thislist.sort()
# print(thislist)


# newList.remove("Banana")// remove method need especefied the value of list
# print(newList)
# newList.pop()
# print(newList)
# del newList[2]
# # del newList[]// without index values it does not work.
# print(newList)
# # del newList
# newList.clear()
# print(newList)
# List have some items such as remove(), pop(),del listname, clear()


    
#include <stdio.h>

# int main()
# {
#     for (int i = 1; i <= 3; i++)
#     {
#         for (int j = 1; j <= 3; j++)
#         {
#             printf("%d %d\n", i, j);
#         }
#     }

#     return 0;
# }     

# isinstance() method is used to check the data type of the variable and it is very important method for problem solving in programming.

# print(isinstance(newList, list))
# List comprehension is a very improtant concept for good programmer.

# newList = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"] 
# secondList = ['Apple','Banana', "Cherry", 'Mango', "Jackfruit","Banana"] 
# newList_one = []
# for x in newList:
#     if "a" in x:
#         newList_one.append(x)

# print(newList_one)    

# newList_two = [ x for x in secondList if "a" in x]
# newList_two = [x for x in secondList if x != "Apple"]

# print(newList_two)

# newList_three = [x for x in secondList]
# print(newList_three)
# newList_four = [x for x in range(5) if x > 3]
# newList_five = [x.upper() for x in secondList]
# print(newList_four)
# print(newList_five)
# newList_six = [ x if x != "Banana" else "Orange" for x in secondList]
# print(newList_six)
# newList_one  = [ x for x in secondList]
# print(newList_one)
# newList_seven = [x for x in newList]
# print(newList_seven)

# Newlist = ['Apple','Banana', "cherry", 'Mango', "jackfruit","Banana"]

# newlist_one = [x for x in Newlist]

# newlist_one = [x for x in Newlist if x != "Apple" ]
# print(newlist_one)
# # Behind the scene, the list comprehension
# # newlist_two = []
# # for x in Newlist:
# #     if x != "Apple":
# #         newlist_two.append(x)
# # print(newlist_two)
# newlist_three = [x for x in Newlist if 'a' in x]
# print(newlist_three)
# # newlist_four = [x for x in range(100) if x % 5 != 0]
# newlist_four = [x for x in range(100) if x % 5 == 0]

# print(newlist_four)
# print("What is the lentgth is ", len(newlist_four), " newlilst_four")
# newlist_five = [x.upper() for x in Newlist]
# print(newlist_five)
# Newlist = ['Apple','Banana',"Goava", "cherry",'watermelon', 'Mango', "jackfruit","Banana"]
# Newlist_one = ['Apple','Banana',"Goava", "Cherry",'Watermelon', 'Mango', "Jackfruit","Banana"]
# Newlist_one.sort()
# print(Newlist_one)

# Number_list = [100, 50, 65, 82, 23, 1, 4, 6, 9, 4,7,5,5]
# Number_list.sort()
# print(Number_list)
# Number_list.sort(reverse = True)
# print(Number_list)
# Newlist_one.sort(reverse = True)
# print(Newlist_one)
# def createFunction(vale):
#     return abs(vale - 1000)

# Number_list.sort(key = createFunction)
# print(Number_list)    
# Newlist = ['Apple','Banana',"Goava", "cherry",'watermelon', 'Mango', "jackfruit","Banana"]
# # Newlist.sort(key = str.lower)
# # print(Newlist)
# Newlist.reverse()
# print(Newlist)

newlist = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist_copy = newlist # this is not a proper way to copy a list

# print(newlist_copy)
# newlist_copy[0] = 'orange'
# print(newlist)

# Actuall way to copy any list
newlist_copy = newlist.copy()
newlist_copy[0] = 'orange'
print(newlist_copy)
print(newlist)
newlist_another_way = list(newlist)
newlist_another_way[0] = 'grapes'   
print(newlist_another_way)
print(newlist)
newlist_final = newlist[:]
newlist_final[0] = 'watermelon'
print(newlist_final)