# 1) Create a user-defined package to implement respective functions
# 2) The package should have at least 5 modules.
# 3) It should be a menu driven program
# 4) It should be a proper project, such as a management system or a login page
# (if it is a login page then it should navigate to that particular site)
# Note: you need to implement file handling and exception handling in this 
# assignment

# (if you want you can use in-built modules such as tkinter or webbrowser or math
# it's optional)
import TeachersManage.Add as sa
import TeachersManage.Update as su
import TeachersManage.Remove as sr
import TeachersManage.Search as ss
import TeachersManage.Display as sd

class InvalidChoice(Exception):
     def __init__(self,args):
        super().__init__(args)
l1=[]
b=True
id=0
try:   
      
      while(b==True):
           print()
           ch=input("Enter 1 to Add Teacher details\n\
Enter 2 to Update Teacher details\n\
Enter 3 to Delete Teacher details\n\
Enter 4 to Search Teacher details \n\
Enter 5 to Display Teacher details\n\
Enter your choice:")
           if(ch=="1"):
               id+=1
               l1.append(sa.AddStu(id))  
               print(l1)
           elif(ch=="2"):
               l1=(su.Upd(l1))
           elif(ch=="3"):
               l1=(sr.Del(l1))
           elif(ch=="4"):
               ss.Search1(l1)
           elif(ch=="5"):
               sd.Disp(l1)
           else:
                raise InvalidChoice("Error:user select invalid choice!")
           c=input("Enter 1 to continue else 0 for exit:")
           if(c!="1"):
               b=False
except InvalidChoice as ic:
        print(ic.args[0])