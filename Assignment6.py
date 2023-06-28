# 1)Create a function named ds with parameters roll_no and name.
# 2)Add those parameters in the following data structures:
# list, tuple, sets and dictionaries
# 3) After adding values
# change the values during runtime
# 4)Delete these data structures


def ds(roll_no,name):
     ls=[]
     tu=()
     se=set()
     dis={}

     ls.append([roll_no,name])
     tu1=((roll_no,name))
     tu+=tu1
     se.add((roll_no,name))
     dis={"roll_no":roll_no,"name":name}

     print("before modify of values of data structure:")
     print("list:",ls)
     print("tupal",tu)
     print("set:",se)
     print("distionary:",dis)

     print()
     new_roll=int(input("Enter new roll_no:"))
     new_name=input("Enter new name:")

     ls[0]=[new_roll,new_name]
     tu=((new_roll,new_name))
     se.update((new_roll,new_name)) 
     dis["roll_no"]=new_roll
     dis["name"]=new_name

     print()
     print("After modify of values of data structure:")
     print("updated values of list:",ls)
     print("updated values of tupal:",tu)
     print("updated values of set:",se)
     print("updated values of distionary:",dis)
     del ls,tu,se,dis
    #  print(ls)
    #  print(tu)
    #  print(se)
    #  print(dis)

roll=int(input("enter your roll no:"))
name=input("enter your name:")
ds(roll,name)
print()      