# # Method:
# # 1- Give any name
# # 2- Return the Vaulue
# # 3- Method can take arguments & Parameters
# # 4- We have to use an object to invoke the method
# #
# # Constructors- it will start with __int__
# # Name is fixed
# # Constructor will not return any value
# # Constructor can take arguments & Parameters
# # Cosntructor will be called at the time of object creation itself.
#
# # Example1.
# # class myclass:
# #     def __init__(self):
# #         print("This is Constrauctor") #Not required to Call this
# #         print("Bhanu Sharma")
# #     def m1(self):
# #         print("Hello")
# # mc=myclass()
# # mc.m1()
#
# # #Example 2
# # class myclass:
# #     name ="Bhanu Sharma"
# #     def __init__(self,name): #Constructor expecting 1 argument
# #         print(name)
# #         print(self.name)
# # mc=myclass("Munish Sandhu")
#
# # Example3
# # class emp:
# #     def __init__(self,empid,empname,Salary):
# #         self.empid=empid
# #         self.empname=empname
# #         self.Salary=Salary
# #     def Display(self):
# #         print(self.empid,self.empname,self.Salary)
# # e1=emp(125,'Bhanu',50000)
# # e2=emp(212,'Munish',55000)
# # e1.Display()
# # e2.Display()
#
# # Example 4
# # class emp:
# #     def __init__(self,empid,empname,Salary):
# #         self.empid=empid
# #         self.empname=empname
# #         self.Salary=Salary
# #     def __str__(self):
# #         return (self.Salary)
# # e1=emp('101',"Rahul",'35000')
# # e2=emp('102',"Ajay",'45000')
#
#
# print(e1,e2)