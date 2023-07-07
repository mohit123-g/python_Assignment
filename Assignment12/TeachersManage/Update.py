import TeachersManage.Display as td
def Upd(l3=[]):
      if l3==[]:
           print("Database is Empty")
           return l3      

      ui=-1 
      if(input("enter 1 to see all Teachers data before updatation else press any num to no see:")=="1"):
           td.Disp(l3)

      n=input("Enter Teacher id you want to Update:")
      for i in range(len(l3)):
           for j in range(len(l3[i])):
                if l3[i][j]==f"id={n}":
                     ui=i
                     break
               
                     
      if(ui!=-1):
           print("Enter Teacher Updated details:")
           n="Name="+input("Enter Teacher Name:")  
           if n=="Name=":
                n=l3[ui][0]
           a="Age="+input("Enter Teacher Age:")
           if a=="Age=":
                a=l3[ui][1]
           p="PhoneNum="+input("Enter Teacher phone:")
           if p=="PhoneNum=":
                p=l3[ui][2]
           d="Department="+input("Enter Teacher Department:")
           if d=="Department=":
                d=l3[ui][3]
           s="Subject="+input("Enter Teacher Subject:")
           if s=="Subject=":
                s=l3[ui][4]
           A="Address="+input("Enter Teacher Address:")
           if A=="Address=":
                A=l3[ui][5]
           l3[ui]=[f"{n}",f"{a}",f"{p}",f"{d}",f"{s}",f"{A}",f"{l3[ui][6]}"]
           print("data updatation successfull!")
           f=open("file2.txt","w")
           for i in range(len(l3)):
                f.writelines(f"{l3[i][0]},{l3[i][1]},{l3[i][2]},\
{l3[i][3]},{l3[i][4]},{l3[i][5]},{l3[i][6]}\n") 
           print()
           if(input("enter 1 to see all Teachers data after updatation else press any num to no see:")=="1"):
                td.Disp(l3)
      else:
           print(ui)
           print("Teacher in not present in database")

      return l3
