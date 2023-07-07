import TeachersManage.Display as td
def Del(l3=[]):
       if l3==[]:
             print("Database is Empty")
             return l3
       if(input("enter 1 to see all Teachers data before deletation else press any num to no see:")=="1"):
              td.Disp(l3)
       di=-1

       n=input("Enter Teacher id you want to Remove:")
       for i in range(len(l3)):
            for j in range(len(l3[i])):
                   if l3[i][j]==f"id={n}":
                     di=i
                     break
            
     
       if(di!=-1):
             del l3[di]
             print("record deletation successfull!")
             f=open("file2.txt","w")
             for i in range(len(l3)):
                   f.writelines(f"{l3[i][0]},{l3[i][1]},{l3[i][2]},\
{l3[i][3]},{l3[i][4]},{l3[i][5]},{l3[i][6]}\n") 
             print()
             if(input("enter 2 to see all Teachers data after deletation else press any num to no see:")=="1"):
                   td.Disp(l3)
       else:
              print(di)
              print("Teacher in not present in database")

       return l3

                  