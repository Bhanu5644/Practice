#Exmaple1
V= lambda a:a+10
print(V(20))

m=lambda a,b,c,d:a*b+c-d
print(m(2,7,9,10))

# list =[10,78,45,15,35]
# list.sort(key=lambda x:x[1])
# print(list)

r="Bhanu"
rev = ""
for i in r:
    rev= i+rev
print(rev)

list = [45,78,12,96,85]
print(sorted(list))
print(list)
rev_list=[]
for i in list:
    rev_list=[i]+rev_list
print(rev_list)