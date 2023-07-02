# // 1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)
# // 2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in 
# // a parameterized constructor
# // 3) Create a method known as display in both the classes, to display the values of a,b and c
# // 4) While accessing the private member an exception should be raised and a personalized message 
# // should be displayed and the exception should be handled properly so that the rest of the code can get executed

class A:
      def __init__(self,A1,B1,C1):
           self.__a=A1
           self._b=B1
           self.c=C1

      def display(self):
          print("this is class A")
          print("a=",self.__a)
          print("b=%d"%(self._b))
          print(f"c={self.c}")


class B(A):
       
     def display(self):
         super().display()
         print("This is class B")
         try:
              print("a=",self.__a)
              raise AttributeError
         except AttributeError as t:
              print("Error:you are trying to access private member of base class!")
         print("b=%d"%(self._b))
         print(f"c={self.c}")
               


B1=B(10,20,30)
B1.display()