# Create a gui based form to take input from the user and then navigate to
# the particular site from where the user came to know about the content

# for example:
# create a form where the user is enquiring about the respective course
# and in the form there is an option for asking where the user came to
# know about it, for eg: instagram ads or YouTube ads

# and then when clicking the submit button
# take the user to the faq page of that site

import tkinter as tk
import webbrowser as wb

root=tk.Tk(className="Spotify Form")
l1=tk.Label(root,text="Spotify Form",font=("Times New Roman",30),bg="SeaGreen1")

l2=tk.Label(root,text="First Name:",font=("Times New Roman",20),bg="SeaGreen1")
e2=tk.Entry(root,font=("Times New Roman",20),width=25)
l3=tk.Label(root,text="Last Name:",font=("Times New Roman",20),bg="SeaGreen1")
e3=tk.Entry(root,font=("Times New Roman",20),width=25)
l4=tk.Label(root,text="Email:",font=("Times New Roman",20),bg="SeaGreen1")
e4=tk.Entry(root,font=("Times New Roman",20),width=25)
l5=tk.Label(root,text="Enter Song Name:",font=("Times New Roman",20),bg="SeaGreen1")
e5=tk.Entry(root,font=("Times New Roman",20),width=25)
l6=tk.Label(root,text="Select website where you see this song ad:",font=("Times New Roman",20),bg="SeaGreen1")
l7=tk.Label(root,font=("Times New Roman",15),bg="SeaGreen1")

select= tk.StringVar()
drop=tk.OptionMenu(root,select,"Youtube.com","Facebook.com","Instagram.com")

def submitForm():
    if e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or select.get()=="":
         l7["text"]="!please fill required information"
    else:
        try:
            f=open("file1.txt","+w")   
            f.writelines(f"First Name:{e2.get()}\nLast Name:{e3.get()}\n\
Email:{e4.get()}\nSong:{e5.get()}\nWebsite:{select.get()}") 
        except IOError:
            print("Form data storage Error")
        wb.open("https://community.spotify.com/t5/FAQs/tkb-p/Spotify-Answers")

b1=tk.Button(root,text="SUBMIT",font=("Times New Roman",20),command=submitForm,)
l1.grid(row=0,column=3)

l2.grid(row=2,column=0)
e2.grid(row=2,column=3)
l3.grid(row=3,column=0)
e3.grid(row=3,column=3)
l4.grid(row=4,column=0)
e4.grid(row=4,column=3)
l5.grid(row=5,column=0)
e5.grid(row=5,column=3)
l6.grid(row=6,column=0)
drop.grid(row=6,column=3)
l7.grid(row=7,column=3)
b1.grid(row=8,column=3)
root.configure(bg="SeaGreen1")

tk.mainloop()
