# Dictionery:- A Dictionery is a collection which is unordered ,changebale(mutable) and indexed.
# In Python Dic always in {} Bracket and they have key and value.
# {Praduct1:100} {Key:Value}
# Ex-1
mydict= {100:"x",205:"y",105:"z"}
print(mydict)

mydict= {"brand":"Hyundai","Model":"i20","Manu":"2022"}
print(mydict["Manu"])
print(mydict["Model"])

#using get command
x=mydict.get("brand")
print(x)

#Ex-3
#Change value in Dictionery
mydict= {
    "brand":"Hyundai"
    ,"Model":"i20","Manu":"2022"
}
mydict["Manu"]=2021
print(mydict["Manu"])

Reading teams from Dic buy loop
#Example-4
# mydict= {"brand":"Hyundai","Model":"i20",
#          "Manu":"2022"
#          }
for i in mydict:
    print(i) # Print only keys
for i in mydict:
    print(mydict[i]) # Print only Value
for x,y in mydict.items():
    print(x,y) # Print both Keys & Value

#Exm-5 Check key is exist in dic or not
# mydict= {"brand":"Hyundai",
#          "Model":"i20","Manu":"2022"
#          }
if "Model" in mydict:
    print("exist")
else:
    print("Not exist")

Example-6 Find number of item in Dict.
mydict= {"brand":"Hyundai",
         "Model":"i20","Manu":"2022"
         }
print(len(mydict)) #3 length of dict

#Exam-7 Adding item it dict
# mydict= {"brand":"Hyundai",
#          "Model":"i20","Manu":"2022"
#          }
# mydict["Colour"]="Red"
# print(mydict)
#Example=8 Delting iteam in dict.
# mydict= {"brand":"Hyundai",
#          "Model":"i20","Manu":"2022"
#          }
mydict.pop("Manu")
# print(mydict)
del mydict["Manu"] #delete manu
print(mydict)
del mydict #Delete all dict show name error
print(mydict)
mydict.clear()
print(mydict) #Will show empty dict. {}

#Example-8 (Want to Copy Dict.)
mydict1= {"brand":"Hyundai",
         "Model":"i20","Manu":"2022"
         }
# mydict2=mydict1
# print(mydict2)
mydict2=mydict1.copy()
print(mydict2)

#Sets you can identify from no Value ,
#Set is collection in ordered
myset={"Mongo","Orange","banana"}
print(type(myset))
print(myset)
