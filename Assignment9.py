# 1) Create a module consisting of class holding various data members and member functions.
# (class can be on various file operations or mathematical operations or string operations)

# 2) Import the above module created and try to implement their member functions.

# 3) Also in the same file, create a user defined exception and implement it.
import Assignment9Class as ac
class InvalidChoice(Exception):
    def __init__(self,args):
        super().__init__(args)

b=True
fobj=ac.FileHandle()
try:   
      while(b==True):
           print(       
       "enter c to create a file\n"\
       "enter r to open this file in read mode\n"\
       "enter w to open this file in write mode\n"\
       "enter a to open this file in append mode\n"\
       "enter t to open this file in text mode\n"\
       "enter b to open this file in binary mode\n"\
       "enter u to open this file in binary mode\n"
               )
           ch=input("enter your choice:")
           if(ch=="c"):
               fobj.FileCreate(input("Enter file name which u want to create:"))
           elif(ch=="r"):
               fobj.FileRead(input("Enter file name which u want to open in read mode:"))
           elif(ch=="w"):
                fobj.FileWrite(input("Enter file name which u want to open in write mode:"))
           elif(ch=="a"):
                 fobj.FileAppn(input("Enter file name which u want to open in append mode:"))
           elif(ch=="t"):
                fobj.FileText(input("Enter file name which u want to open in text mode:"))
           elif(ch=="b"):
                fobj.FileBina(input("Enter file name which u want to open in binary mode:"))
           elif(ch=="u"):
                fobj.FileUpdate(input("Enter file name which u want to open in Update mode:"))
           else:
                raise InvalidChoice("Error:user select invalid choice!")
           c=input("Enter 1 to continue else 0 for exit:")
           if(c!="1"):
               b=False
except InvalidChoice as ic:
        print(ic.args[0])
