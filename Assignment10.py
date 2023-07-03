
# 1) Implement the tkinter and webbrowser module
# 2) create a gui for taking input from the user and create a button to navigate to a browser site.
# 3) Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses
# Note:
# [you cannot use Google search]
# you can use YouTube, etc.

import tkinter as tk
import webbrowser as wb

obj=tk.Tk(className="MOhit")

e=tk.Entry(obj,font=("Time New Roman",20),width=30)
def Nav():
    n=e.get()
    print("user entered text is:"+n)
    print(f"you are navigating to www.{n}.com'")
    wb.open("www."+n+".com")
l1=tk.Label(obj,text="Enter name of any website:",font=("Time New Roman",30))
b1=tk.Button(obj,text="Search",font=("Time New Roman",30),command=Nav,bg="blue")
l1.grid(row=0,column=0)
e.grid(row=1,column=0)
b1.grid(row=2,column=0)

obj.mainloop()
