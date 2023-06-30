# 1) Create a function with default parameter "file" storing the file path
# 2) Open the "file" in append mode
# 3) Use writelines() method to add your roll number, name, and class
# 4) Use readines() method to print your data in the prompt

# Note: Use try...except block with suitable exception class

def Func(rollno,name,Class,file="file1.txt"):
     try: 
         f=open(file,"+a")
         f.writelines(["rollno={0}, name={1}, class={2}".format(rollno,name,Class)])
         f.seek(0)
         print(f.readlines())
     except:
          if(IOError):
              print("Exception is handled by io error")
     finally:
        print("file read and write successfull")


roll=int(input("enter your roll no:"))
name=input("enter your name:")
Class=input("enter your class:")
Func(roll,name,Class)