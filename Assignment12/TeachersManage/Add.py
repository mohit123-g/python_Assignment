def AddStu(file="file2.txt"):
       ls=[]
       print("Enter Teacher details:")
       n=input("Enter Teacher Name:")  
       a=input("Enter Teacher Age:")
       p=input("Enter Teacher phone:")
       d=input("Enter Teacher Department:")
       s=input("Enter Teacher Subject:")
       A=input("Enter Teacher Address:")
       ls.extend([f"Name={n}",f"Age={a}",f"Phone={p}",f"Department={d}",f"Subject={s}",f"Address={A}"])
    #    print(ls)
       f=open(file,"+a")
       f.writelines(f"{ls[0]},{ls[1]},{ls[2]},\
{ls[3]},{ls[4]},{ls[5]},\n")
       return ls
# "Mohit",18,"1234556699","IF","C++","Mumbai"

