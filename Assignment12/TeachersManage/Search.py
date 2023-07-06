def Search1(l3=[]):
     si=None
     n=input("Enter Teacher Name you want to remove:")
     for i in range(len(l3)):
          for j in range(len(l3[i])):
               if l3[i][j]==f"Name={n}":
                   si=i


     for i in range(len(l3[si])):
          print(l3[si][i])