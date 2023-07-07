def Search1(l3=[]):
      if l3==[]:
           print("Database is Empty")
           return l3
    
      si=-1
      n=input("Enter Teacher id you want to Search:")
      for i in range(len(l3)):
           for j in range(len(l3[i])):
                if l3[i][j]==f"id={n}":
                     si=i
                     break
            
      if(si!=-1):
           print("Searched Teacher Details:")
           for i in range(len(l3[si])):
                print(l3[si][i])
      else:
           print("Teacher in not present in database")


      