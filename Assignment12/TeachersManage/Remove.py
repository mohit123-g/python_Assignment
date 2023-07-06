def Del(l3=[]):
     di=None  
     for i in range(len(l3)):
          for j in range(len(l3[i])):
               print(l3[i][j])
          print()

     n=input("Enter Teacher Name you want to remove:")
     for i in range(len(l3)):
          for j in range(len(l3[i])):
               if l3[i][j]==f"Name={n}":
                   di=i
     del l3[di]       
     for i in range(len(l3)):
          for j in range(len(l3[i])):
               print(l3[i][j])
          print()
                  