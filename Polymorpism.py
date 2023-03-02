#overloading (polymorpism)
#Example 1
class Parent:
    name="Munish"
class Child(Parent):
    name = "Ashish"
cobj=Child()
print(cobj.name)

#Example 2
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello"+name)
        else:
            print("Hello")
H=Human()
H.sayhello("Munish")

#Exampel 3
class calculation:
    def add(self,a=0,b=0,c=80):
        print(a+b+c)
cobj=calculation()
# cobj.add()
cobj.add(10,20)
# cobj.add(10,50,70)