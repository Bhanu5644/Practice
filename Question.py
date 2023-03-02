#How reverse String?
C= "The Distance between Bharatpur from Panipat was 315 KM"
rev_Str=""
for i in C:
    rev_Str=i+rev_Str
print(rev_Str)
#How skip Digit in list?
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(b[0: :3])
#Call Single Tupple?
MyTupple =("Bhanu","Sharma","Vani")
print(type[MyTupple])
print(MyTupple[0])
#Print the format in Dictionary & Capital of State?
Dic={"Rajasthan":"Jaipur","Haryana":"Chandigarh","Uttar Pradesh":"Lucknow"}
# print(Dic["Rajasthan"])
# print(Dic["Uttar Pradesh"])
for x,y in Dic.items():
    print(x,y)

f="I Love India"
rev_str=""
for a in f:
    rev_str=a+rev_str
print(rev_str)
#How reverse Value INT?
# e =[0,1,2,3,4,5,6,7,8,9]
# print(e[0: :2])
# e =[0,1,2,3,4,5,6,7,8,9]
# print(e[-1: :-1])
# original_list = [1, 2, 3, 4, 5]
# print("List before reverse : ",original_list)
# reversed_list = []
# for value in original_list:
#   reversed_list = [value] + reversed_list
# print("List after reverse : ", reversed_list)

List1 = [1,2,3,4,5] #manual list reverse
print("list before:",List1)
List2 = []
for i in List1:
    List2 = [i] + List2
print("List after:",List2)
