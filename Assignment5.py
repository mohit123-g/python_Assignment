# Take input from the user of 5 numbers and store it in a list.
# Perform below operations:
# 1) Calculate the sum of all the elements in the list
# 2) Find the smallest number
# 3) Find the largest number
# 4) Display list in ascending order
# 5) Display list in descending order
# 6) Convert list into tuple
# 7) Delete the list

ls=[]
for i in range(1,6,1):
     ls.append(int(input("Enter any num:")))
print("sum of all element in list:",sum(ls))
print("smallest element in list:",min(ls))
print("largest element in list:",max(ls))
ls.sort()
print("Display list in descending order:",ls)
ls.reverse()
print("Display list in descending order:",ls)
del ls
print(" Delete list",ls)