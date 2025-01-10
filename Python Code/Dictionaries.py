#Dictionaries are used to store data values in key:value pairs, can be referred to by using the key name.
#dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "Club": "Man City", #("key" : "value")
  "Coach": "Pep",
  "year": 2016
}   #written with curly brackets
print(thisdict)

#accessing
print(thisdict["year"])#use square brackets to access value of a key
print(thisdict.get("Coach")) #can use get() method with 
x = thisdict.keys()
print(x) #using keys() method returns list of all keys in a dictionary
y = thisdict.values()
print(y) #vales() method returns list of values in a dictionary
z = thisdict.items()
print(z)# item() method returns list of all items in a dictionary
#use in keyword to determine if a specific key is present in a dictionary
if "year" in thisdict:
    print('yes, the year of assumtption is one of theb keys in this dictinoanry')

#use len() fucntion to determine number of items in a dictionary
print(len(thisdict))
#dictionaries are objects with data type 'dict'
print(type(thisdict))

#adding items
thisdict["level"] = "God-tier"
#changing items
thisdict["Coach"] = "Guadiola"
print(thisdict)
#thisdict.update({"year" : 2026}) #can use update() method to change/update values and keys

#removing items
thisdict.pop("year") #removes the item from the dictionary 
thisdict.popitem() #removes the last inserted item/ random item for older versions of python
del thisdict["level"] #del keyword can be used to remove item or the entire dictionary
thisdict.clear() #empties the dictionary

#Loop throiugh a dictionary
for x in thisdict:
    print(x) #prints all key names in dictionary one by one 
print(thisdict[x]) #prints all values in dictioanry one by one
for x in thisdict.values():
    print(x) #can use values() method to return values in a dictionary
for x in thisdict.keys():
    print(x) # returns all keys in the dictionary
for x, y in thisdict.items(): 
    print (x, y) #loops through both key and values

#copying a dictionary
citydict = thisdict.copy() #can use copy method
print(citydict)
citydict = dict(thisdict) # can use dict()fuction

#Nested dictionaries are dictionaries that contain other dictionaries



