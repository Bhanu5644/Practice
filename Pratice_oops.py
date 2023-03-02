# Oops (Object Oriented Program)
# In Python, object-oriented Programming (OOPs) is a programming paradigm
# that uses objects and classes in programming. It aims to implement real-world entities like inheritance,
# polymorphisms, encapsulation, etc. in the programming

#Class
#Object
#Inhertance
#polymorphism
#Oveloading

#**********CLASS***********
#Class:- Collection of variable(Attribute) and Method (Behaviour,ex. Employed id,Salary),also called blue print,Logical Entity.
#Object:- Object is instance of class,Physical entity, For one class create multiple objects,object are independent.

#Function vs Method
# Function- We can create without closs (def)
# Method - Create inside the class.

class myteam:
    def myfun(self):
        pass
    def display(self):
        print("Robert")
mc1=myteam() #Always Call
mc1.myfun()
mc1.display()

#Example:2
# class myclass:
#     def m1(self):
#         print("This is instance method")
#     def m2(self,num):
#         print(self,num)
# mc=myclass()
# mc.m1()
# # mc.m2(10,20)
# myclass.m2(10,50)

#here we are calling static method directly from using class not through object
#Example:3
# class myclass:
#     a,b = 10,20
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=myclass()
# mc.add()
# mc.mul()

#Example:-4
#Global Variable Come before class.
# i,j = 15,20
# class myclass:
#     a,b =10,20 #class variable
#     def add(self,x,y):
#         print(x+y) #
#         print(self.a+self.b) # Class Variable
#         print(i+j) #Global Variable
# mc = myclass()
# mc.add(100,200)

# a,b = 15,25
# class myclass:
#     a,b =10,20 #class variable
#     def add(self,a,b):
#         print(a+b) #
#         print(self.a+self.b) # Class Variable
#         print(globals()["a"]+globals()["b"]) #Global Variable
# mc = myclass()
# mc.add(150,45)

#one class have multiple objects.
# class myclass:
#     def display(self):
#         print("This is display method")
# obj1=myclass()
# obj1.display("Bhanu")
# obj2=myclass()
# obj2.display("Munish") #we call one function in multiple time.


