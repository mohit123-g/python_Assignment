print("For Loop filter")
name="Mohit Gupta"
for i in name:
     if(i=="p"):
         pass
     elif(i=="G"):
         continue
     elif(i=="pt"):
          break
     else:
         print(i)
else:
     print("Loop is break")


print()
print("While Loop filter")
ls=[1,2,44,5,"mg",78]
i=0
while(i<=(len(ls)-1)):
    if(ls[i]==44):
          pass
    elif(ls[i]==5):
         i+=1
         continue
    elif(ls[i]=="mg"):
          break
    else:
          print(ls[i]) 
    i+=1
else:
     print("while is break")
    

print()
print("While Loop filter odd num")
i2=0
while(i2<=20):
     if(i2%2!=0):
         i2+=1
         continue
     else:
        print(i2)
     i2+=1