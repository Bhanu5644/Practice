# Inhertance:-
# Acquiring al1 attributes (variables) and behaviours(methos)from one class to another class is called as Inhertance,
# class A--> a,b,¢_m1()m2()_ A is Parenetclass
# ClassB(A)-->> x,Z m3()--->> B is called child class of A Class
# Objective of Inhertance:
# code Re-usuability
# Avoid Duplicatoin
# Type of Inheretance:
# 1. Single--> Parents>Child
# 2. MultipleLevel --> Parents->Child->Child->Child
# 3. Heirarchy --> Single parents Multi Child
# 4. Multiple--> Multi Parents Single Child
#
# Example 1 Single Inhertance
class a:
    def m1(self):
        print("This is m1 from class A")
class b(a):
    def m2(self):
        print("This is m2 from class b")
obj=b()
obj.m1()
obj.m2()
# Example 2 Single Inhertance
class a:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class b(a):
    a,b =30,40
    def m2(self):
        print(self.a*self.b)
obj=b()
obj.m1()
obj.m2()
#Example 3 Multilevel Inheritance
class a:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)
class b(a):
    a,b =30,40
    def m2(self):
        print(self.a*self.b)
class c(b):
    c,d =60,40
    def m3(self):
        print(self.c-self.d)
cobj=c()
cobj.m1()
cobj.m2()
cobj.m3()
# Exmaple 4 Heirarchy Inheritance
# class a:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class b(a):
#     a,b =30,40
#     def m2(self):
#         print(self.a*self.b)
# class c(b):
#     c,d =60,40
#     def m3(self):
#         print(self.c-self.d)
# bobj=b()
# bobj.m1()
# bobj.m2()
#
# cobj=c()
# cobj.m2()
# cobj.m3()
# Example 5 Multiple Inhertance
# class a: # Parents
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class b(): #parents
#     a,b =30,40
#     def m2(self):
#         print(self.a*self.b)
# class c(a,b):
#     c,d =60,40
#     def m3(self):
#         print(self.c-self.d)
# cobj=c()
# cobj.m1()
# cobj.m2()
# cobj.m3()

r= [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,9]
m=[]
for i in r:
    if i not in m:
        m.append(i)
print(m)

class a:
    x,y =10,20
    def m1(self):
        print(self.x+self.y)
class b(a):
    a,b =30,40
    def m2(self):
        print(self.a-self.b)
class c(b):
    c,d = 50,70
    def m3(self):
        print(self.c*self.d)
h=c()
h.m1()
h.m2()
h.m3()