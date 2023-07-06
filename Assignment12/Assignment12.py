# 1) Create a user-defined package to implement respective functions
# 2) The package should have at least 5 modules.
# 3) It should be a menu driven program
# 4) It should be a proper project, such as a management system or a login page
# (if it is a login page then it should navigate to that particular site)
# Note: you need to implement file handling and exception handling in this 
# assignment

# (if you want you can use in-built modules such as tkinter or webbrowser or math
# it's optional)
import StudentManage.Add as sa
import StudentManage.Display as sd
import StudentManage.Remove as sr
import StudentManage.Search as ss
l1=[]
ch=True
while ch==True:
     c=input("Enter 1 to Add Teacher details\n\
Enter 2 to Update Teacher details\n\
Enter 3 to Delete Teacher details\n\
Enter 4 to Search Teacher details \n\
Enter 5 to Display Teacher details\n\
Enter your choice:")
     if c=="1":
         l1.append(sa.AddStu())
         print(l1)
     elif c=="3":
          sr.Del(l1)
     elif c=="4":
          ss.Search1(l1)
     elif c=="5":
         sd.Disp(l1)
     if input("Enter 1 to continue:")!="1":
        ch=False
    
