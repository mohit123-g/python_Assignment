class FileHandle:
     filer=None
     filew=None
     filea=None
     filet=None
     fileb=None

     def FileRead(self,file="file1.txt"):
         self.filer=open(file,"r")
         self.filer.seek(0)
         print(f"{file} contents:")
         print(self.filer.readlines())

     def FileWrite(self,file="file1.txt"):
         self.filew=open(file,"w")
         self.filew.seek(0)
         con=input(f"enter content u want to write in {file}:")
         self.filew.writelines(con)
         self.filew.seek(0)
         print(f"{file} contents:")
         self.FileRead(file)

     def FileAppn(self,file="file1.txt"):
         self.filea=open(file,"a")
         self.filea.seek(0)
         print(f"{file} contents before append:")
         self.FileRead(file)
         self.filea.seek(0)
         con=input(f"enter content u want to write in {file}:")
         self.filea.writelines(con)
         self.filea.seek(0)
         print(f"{file} contents after append:")
         self.FileRead(file)
        
     def FileText(self,file="file1.txt"):
         self.filet=open(file,"tr")
         self.filet.seek(0)
         print(f"{file} contents:")
         print(self.filet.readlines())

     def FileBina(self,file="img1.jpg"):
         self.fileb=open(file,"rb")
         self.fileb.seek(0)
         print(f"{file} contents:")
         print(self.fileb.read())
     
     def FileUpdate(self,file="file1.txt"):
         self.filea=open(file,"+a")
         self.filea.seek(0)
         print(f"{file} contents before update:")
         self.FileRead(file)
         self.filea.seek(0)
         con=input(f"enter content u want to update in {file}:")
         self.filea.writelines(con)
         self.filea.seek(0)
         print(f"{file} contents after update :")
         self.FileRead(file)
    
