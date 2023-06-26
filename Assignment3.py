choice=True
print("Calculator")
while choice==True:
     n1=int(input("Enter first num:"))
     op=input("Enetr operator like(+,-,*,/,%,**,//):")
     n2=int(input("Enter second num:"))
     if op=="+":
         print("Ans:",n1,"+",n2,":",n1+n2)
     elif op=="-":
         print("Ans:",n1,"-",n2,":",n1-n2)
     elif op=="*":
         print("Ans:",n1,"*",n2,":",n1*n2)
     elif op=="/":
         print("Ans:",n1,"/",n2,":",n1/n2)
     elif op=="%": 
         print("Ans:",n1,"%",n2,":",n1%n2)
     elif op=="**":
         print("Ans:",n1,"**",n2,":",n1**n2)
     elif op=="//": 
         print("Ans:",n1,"//",n2,":",n1//n2)
     else:
         print("invalid operator entered")

     print("Enter 1 to continue or 0 for exit:")
     cho=int(input())
     if cho==0:  
         choice=False
