def Disp(l3=[]):
      if l3==[]:
           print("Database is Empty")
      else:
           print("All Teachers Details")
           for i in range(len(l3)):
                for j in range(len(l3[i])):
                     print(l3[i][j])
                print()