class FileHandle:
     filer=None
     filew=None
     filea=None
     filet=None
     fileb=None
     filec=None

     def FileCreate(self,file):
         try:
           self.filec=open(file,"x")
           print(f"{file} created successfully")
           c1=input(f"Do you want to write data in {file} so enter 'w' else enter 'e' to leave it empty:")
           if(c1=="w"):
                 self.FileWrite(file)
         except FileExistsError:
             print(f"{file} already exist") 

     def FileRead(self,file):
         try:
             self.filer=open(file,"r")
             self.filer.seek(0)
             print(f"{file} contents:")
             print(self.filer.readlines())
         except FileNotFoundError:
              print(f"{file} not found!")

     def FileWrite(self,file):
         c1=input(f"warning write mode will override {file} data do you want override then enter 'w' else enter 'l' to leave:")
         if(c1=="w"):
             self.filew=open(file,"w")
             self.filew.seek(0)
             c2=input(f"if you want to write single line in {file} enter 's'\n\
or if you want to write multiple lines in {file} enter 'm'\nenter your choise:")
             if(c2=="s"):
                 con=input(f"enter content u want to write in {file}:")
                 self.filew.write(con)
             if(c2=="m"): 
                 con=input(f"enter contents u want to write in {file}:")
                 self.filew.writelines(con)
             c3=input(f"do you want to see {file} contents enter 's' else 'n' to not see:")
             if(c3=="s"):
                 self.filew.seek(0)
                 self.FileRead(file)

     def FileAppn(self,file):
         self.filea=open(file,"a")
         self.filea.seek(0)
         c1=input(f"if you want to see {file} contents before append enter 's' else enter any 'n' to not see ")
         if(c1=="s"):
             print(f"{file} contents before append:")
             self.FileRead(file)
             self.filea.seek(0)
         c2=input(f"if you want to write single line in {file} enter 's'\n\
or if you want to write multiple lines in {file} enter 'm'\nenter your choice:")
         if(c2=="s"):
             con=input(f"enter content u want to append in {file}:")
             self.filea.write(con)
         elif(c2=="m"): 
             con=input(f"enter contents u want to append in {file}:")
             self.filea.writelines(con)
         c3=input(f"do you want to see {file} contents after append enter 's' else 'n' to not see:")
         if(c3=="s"):
             self.filea.seek(0)
             print(f"{file} contents after append:")
             self.FileRead(file)
        
     def FileText(self,file):
         c1=input(f"if you want to open {file} in read text mode then enter 'r'\n\
or if you want to open {file} in write text mode then enter 'w'\nenter your choice:"
                  )
         if(c1=="r"):
             self.filet=open(file,"rt")
             self.filet.seek(0)
             print(f"{file} contents:")
             print(self.filet.readlines())
         elif(c1=="w"):
              c1=input(f"warning write mode will override {file} data do you want override then enter 'o' else enter 'l' to leave:")
              if(c1=="o"):
                  self.filet=open(file,"wt")
                  self.filet.seek(0)
                  c2=input(f"if you want to write single line in {file} enter 's'\n\
or if you want to write multiple lines in {file} enter 'm'\nenter your choise:")
                  if(c2=="s"):
                     con=input(f"enter content u want to write in {file}:")
                     self.filet.write(con)
                  elif(c2=="m"): 
                     con=input(f"enter contents u want to write in {file}:")
                     self.filet.writelines(con)
                  c3=input(f"do you want to see {file} contents enter 's' else 'n' to not see:")
                  if(c3=="s"):
                     self.filet.seek(0)
                     self.FileRead(file)

     def FileBina(self,file):
         c1=input(f"if you want to open {file} in read text mode then enter 'r'\n\
or if you want to open {file} in write text mode then enter 'w'\nenter your choice:"
                  )
         if(c1=="r"):
             self.fileb=open(file,"rt")
             self.fileb.seek(0)
             print(f"{file} contents:")
             print(self.fileb.readlines())
         elif(c1=="w"):
              c1=input(f"warning write mode will override {file} data do you want override then enter 'o' else enter 'l' to leave:")
              if(c1=="o"):
                  self.fileb=open(file,"wt")
                  self.fileb.seek(0)
                  c2=input(f"if you want to write single line in {file} enter 's'\n\
or if you want to write multiple lines in {file} enter 'm'\nenter your choise:")
                  if(c2=="s"):
                     con=input(f"enter content u want to write in {file}:")
                     self.fileb.write(con)
                  elif(c2=="m"): 
                     con=input(f"enter contents u want to write in {file}:")
                     self.fileb.writelines(con)
                  c3=input(f"do you want to see {file} contents enter 's' else 'n' to not see:")
                  if(c3=="s"):
                     self.fileb.seek(0)
                     self.FileRead(file)

     
     def FileUpdate(self,file):
         self.fileu=open(file,"+a")
         self.fileu.seek(0)
         c1=input(f"if you want to see {file} contents before update enter 's' else enter any 'n' to not see: ")
         if(c1=="s"):
             print(f"{file} contents before update :")
             print(self.fileu.readlines())
             self.fileu.seek(0)
         c2=input(f"if you want to update single line in {file} enter 's'\n\
or if you want to update multiple lines in {file} enter 'm'\nenter your choice:")
         if(c2=="s"):
             con=input(f"enter content u want to update in {file}:")
             self.fileu.write(con)
         elif(c2=="m"): 
             con=input(f"enter contents u want to update in {file}:")
             self.fileu.writelines(con)
         c3=input(f"do you want to see {file} contents after update enter 's' else 'n' to not see:")
         if(c3=="s"):
             self.fileu.seek(0)
             print(f"{file} contents after update:")
             print(self.fileu.readlines())
    
